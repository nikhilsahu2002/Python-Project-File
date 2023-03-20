# x = {'name':"nikhil",'Class':"Mca"}

dic={
    'name':'Nikhil',
    'age':21,
    'class':"MCA",
    1:'one',
    'lang': ['python','c','java']
}

# print(dic['name'])
# print(dic[1])

# dic=tuple(dic)

# print(dic)

# dic = list(dic)
# print(dic)

x=dict(name='nikhil',Class='MCA')
x.update(age=21)
x.pop('name')

print(x)

#write a priogram in python create a dic for persional info such that name age city cours university and grade 

new_dic=dict(name = 'nikhil',age=21,course='MCA',University='united University',city='Allahabad',grade='A+')

print(new_dic)

old_dic={
    'name':'nikhil',
    'age':21,
    'cours':'MCA',
    'City':'Allahabad',
    'grade':'A+',
    'University':'united University'

}

print(old_dic)

#access item in dict
# 1. using key

print(new_dic['name'])

print(new_dic.get('city')) # using get method to retrive data

#keys method 
# return a list of all the keys in the dict 

print(new_dic.keys())
print(new_dic.values())#return list of all the values in the dic
print(new_dic.items()) #returns all the items as tuple of the dic in the list 
print()
for i in new_dic.items():
    print(i)

for key,values in new_dic.items():
    print(key,"=",values)