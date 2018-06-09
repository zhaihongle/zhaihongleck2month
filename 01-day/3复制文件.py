d = open("xx珍藏.txt","r")
countent = d.read()
d.close()
f = open ("复制珍藏.txt","w")
f.write(countent)
f.close()

