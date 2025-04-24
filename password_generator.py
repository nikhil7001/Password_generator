import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['!','@','#','$','%','&','*','(',')','+']
print("Welcome to Password Generator!\n")
l=int(input("How many letters you want in password?\n"))
n=int(input("How many numbers you want in password?\n"))
s=int(input("How many symbols you want in password?\n"))
p_list=[]
for i in range(1,l+1):
    c=random.choice(letters)
    p_list+=c
for i in range(1,n+1):
    c=random.choice(num)
    p_list+=c
for i in range(1,s+1):
    c=random.choice(sym)
    p_list+=c
random.shuffle(p_list)
p=""
for i in p_list:
    p+=i
print(p)   










