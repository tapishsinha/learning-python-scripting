# This program prints hello and asks for my first name

print('Hello World!')

print('What is your first name: ') #ask the name
myName = input()

print('Nice to meet you '+ myName)
print ('The length of your name is ')
print(len(myName))

print('How old are you?') #ask their age
myAge = input()

print('You will be '+ (str(int(myAge)+1)) + ' years old in 1 year')
