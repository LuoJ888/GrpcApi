class login:
    def __init__(self):
        self.name = input()
        self.pwd = input()

    def checkNameAndPwd(self):
        if self.name is None:
            print('用户名不能为空')
        if self.pwd is None:
            print('密码不能为空')
        if len(self.name) < 6:
            print('用户名小于6位')
        if len(self.pwd) < 6:
            print('密码小于6位')


login.checkNameAndPwd()
