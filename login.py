def login(name,password,listname):
	i = 0
	for index in range(len(listname)):
		if listname[index][0] == name.lower():
			if listname[index][1] == password:
				i = i + 1
				break
			else:
				i = i-1
		else:
			continue
	return i