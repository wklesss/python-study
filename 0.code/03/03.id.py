"""
用户身份验证

version：0.1
Author: 王凯
"""
username = input('请输入用户名')
password = input('请输入口令')
# 用户名是admin且密码是123456则身份验证成功，否则失败
if username == 'admin' and password =='123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')
    