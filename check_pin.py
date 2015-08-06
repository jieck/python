#检查pin值和用户名
database = [['jack','12'],['jie','14'],['wo','23']]
user = input("you user name : ")
pin = input('input your pin : ')
if [user,pin] in database :
	print('Access granted')