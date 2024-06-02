from flask import Flask, render_template, request, redirect, url_for, session

web = Flask(__name__)
web.secret_key = 'your_secret_key'  # Sử dụng secret key cho session

# Tạo một danh sách tài khoản mẫu (cố định, không cần cơ sở dữ liệu)
accounts = {'Ngọ Văn Trọng': '1234', 'TrongNV': '5678'}

@web.route('/')
def home():
    if 'username' in session:
        return "Xin chào, " + session['username'] + "đến với lớp học Python thầy Khánh! "+ " <a href='/logout'>Đăng xuất</a>"
    return "Trang chủ - Học Viện Công Nghệ Bưu Chính Viễn Thông- PTIT"+ " <a href='/login'>Đăng nhập</a>   <a href='/register'>Đăng kí</a>"

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in accounts and accounts[username] == password:
            session['username'] = username
            return "Đăng nhập thành công! <a href='/'>Trang chủ</a>"
        else:
            return "Sai tài khoản hoặc mật khẩu."

    if 'username' in session:
        return redirect(url_for('home'))
    
    return render_template('login.html')

@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        accounts[username] = password
        return "Đăng ký thành công! <a href='/login'>Đăng nhập</a>"

    if 'username' in session:
        return redirect(url_for('home'))

    return render_template('register.html')

@web.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    web.run(debug=True)
