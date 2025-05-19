import random

password = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','-']

print("Welcome to PyPassword generator!")

num_letters = int(input("How many letters would you like in your password\n"))
num_numbers = int(input("How many numbers would you like in the password\n"))
num_symbols = int(input("How many symbols would you like in the password\n"))



for i in range(0, num_letters):
    password = password + list((random.choice(letters)))
for j in range(0, num_numbers):
    password = password + list((random.choice(numbers)))
for k in range(0, num_numbers):
    password = password + list((random.choice(symbols)))

new_password = random.shuffle(password)
#print(password)
print (''.join(password))