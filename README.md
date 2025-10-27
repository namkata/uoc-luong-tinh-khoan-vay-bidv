# 💰 Công cụ Tính Lương - Salary Calculator

Ứng dụng web tính lương với giao diện tương tự BIDV, bao gồm Flask API backend và HTML/JavaScript frontend.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Tính năng

- 🚀 **Ước tính lương nhanh**: Tính lương thực lĩnh từ lương cơ bản
- 📊 **Tính lương chi tiết**: Tính toán đầy đủ với phụ cấp, người phụ thuộc
- 💸 **Tính thuế thu nhập cá nhân**: Theo bậc thang thuế Việt Nam 2024
- 🏥 **Tính bảo hiểm**: Bảo hiểm xã hội, y tế, thất nghiệp
- 🎨 **Giao diện đẹp**: Thiết kế tương tự BIDV, responsive
- 📱 **Mobile-friendly**: Hoạt động tốt trên mọi thiết bị

## 📁 Cấu trúc dự án

```
uoc-luong-tinh-khoan-vay-bidv/
├── 🐍 app.py              # Flask API server
├── 🌐 index.html          # Frontend interface  
├── 📦 requirements.txt    # Python dependencies
└── 📖 README.md          # Hướng dẫn sử dụng
```

## 🚀 Cài đặt nhanh

### Yêu cầu hệ thống

- ✅ Python 3.7+ (để chạy Flask API)
- ✅ Web browser hiện đại (Chrome, Firefox, Edge, Safari)
- ✅ Windows/macOS/Linux

### 📥 Bước 1: Cài đặt Python

