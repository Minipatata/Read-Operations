#Here is a file attached. You have to perform the following operations of 
# File Handling using Python
f=open("demo.txt","r")
print(f.read(20))
f.close()
f=open("demo.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
f=open("demo.txt","r")
for lines in f:
    print(lines)
f.close()