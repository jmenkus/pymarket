import configparser,os

c = configparser.ConfigParser()
c.read("pymarket.conf")

for i in c.items("Network Options"):
	print(i)
	print(type(i[1]))

#if os.exists("orderbook.csv"):
#	pass

