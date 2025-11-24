import os
import datetime
import math

# Cấu hình tiêu đề trang web
PAGE_TITLE = "Index of /KODI/F/"

def get_size_format(b, factor=1024, suffix="B"):
    """Chuyển đổi byte sang KB, MB, GB"""
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f} {unit}{suffix}"
        b /= factor
    return f"{b:.2f} Y{suffix}"

def get_icon(filename):
    """Chọn icon dựa trên đuôi file"""
    ext = filename.split('.')[-1].lower()
    if ext in ['zip', 'rar', '7z']:
        return "📦" # Icon hộp
    elif ext in ['apk']:
        return "🤖" # Icon Android
    elif ext in ['jpg', 'png', 'jpeg', 'gif']:
        return "🖼️" # Icon ảnh
    elif ext in ['txt', 'xml', 'json']:
        return "📝" # Icon văn bản
    else:
        return "📄" # Icon file chung

def generate_index():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # Các file muốn bỏ qua, không hiện lên web
    ignore_files = ['index.html', 'gen_index.py', '.gitignore', '.DS_Store']
    
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{PAGE_TITLE}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; color: #333; }}
        .container {{ max-width: 900px; margin: 0 auto; background: white; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); border-radius: 8px; }}
        h1 {{ font-size: 24px; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 20px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ text-align: left; padding: 12px; border-bottom: 1px solid #eee; }}
        th {{ background-color: #f8f9fa; font-weight: 600; color: #555; }}
        tr:hover {{ background-color: #f1f1f1; }}
        a {{ text-decoration: none; color: #0366d6; font-weight: 500; display: flex; align-items: center; }}
        a:hover {{ text-decoration: underline; }}
        .icon {{ margin-right: 10px; min-width: 25px; text-align: center; }}
        .size {{ color: #666; font-size: 0.9em; font-family: monospace; }}
        .date {{ color: #888; font-size: 0.9em; }}
        .footer {{ margin-top: 20px; font-size: 12px; color: #999; text-align: center; }}
    </style>
</head>
<body>
<div class="container">
    <h1>{PAGE_TITLE}</h1>
    <table>
        <thead>
            <tr>
                <th style="width: 55%">Name</th>
                <th style="width: 30%">Last Modified</th>
                <th style="width: 15%">Size</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><a href="../"><span class="icon">📂</span> [Parent Directory]</a></td>
                <td>-</td>
                <td>-</td>
            </tr>
    """

    # Sắp xếp file theo tên
    files.sort()

    for filename in files:
        if filename in ignore_files or filename.startswith('.'):
            continue
            
        # Lấy thông tin file
        filepath = os.path.join('.', filename)
        size = get_size_format(os.path.getsize(filepath))
        mtime = os.path.getmtime(filepath)
        date_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
        icon = get_icon(filename)

        html_content += f"""
            <tr>
                <td><a href="{filename}"><span class="icon">{icon}</span> {filename}</a></td>
                <td class="date">{date_str}</td>
                <td class="size">{size}</td>
            </tr>
        """

    html_content += """
        </tbody>
    </table>
    <div class="footer">Generated automatically by Python</div>
</div>
</body>
</html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ Đã tạo file index.html thành công!")

if __name__ == "__main__":
    generate_index()