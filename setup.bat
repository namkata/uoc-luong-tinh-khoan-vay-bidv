@echo off
echo ========================================
echo    BIDV Salary Calculator Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python không được tìm thấy!
    echo 📥 Vui lòng tải và cài đặt Python từ: https://python.org
    echo ⚠️  Nhớ chọn "Add Python to PATH" khi cài đặt
    echo.
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt
python --version

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip không được tìm thấy!
    echo 📥 Vui lòng cài đặt pip
    pause
    exit /b 1
)

echo ✅ pip đã sẵn sàng
echo.

REM Install dependencies
echo 📦 Đang cài đặt dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Lỗi khi cài đặt dependencies!
    echo 🔧 Thử chạy: pip install Flask Flask-CORS
    pause
    exit /b 1
)

echo ✅ Dependencies đã được cài đặt thành công!
echo.

REM Create start script
echo 🚀 Tạo script khởi động...
echo @echo off > start.bat
echo echo ======================================== >> start.bat
echo echo    BIDV Salary Calculator Server >> start.bat
echo echo ======================================== >> start.bat
echo echo. >> start.bat
echo echo 🌐 Server đang khởi động tại: http://localhost:5000 >> start.bat
echo echo 📱 Mở index.html trong browser để sử dụng >> start.bat
echo echo. >> start.bat
echo echo ⏹️  Nhấn Ctrl+C để dừng server >> start.bat
echo echo. >> start.bat
echo python app.py >> start.bat

echo ✅ Script khởi động đã được tạo!
echo.

echo 🎉 Setup hoàn tất!
echo.
echo 📋 Các bước tiếp theo:
echo    1. Chạy 'start.bat' để khởi động server
echo    2. Mở 'index.html' trong browser
echo    3. Bắt đầu tính lương!
echo.
echo 💡 Hoặc chạy thủ công:
echo    python app.py
echo.

pause