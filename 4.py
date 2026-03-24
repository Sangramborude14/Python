a = int(input("enter the number"))

for i in range(1, a-1):
    if a % i == 0 :
        print('the number is not prime ')
        break
    else:
        print('the number is prime')
       