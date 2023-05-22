'''
relative path and absalute path 
open() : reading and writeing  : fp = open (filename ,mode of accesss) 
read()
write/append()
close()

# '''

fp = open("E:/UU/test.txt","r")

# x=fp.read()
# x=fp.read(10)
x=fp.readline()
y=fp.readline()
z= fp.readline()
# fp.mode tell's a file mode
#  close method of a file object flushes any unreaden information and close the file object 
    # syntax : file_object.close()
fp.close()
# print(fp.closed) boolen 
# print(line)
# print(x)
# print(y)
# print(z)
# write() writes a string into a file 
        # fileonject.erite(string)

line = (input("Enter The String"))
fp = open("E:/UU/test.txt","w")

x="this is new string"
fp.write(line)
# fp.read()
fp.close()
# append 

fp = open("E:/UU/test.txt","a")
x="this is new string"
fp.write(x)
fp.close()

# file posstion 
# tell() - tells the current position of the file pointer 
# seek() - is used to change position of the file pointer 
    # fp.seek(offset,from_what) - offset tells number of postions to move forward ,from_what - it definies refrecne point or point of refrence it acceptes 3 value 0,1,2 0-set the 
    # refrence point at the beging of the point set the refrecne point at the corent potion 2:- set the refrece point at end of the file

fp = open("E:/UU/test.txt","r")
fp.read(5)
print(fp.tell())
fp.seek(0,0)
print(fp.tell())
fp.close() 

# renaming and delecting a file
# pyhton os moduls provides methods that helps you to performe file processing opertions such as rename delete mkdir chdir 
import os 
# #  remdir() :- Delete a dirctory 
# os.rmdir("E:/UU/uumca")

# print(os.getcwd())
# # csdir() :- change the current directory
# # os.change(newdirctory) 
# os.chdir("E:/UU")

# os.mkdir("E:/UU/uumca")
# # os.rename("E:/UU/test.txt","E:/UU/test1.txt") 
# os.remove("E:/UU/tt.txt")

# getcwd() :get current working directory

# def read_links_file(file):
# 	with open(file, 'rb') as f:
# 		links = f.readlines()
# 	return links

# read_links_file("E:/UU/test.txt")