#Assigning elements to lists
list1=['apple','mango','grapes','pineapple']
list2=[1,78, True, 'Riya','Eat']
print('List 1:',list1)
print('List 2:',list2)
list1.append('guava')
list1[2]='pears'
print('Updated List 1:',list1)
list2.append(15647)
list2[1]=[1,2,3,4]
print('Updated List 2:',list2)
print('\n')

#Accessing elements from a tuple
tuple1=('a','b','c','d','e','f',[8,6,4],'g','h')
print('Tuple 1 is:',tuple1)
print(tuple1[4])
print(tuple1[6][1])
tuple2=(20,40,678,983,675)
print('Tuple 2 is:',tuple2)
print(tuple2[-1])
print(tuple2[-4])
tuple3=('france','india','usa','italy','russia')
print('Tuple 3 is:',tuple3)
print(tuple3[2:4])
print('\n')

#Deleting different dictionary elements
dict={'Riya':18,'Dilip':34,'Sahana':21,'Priya':28,'Ansh':24}
print('The dictionary is:',dict)
del dict['Sahana']
print('After deleting an element:',dict)
print(dict.pop('Ansh'))
print('The updated dictionary is:',dict)
dict.clear()
print('Empty dictionary:',dict)
