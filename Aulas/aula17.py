num = [2, 5, 9, 1]
num[2]= 3
#num[4]= 7
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(f'Essa lista tem {len(num)} elementos')
print(num)