#### Windows:
1. Tải Python từ [python.org](https://www.python.org/downloads/)
2. **QUAN TRỌNG**: Chọn "Add Python to PATH" khi cài đặt
3. Khởi động lại Command Prompt/PowerShell

#### macOS:
```bash
# Sử dụng Homebrew
brew install python3
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Kiểm tra cài đặt:
```bash
python --version    # Hoặc python3 --version
pip --version       # Hoặc pip3 --version
```

### 📦 Bước 2: Clone và cài đặt dependencies

```bash
# Clone repository (nếu có)
git clone <repository-url>

# Hoặc tải zip và giải nén

# Di chuyển vào thư mục dự án
cd uoc-luong-tinh-khoan-vay-bidv

# Cài đặt dependencies
pip install -r requirements.txt

# Nếu gặp lỗi, thử:
pip3 install -r requirements.txt
```

## 🎯 Chạy ứng dụng

### 🔥 Bước 1: Khởi động Flask API

```bash
# Chạy server Flask
python app.py

# Hoặc nếu gặp lỗi:
python3 app.py
```

✅ **Thành công khi thấy**:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

🌐 API sẽ chạy tại: `http://localhost:5000`

### 🌐 Bước 2: Mở giao diện web

#### Cách 1: Mở trực tiếp
- Double-click vào file `index.html`
- Hoặc kéo thả file vào trình duyệt

#### Cách 2: Sử dụng Live Server (Khuyến nghị)
```bash
# Cài đặt live-server (chỉ cần 1 lần)
npm install -g live-server

# Chạy live server
live-server --port=3000
```

#### Cách 3: Python HTTP Server
```bash
# Python 3
python -m http.server 3000

# Python 2
python -m SimpleHTTPServer 3000
```

🎉 **Truy cập**: `http://localhost:3000`

## 🔧 Kiểm tra hoạt động

### Test API
```bash
# Test endpoint trang chủ
curl http://localhost:5000/

# Test tính lương
curl -X POST http://localhost:5000/estimate \
  -H "Content-Type: application/json" \
  -d '{"basic_salary": 15000000}'
```

### Test Frontend
1. Mở `http://localhost:3000` (hoặc file index.html)
2. Nhập lương cơ bản: `15000000`
3. Click "Tính lương ngay"
4. Kiểm tra kết quả hiển thị

## 📚 API Documentation

### 🏠 1. Trang chủ
- **URL**: `GET /`
- **Mô tả**: Thông tin API và danh sách endpoints
- **Response**: JSON với thông tin API

### 📊 2. Tính lương chi tiết
- **URL**: `POST /calculate`
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
    "basic_salary": 15000000,    // Lương cơ bản (bắt buộc)
    "allowances": 3000000,       // Phụ cấp (tùy chọn)
    "dependents": 2              // Số người phụ thuộc (tùy chọn)
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "data": {
      "basic_salary": 15000000,
      "allowances": 3000000,
      "gross_income": 18000000,
      "insurance_details": {
        "social_insurance": 1200000,
        "health_insurance": 225000,
        "unemployment_insurance": 150000,
        "total_insurance": 1575000
      },
      "taxable_income": 2625000,
      "personal_income_tax": 131250,
      "net_salary": 16293750,
      "dependents": 2
    }
  }
  ```

### ⚡ 3. Ước tính lương nhanh
- **URL**: `POST /estimate`
- **Body**:
  ```json
  {
    "basic_salary": 15000000
  }
  ```

### 💸 4. Xem bậc thuế
- **URL**: `GET /tax-brackets`
- **Response**: Danh sách bậc thuế và mức giảm trừ

### 🏥 5. Xem tỷ lệ bảo hiểm
- **URL**: `GET /insurance-rates`
- **Response**: Tỷ lệ các loại bảo hiểm

## 📖 Công thức tính toán

### 💰 1. Bảo hiểm xã hội (2024)
- **Bảo hiểm xã hội**: 8% lương cơ bản
- **Bảo hiểm y tế**: 1.5% lương cơ bản  
- **Bảo hiểm thất nghiệp**: 1% lương cơ bản
- **Mức lương tối đa đóng BHXH**: 29.8 triệu VNĐ/tháng

### 🧮 2. Thuế thu nhập cá nhân (Bậc thang 2024)
| Thu nhập chịu thuế/tháng | Thuế suất |
|--------------------------|-----------|
| Đến 5 triệu              | 5%        |
| Từ 5-10 triệu           | 10%       |
| Từ 10-18 triệu          | 15%       |
| Từ 18-32 triệu          | 20%       |
| Từ 32-52 triệu          | 25%       |
| Từ 52-80 triệu          | 30%       |
| Trên 80 triệu           | 35%       |

### 👨‍👩‍👧‍👦 3. Giảm trừ gia cảnh (2024)
- **Bản thân**: 11 triệu VNĐ/tháng
- **Người phụ thuộc**: 4.4 triệu VNĐ/người/tháng

### 🔢 4. Công thức tính lương thực lĩnh
```
1. Tổng thu nhập = Lương cơ bản + Phụ cấp
2. Tổng bảo hiểm = BHXH + BHYT + BHTN
3. Giảm trừ gia cảnh = 11 triệu + (Số người phụ thuộc × 4.4 triệu)
4. Thu nhập chịu thuế = Tổng thu nhập - Tổng bảo hiểm - Giảm trừ gia cảnh
5. Thuế TNCN = Tính theo bậc thang
6. Lương thực lĩnh = Tổng thu nhập - Tổng bảo hiểm - Thuế TNCN
```

## 🎮 Hướng dẫn sử dụng

### 📱 Giao diện chính

#### Tab "Ước tính lương" 🚀
1. Nhập **lương cơ bản** (VD: 15000000)
2. Click **"Tính lương ngay"**
3. Xem kết quả ước tính nhanh

#### Tab "Tính lương chi tiết" 📊
1. Nhập **lương cơ bản** (bắt buộc)
2. Nhập **phụ cấp** (tùy chọn)
3. Nhập **số người phụ thuộc** (tùy chọn)
4. Click **"Tính lương ngay"**
5. Xem kết quả chi tiết với breakdown

### 💡 Ví dụ tính toán

#### Ví dụ 1: Lương 15 triệu
```
Input:
- Lương cơ bản: 15,000,000 VNĐ
- Phụ cấp: 0 VNĐ
- Người phụ thuộc: 0

