#write name to file
name=input("Enter your name\n")
fd = open("name.txt","w")
fd.write(name)
fd.close()
