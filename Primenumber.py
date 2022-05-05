#To find wether the given number is prime number or not

n = 407

if n > 1:
    for i in range(2, int(n/2)+1):
        if (n%i) == 0:
            print("Number is not a prime number")
            print(f"{i} times {n//i} is {n}")
            break
    else:
        print("Is a prime number")
else:
    print("Is not a prime number")

#To print the prime number for given range

def prime(x,y):
    prime_list =[]
    for i in range (x,y):
        if  i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

l = prime(900, 1000)
print(l)
