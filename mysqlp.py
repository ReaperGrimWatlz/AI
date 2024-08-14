import mysql.connector as cnct
cont=cnct.connect(host="localhost",user="Anyone",passwd="ABC@123",database="test")
if mycon.is_connected():
  print('Successfully Conected')
