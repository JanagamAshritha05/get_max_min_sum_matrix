# Row and Column with Maximun 
#3 3
#1 2 3
#10 20 30
#5 10 15

def convert_str_to_int(list_a):
    new=[]
    for i in list_a:
        i=int(i)
        new.append(i)
    return new 

m,n=input().split() 
m,n=int(m),int(n)
num_list=[]
for i in range(m):
    list_a=input().split() 
    int_list=convert_str_to_int(list_a)
    num_list.append(int_list)
    
max_list=[]    
for i in num_list:
    max_list.append(max(i))
    max_num=max(max_list)

for i in num_list:
    if max_num in i:
        max_list=i
        max_num_index=i.index(max_num)
 
col_list=[]       
for i in num_list:
    list_a=i[max_num_index]
    col_list.append(list_a)
print(max_list)
print(col_list)





