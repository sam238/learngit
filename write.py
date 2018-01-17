#w = open("d:/python/write.txt",'w')
#w.write("hello world")
#w.close()
def write(name,password):
	with open("d:/python/users.txt","a") as w:
		#name1 = "\n%s\t%s" % (name,password)
		name1 = "\n{0}\t{1}".format(name,password)
		w.write(name1)

