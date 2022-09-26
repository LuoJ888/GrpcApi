name = input()
try:
    pwd = int(input())
except:
    print('密码类型只能是数字')

    def checkNameAndPwd():
        if name == '':
            print('用户名不能为空')
        if 2 <= len(name) < 8:
            pass
        else:
            print('用户名长度仅可在2-7之间')
        # if type(pwd) is not int:
        #     print('密码类型只能是数字')
        if 6 <= len(str(pwd)) < 10:
            pass
        else:
            print('密码长度仅可在6-9之间')
        try:
            if pwd == '':
                print('密码不能为空')
        except Exception as e1:
            print(f'{e1}')


    checkNameAndPwd()
