import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="savitar12")
cursor=mydb.cursor()

cursor.execute("CREATE DATABASE if not exists customor")
        
cursor.execute("USE Customor")


cursor.execute("CREATE TABLE if not exists stockinfo(productname VARCHAR(20),stock int(20))")

str1="insert into stockinfo values('BED',100),('SOFA',100),('CHAIR',100),('BOOKSHELF',100),('DRESSING TABLE',100),('TABLE',100),('CUPBOARD',100),('SHOWCASE',100),('LAMP',100),('SHOERACK',100),('PHONE',100),('FRIDGE',100),('LAPTOP',100),('WASHING MACHINE',100),('HEATER',100),('SPEAKER',100),('TV',100),('AC',100),('GEYSER',100),('IRON',100),('BELT',100),('CARPET',100),('HAIRDRYER',100),('JEANS',100),('KURTI',100),('PERFUME',100),('SUNGLASSES',100),('SAREE',100),('SHIRT',100),('WATCH',100)"
cursor.execute(str1)
mydb.commit()
