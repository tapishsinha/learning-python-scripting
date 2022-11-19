print('Enter the value:')
input_num = int(input())
flag_num = input_num
sum = 0
while flag_num > 0:
    last = flag_num % 10
    sum = sum + (last **  3)
    flag_num = flag_num // 10
 
if sum == input_num:
    print(str(input_num)+' is an Armstrong Number')

else:
    print(str(input_num)+' is not an Armstrong Number')