import datetime
filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
lst=["content1.txt","content2.txt","content3.txt"]
f=open(filename+".txt","a")
for i in lst:
	t=open(i,"r")
	temp=t.read()
	f.write(temp)
	t.close()
