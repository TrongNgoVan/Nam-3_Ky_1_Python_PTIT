from flask import Flask, render_template, request, redirect, url_for
import time;

app = Flask(__name__, static_url_path='/static')

# Trang chủ
@app.route('/')
def home():
    
    return render_template('index.html')

# Trang đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Kiểm tra xem tài khoản đã tồn tại hay chưa
        if not is_username_taken(username):
            save_user(username, password, email)
            return redirect(url_for('login'))
        else:
            return "<h1>Account already registered</h1>"
    
    return render_template('register.html')

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if is_valid_login(username, password):
            return "<h1>Welcome to PTIT !!!</h1>"
        else:
            return "<h1>Login Failed!</h1>"
    
    return render_template('login.html')


# Kiểm tra xem tài khoản đã tồn tại hay chưa
def is_username_taken(username):
    with open(r"C:\Lap trinh web voi Python\DataBase.txt", 'r') as file:
        for line in file:
            stored_username = line.split(';')[0]
            if username == stored_username:
                return True
    return False

# Lưu thông tin người dùng vào DataBase.txt
def save_user(username, password, email):
    with open('DataBase.txt', 'a') as file:
        file.write(f"{username};{password};{email}\n")

# Kiểm tra xem thông tin đăng nhập có hợp lệ hay không
def is_valid_login(username, password):
    try:
        with open(r"C:\Lap trinh web voi Python\DataBase.txt", 'r') as file:
            for line in file:
                stored_username, stored_password, _ = line.strip().split(';')
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return False


def save_feedback(username, feedback_text, localtime):
    with open('feedback.txt', 'a') as file:
        file.write(f"{username};{feedback_text};{localtime}\n")

if __name__ == '__main__':
    app.run(debug=True)