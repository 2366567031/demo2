class Initpage:

    # 成功用例的数据
    login_success_data = [
        {"username":"root","password":"root","expect":"Student Login"}
    ]

    # 失败用例的数据：msg_uname
    login_pwd_error_data = [
        {"username": "不再爱了", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]

    login1_teacher_data = [
        {"loginname": "jason", "password": "admin", "expect": "Teacher manager"}
    ]

    login1_teacher_x_data = [
        {"loginname": "abyz", "password": "abyz", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "ABYZ", "password": "ABYZ", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "0189", "password": "0189", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "！@#￥%&*", "password": "！@#￥%&*", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "Ay9中", "password": "ABYZ", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "Ay", "password": "Ay9中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "A9", "password": "A9", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "A中", "password": "A中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "y9", "password": "y9", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "y中", "password": "y中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "9中", "password": "9中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "Aa9", "password": "Aa9", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "Aa中", "password": "Aa中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "a9中", "password": "a9中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "a9中", "password": "a9中", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "123", "password": "123", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"loginname": "9中", "password": "ABYZ", "expect": "账户名错误或密码错误!别瞎弄!"},


    ]