Output:
- Tổng thu nhập: 15,000,000 VNĐ
- Bảo hiểm: 1,575,000 VNĐ (10.5%)
- Thuế TNCN: 131,250 VNĐ (0.875%)
- Lương thực lĩnh: 13,293,750 VNĐ
```

#### Ví dụ 2: Lương 25 triệu + phụ cấp + 2 người phụ thuộc
```
Input:
- Lương cơ bản: 25,000,000 VNĐ
- Phụ cấp: 5,000,000 VNĐ
- Người phụ thuộc: 2

Output:
- Tổng thu nhập: 30,000,000 VNĐ
- Bảo hiểm: 2,625,000 VNĐ (8.75%)
- Thuế TNCN: 1,043,750 VNĐ (3.48%)
- Lương thực lĩnh: 26,331,250 VNĐ
```

## 🚨 Troubleshooting

### ❌ Lỗi thường gặp

#### 1. "Python not found" / "pip not found"
```bash
# Windows: Tải và cài đặt Python từ python.org
# Đảm bảo chọn "Add Python to PATH"

# macOS:
brew install python3

# Linux:
sudo apt install python3 python3-pip

# Kiểm tra:
python --version
pip --version
```

#### 2. "Cannot connect to server" / "API không hoạt động"
```bash
# Kiểm tra Flask server có chạy không
python app.py

# Kiểm tra port 5000 có bị chiếm không
netstat -an | findstr :5000

# Thử port khác
python app.py --port 5001
```

#### 3. "Module not found" / "Import error"
```bash
# Cài đặt lại dependencies
pip install -r requirements.txt

# Hoặc cài đặt thủ công
pip install Flask Flask-CORS
```

#### 4. "CORS error" / Lỗi kết nối frontend-backend
- Đảm bảo Flask server đang chạy
- Kiểm tra URL trong `index.html` (dòng 542): `const API_BASE_URL = 'http://localhost:5000';`
- Thử tắt antivirus/firewall tạm thời

#### 5. Giao diện không hiển thị đúng
```bash
# Sử dụng HTTP server thay vì mở file trực tiếp
python -m http.server 3000

# Hoặc
npm install -g live-server
live-server --port=3000
```

### 🔧 Debug mode

#### Bật debug cho Flask
```python
# Trong app.py, dòng cuối:
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### Kiểm tra log
- Mở Developer Tools (F12) trong browser
- Xem tab Console để kiểm tra lỗi JavaScript
- Xem tab Network để kiểm tra API calls

### 📞 Hỗ trợ

#### Kiểm tra hệ thống
```bash
# Kiểm tra Python
python --version

# Kiểm tra pip
pip --version

# Kiểm tra Flask
python -c "import flask; print(flask.__version__)"

# Test API
curl http://localhost:5000/
```

#### Thông tin hệ thống
- **OS**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.7+
- **Browser**: Chrome 80+, Firefox 75+, Safari 13+, Edge 80+

## 🚀 Deployment

### Heroku
```bash
# Tạo Procfile
echo "web: python app.py" > Procfile

# Deploy
git init
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📈 Tính năng nâng cao

### Thêm tính năng mới
1. **Tính lương theo giờ**: Thêm endpoint `/hourly-salary`
2. **Xuất PDF**: Tích hợp jsPDF
3. **Lưu lịch sử**: Sử dụng localStorage
4. **So sánh lương**: Multiple salary comparison
5. **Tính lương net to gross**: Reverse calculation

### Tùy chỉnh giao diện
```css
/* Thay đổi màu chủ đạo trong index.html */
:root {
  --primary-color: #1e88e5;  /* Màu xanh BIDV */
  --secondary-color: #1565c0;
}
```

## 📄 License

MIT License - Tự do sử dụng cho mục đích cá nhân và thương mại.

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Tạo Pull Request

## 📞 Liên hệ

- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-repo/discussions)

---

⭐ **Nếu project hữu ích, hãy cho một star nhé!** ⭐