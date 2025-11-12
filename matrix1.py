# Max, Min, Sum of Matrix 
#3 3
#1 2 3
#10 20 30
#5 10 15

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here
max_list=[] 
min_list=[]
sum_list=[]
for i in num_list:
    max_list.append(max(i))
    min_list.append(min(i))
    sum_list.append(sum(i)) 
print(max(max_list))
print(min(min_list))
print(sum(sum_list))

##### 
def convert_str_to_int(val):
    new=[]
    for i in val:
        new.append(int(i))
    return new 

def get_total_sum(num_list):
    total=0 
    for list_a in num_list:
        total+=sum(list_a)
    return total 

num_list=[]
m,n=input().split() 
m,n=int(m),int(n)
for i in range(m):
    val=input().split() 
    int_list=convert_str_to_int(val)
    num_list.append(int_list)
print(max(max(num_list)))
print(min(min(num_list)))
total_sum=get_total_sum(num_list)
print(total_sum)

