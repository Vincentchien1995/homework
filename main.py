def is_prime(N):
    if N <=1:
        return False
    for i in range(2,N):
        if N%i == 0:
            return False
    return True

N =int(input("enter the value of N"))
def n_prime(N):
    num = 2
    count =0
    while count<N:
        if is_prime(num):
            print(num)
            count += 1
        num +=1
print(n_prime(N))





def simple_search(tab, item):
    i = 0
    while i < len(tab):
        if tab[i] == item:
        return i
        i += 1
    return -1


nitems = int(input("Enter the number of items: "))
items = []
i = 0
while i < nitems:
    item = float(input("Enter the item: "))
    items.append(item)
    i += 1

print(simple_search(items,4))