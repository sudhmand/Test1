fl = open('test','r')
ln = fl.readline()
names = ln.split(":")
lastname = names[1]
print lastname.rstrip()
fl.close()
