from login import login
from read import readname
from write import write
print("请输入用户名,并用回车键结束:")
name = input()
print("请输入密码，并用回车键结束：")
password = input()

listname = readname()
i = login(name,password,listname)
		
if i>0:
	print("登陆成功")
elif  i<0:
	print("密码错误")
	print("重新输入密码")
	newpassword = input()
	
else:
	print("您是否需要注册，输入Y继续，输入N，退出登陆")
	n1 = input()
	if n1.upper() =="Y":
		write(name,password)
		print("用户注册成功")
	else:
		exit()