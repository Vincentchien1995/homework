def is_prime(N):  #Define is_prime function
    if N <=1:
        return False
    for i in range(2,N):
        if N%i == 0:   #if remainder equal to 0 then it's not a prime_number
            return False
    return True

N =int(input("enter the value of N"))
def n_prime(N):
    num = 2  #prime_number start from 2
    count =0 #count how many prime_number
    while count<N:
        if is_prime(num):
            print(num)
            count += 1
        num +=1
print(n_prime(N))





