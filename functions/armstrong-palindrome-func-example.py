def reverse(number):
    temp=number
    sum=0
    while temp>0:
        digit = temp%10
        sum=sum*10 + digit
        temp = temp // 10
    return sum

def armstrong(number):
    temp=number
    order=len(str(temp))
    sum=0
    while temp>0:
        digit = temp%10
        sum=sum + digit**order
        temp = temp // 10
    return sum


try:
    number = (int(input('Enter the number:')))

    if reverse(number) == number:
        print(str(number)+' is a Palindrome number')

    else:
        print(str(number)+' is not a Palindrome number')

    if armstrong(number) == number:
        print(str(number)+' is an Armstrong number')

    else:
        print(str(number)+' is not an Armstrong number')

except ValueError:
    print('You entered a non-numeric value')