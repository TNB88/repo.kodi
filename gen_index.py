import os

# --- CẤU HÌNH ---
# Các thư mục không muốn liệt kê
EXCLUDED_DIRS = {'.git', '.github', '.idea', '__pycache__', 'venv', '.vscode'}
# Các file không muốn liệt kê
EXCLUDED_FILES = {'index.html', 'gen_index.py', 'chay-cai-nay.bat', '.gitignore', '.DS_Store', 'README.md', 'CNAME'}

def generate_simple_html(path):
    try:
        # Lấy danh sách file và thư mục
        items = os.listdir(path)
        dirs = []
        files = []

        for item in items:
            # Bỏ qua các file/folder bị loại trừ
            if item in EXCLUDED_FILES or item in EXCLUDED_DIRS: continue
            
            full_path = os.path.join(path, item)
            
            if os.path.isdir(full_path):
                dirs.append(item)
            else:
                files.append(item)
        
        # Sắp xếp theo tên
        dirs.sort()
        files.sort()

        # --- TẠO NỘI DUNG HTML ---
        # Dùng format "Apache Directory Listing" chuẩn nhất cho Kodi
        # Không CSS, không Table, dùng thẻ <pre> để xuống dòng tự nhiên
        
        lines = []
        lines.append('<!DOCTYPE html>')
        lines.append('<html>')
        lines.append('<head><title>Index</title></head>')
        lines.append('<body>')
        
        # Tiêu đề cho biết đang ở đâu (dành cho người xem trình duyệt)
        display_path = path if path != '.' else 'Root'
        lines.append(f'<h1>Index of {display_path}</h1>')
        
        lines.append('<hr>')
        lines.append('<pre>')

        # Link quay lại thư mục cha (trừ thư mục gốc)
        if path != '.':
            lines.append('<a href="../">../</a>')

        # Liệt kê Thư mục (thêm dấu / vào cuối để Kodi hiểu là folder)
        for d in dirs:
            lines.append(f'<a href="{d}/">{d}/</a>')

        # Liệt kê File
        for f in files:
            lines.append(f'<a href="{f}">{f}</a>')

        lines.append('</pre>')
        lines.append('<hr>')
        lines.append('</body>')
        lines.append('</html>')

        # Ghi file index.html
        with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
            f.write('\n'.join(lines))
            
        print(f"Đã tạo index.html cho: {path}")
            
    except Exception as e:
        print(f"Lỗi tại {path}: {e}")

# --- CHẠY QUÉT ---
print("--- Đang quét và tạo Index kiểu cổ điển ---")

# os.walk giúp đi sâu vào tất cả các thư mục con
for root, dirs, files in os.walk('.', topdown=True):
    # Loại bỏ các thư mục hệ thống khỏi danh sách duyệt
    dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
    
    generate_simple_html(root)

print("\n✅ HOÀN TẤT! Index chuẩn Apache đã được tạo.")