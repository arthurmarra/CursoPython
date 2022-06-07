num = [[],[]]

for valores in range(0,7):
    resp = int(input(f'Digite o {valores+1}º valor:'))
    if resp % 2 ==0:
        num[0].append(resp)
    elif resp %2 == 1:
        num[1].append(resp)

 #   if num[valores] %2 ==0:
 #       pares.append(num[valores])
 #   elif num[valores]%2 == 1:
 #     impares.append(num[valores])

num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')