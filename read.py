
def readname():
	r = open("D:/python/users.txt","r")
	d = []
	try:
		for line in r.readlines():
			name = line.split('\t')
			name[1] = name[1].strip()
			d.append(name)
	finally:
		if r:
			r.close()
	25d.pop(0)
	return d






