# 🚀 HƯỚNG DẪN KHỞI ĐỘNG NHANH

## ⚡ Bắt đầu ngay trong 5 phút!

### 📋 Bước 1: Cài đặt Python (nếu chưa có)

#### Windows:
1. 🌐 Truy cập: https://python.org/downloads/
2. 📥 Tải **Python 3.9+** (phiên bản mới nhất)
3. 🔧 Chạy file cài đặt
4. ⚠️ **QUAN TRỌNG**: Tích vào ☑️ **"Add Python to PATH"**
5. ✅ Click "Install Now"

#### Kiểm tra cài đặt:
```bash
# Mở Command Prompt hoặc PowerShell
python --version
pip --version
```

### 📦 Bước 2: Cài đặt dependencies

```bash
# Trong thư mục project
pip install -r requirements.txt
```

### 🚀 Bước 3: Chạy ứng dụng

#### Cách 1: Sử dụng script tự động
```bash
# Chạy setup (chỉ lần đầu)
.\setup.bat

# Khởi động server
.\start.bat
```

#### Cách 2: Chạy thủ công
```bash
# Khởi động Flask API
python app.py

# Mở browser và truy cập:
# file:///path/to/index.html
# hoặc http://localhost:3000 (nếu dùng HTTP server)
```

### 🌐 Bước 4: Mở giao diện

#### Cách 1: Mở file trực tiếp
- Double-click vào `index.html`
- Hoặc kéo thả vào browser

#### Cách 2: Sử dụng HTTP server (khuyến nghị)
```bash
# Terminal mới
python -m http.server 3000

# Truy cập: http://localhost:3000
```

## 🎯 Sử dụng nhanh

### Tab "Ước tính lương" 
1. Nhập lương cơ bản: `15000000`
2. Click **"Tính lương ngay"**
3. Xem kết quả ngay lập tức!

### Tab "Tính lương chi tiết"
1. Lương cơ bản: `25000000`
2. Phụ cấp: `5000000` 
3. Người phụ thuộc: `2`
4. Click **"Tính lương ngay"**
5. Xem breakdown chi tiết!

## 🚨 Khắc phục sự cố nhanh

### ❌ "Python not found"
```bash
# Cài đặt lại Python với "Add to PATH"
# Hoặc thêm Python vào PATH thủ công
```

### ❌ "Cannot connect to server"
```bash
# Kiểm tra Flask có chạy không
python app.py

# Kiểm tra URL trong index.html
# Dòng 542: const API_BASE_URL = 'http://localhost:5000';
```

### ❌ "Module not found"
```bash
pip install Flask Flask-CORS
```

## 📱 Demo nhanh

### Input mẫu:
- **Lương cơ bản**: 20,000,000 VNĐ
- **Phụ cấp**: 3,000,000 VNĐ  
- **Người phụ thuộc**: 1

### Output mong đợi:
- **Tổng thu nhập**: 23,000,000 VNĐ
- **Bảo hiểm**: ~2,415,000 VNĐ
- **Thuế TNCN**: ~450,000 VNĐ
- **Lương thực lĩnh**: ~20,135,000 VNĐ

## 🎉 Hoàn thành!

Bây giờ bạn có thể:
- ✅ Tính lương nhanh chóng
- ✅ Xem breakdown chi tiết
- ✅ Tính cho nhiều trường hợp khác nhau
- ✅ Sử dụng giao diện đẹp như BIDV

## 📞 Cần hỗ trợ?

1. 📖 Đọc `README.md` để biết chi tiết
2. 🔍 Kiểm tra phần Troubleshooting
3. 🐛 Báo lỗi qua GitHub Issues

---

⚡ **Chỉ 5 phút để có công cụ tính lương chuyên nghiệp!** ⚡