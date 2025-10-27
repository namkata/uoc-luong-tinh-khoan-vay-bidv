from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

class SalaryCalculator:
    def __init__(self):
        # Thuế suất thu nhập cá nhân theo bậc thang
        self.tax_brackets = [
            (5000000, 0.05),    # Đến 5 triệu: 5%
            (10000000, 0.10),   # Từ 5-10 triệu: 10%
            (18000000, 0.15),   # Từ 10-18 triệu: 15%
            (32000000, 0.20),   # Từ 18-32 triệu: 20%
            (52000000, 0.25),   # Từ 32-52 triệu: 25%
            (80000000, 0.30),   # Từ 52-80 triệu: 30%
            (float('inf'), 0.35) # Trên 80 triệu: 35%
        ]
        
        # Mức giảm trừ gia cảnh
        self.personal_deduction = 11000000  # 11 triệu/tháng
        self.dependent_deduction = 4400000  # 4.4 triệu/người phụ thuộc
        
        # Tỷ lệ bảo hiểm xã hội
        self.social_insurance_rate = 0.08   # 8%
        self.health_insurance_rate = 0.015  # 1.5%
        self.unemployment_insurance_rate = 0.01  # 1%
        
        # Mức lương tối đa đóng bảo hiểm
        self.max_insurance_salary = 29800000  # 29.8 triệu

    def calculate_insurance(self, basic_salary):
        """Tính bảo hiểm xã hội, y tế, thất nghiệp"""
        insurance_base = min(basic_salary, self.max_insurance_salary)
        
        social_insurance = insurance_base * self.social_insurance_rate
        health_insurance = insurance_base * self.health_insurance_rate
        unemployment_insurance = insurance_base * self.unemployment_insurance_rate
        
        total_insurance = social_insurance + health_insurance + unemployment_insurance
        
        return {
            'social_insurance': social_insurance,
            'health_insurance': health_insurance,
            'unemployment_insurance': unemployment_insurance,
            'total_insurance': total_insurance,
            'insurance_base': insurance_base
        }

    def calculate_personal_income_tax(self, taxable_income):
        """Tính thuế thu nhập cá nhân theo bậc thang"""
        if taxable_income <= 0:
            return 0
        
        tax = 0
        remaining_income = taxable_income
        prev_bracket = 0
        
        for bracket_limit, rate in self.tax_brackets:
            if remaining_income <= 0:
                break
                
            taxable_at_bracket = min(remaining_income, bracket_limit - prev_bracket)
            tax += taxable_at_bracket * rate
            remaining_income -= taxable_at_bracket
            prev_bracket = bracket_limit
            
        return tax

    def calculate_salary(self, basic_salary, allowances=0, dependents=0):
        """Tính toán lương chi tiết"""
        # Tổng thu nhập
        gross_income = basic_salary + allowances
        
        # Tính bảo hiểm
        insurance_info = self.calculate_insurance(basic_salary)
        total_insurance = insurance_info['total_insurance']
        
        # Thu nhập chịu thuế
        total_deduction = self.personal_deduction + (dependents * self.dependent_deduction)
        taxable_income = max(0, gross_income - total_insurance - total_deduction)
        
        # Tính thuế thu nhập cá nhân
        personal_income_tax = self.calculate_personal_income_tax(taxable_income)
        
        # Lương thực lĩnh
        net_salary = gross_income - total_insurance - personal_income_tax
        
        return {
            'basic_salary': basic_salary,
            'allowances': allowances,
            'gross_income': gross_income,
            'insurance_details': insurance_info,
            'total_deduction': total_deduction,
            'taxable_income': taxable_income,
            'personal_income_tax': personal_income_tax,
            'net_salary': net_salary,
            'dependents': dependents
        }

# Khởi tạo calculator
calculator = SalaryCalculator()

@app.route('/')
def home():
    return jsonify({
        'message': 'API Tính Lương - Salary Calculator API',
        'version': '1.0.0',
        'endpoints': {
            '/calculate': 'POST - Tính lương chi tiết',
            '/tax-brackets': 'GET - Xem bậc thuế',
            '/insurance-rates': 'GET - Xem tỷ lệ bảo hiểm'
        }
    })

@app.route('/calculate', methods=['POST'])
def calculate_salary():
    try:
        data = request.get_json()
        
        # Validate input
        basic_salary = float(data.get('basic_salary', 0))
        allowances = float(data.get('allowances', 0))
        dependents = int(data.get('dependents', 0))
        
        if basic_salary <= 0:
            return jsonify({'error': 'Lương cơ bản phải lớn hơn 0'}), 400
        
        if dependents < 0:
            return jsonify({'error': 'Số người phụ thuộc không thể âm'}), 400
        
        # Calculate salary
        result = calculator.calculate_salary(basic_salary, allowances, dependents)
        
        return jsonify({
            'success': True,
            'data': result
        })
        
    except ValueError as e:
        return jsonify({'error': 'Dữ liệu đầu vào không hợp lệ'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tax-brackets', methods=['GET'])
def get_tax_brackets():
    """Lấy thông tin bậc thuế"""
    brackets = []
    prev_limit = 0
    
    for limit, rate in calculator.tax_brackets:
        if limit == float('inf'):
            brackets.append({
                'from': prev_limit,
                'to': 'Trên ' + f"{prev_limit:,.0f}".replace(',', '.'),
                'rate': f"{rate*100}%"
            })
        else:
            brackets.append({
                'from': prev_limit,
                'to': limit,
                'rate': f"{rate*100}%"
            })
        prev_limit = limit
    
    return jsonify({
        'tax_brackets': brackets,
        'personal_deduction': calculator.personal_deduction,
        'dependent_deduction': calculator.dependent_deduction
    })

@app.route('/insurance-rates', methods=['GET'])
def get_insurance_rates():
    """Lấy thông tin tỷ lệ bảo hiểm"""
    return jsonify({
        'social_insurance_rate': f"{calculator.social_insurance_rate*100}%",
        'health_insurance_rate': f"{calculator.health_insurance_rate*100}%",
        'unemployment_insurance_rate': f"{calculator.unemployment_insurance_rate*100}%",
        'max_insurance_salary': calculator.max_insurance_salary
    })

@app.route('/estimate', methods=['POST'])
def estimate_salary():
    """Ước tính nhanh lương thực lĩnh"""
    try:
        data = request.get_json()
        basic_salary = float(data.get('basic_salary', 0))
        
        if basic_salary <= 0:
            return jsonify({'error': 'Lương cơ bản phải lớn hơn 0'}), 400
        
        # Ước tính đơn giản (không tính phụ cấp và người phụ thuộc)
        result = calculator.calculate_salary(basic_salary, 0, 0)
        
        return jsonify({
            'success': True,
            'basic_salary': basic_salary,
            'estimated_net_salary': result['net_salary'],
            'total_deductions': result['insurance_details']['total_insurance'] + result['personal_income_tax']
        })
        
    except ValueError:
        return jsonify({'error': 'Dữ liệu đầu vào không hợp lệ'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)