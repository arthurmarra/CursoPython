def maior(* num):
    nm = cont = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        if cont == 0:
            nm = num[cont]
        else:
            if nm<num[cont]:
                nm = num[cont]
        print(f'{v} ', end='')
        cont +=1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {nm}.')
    print('-=' * 30)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
