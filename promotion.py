inicio = input('Bem vindo a mercearia, selecione quais produtos você deseja comprar (1: Água / 2: Açúcar / 3: Café): ')

if inicio == '1':
    quant = int(input('Quantas águas você deseja comprar? '))
    parcial = 2.5 * quant
    if quant >= 10:
        total = parcial - (parcial * 0.1)
        print(f'PARABÉNS!!! Você recebeu um desconto de 10% e está levando {quant} água(s) pelo valor de R${total}')
    else:
        print(f'Você está levando {quant} água(s) pelo valor de R${parcial}')
elif inicio == '2':
    quant = int(input('Quantos açúcar você deseja comprar? '))
    parcial = 5.0 * quant
    if quant >= 10:
        total = parcial - (parcial * 0.1)
        print(f'PARABÉNS!!! Você recebeu um desconto de 10% e está levando {quant} açúcar pelo valor de R${total}')
    else:
        print(f'Você está levando {quant} açúcar pelo valor de R${parcial}')
elif inicio == '3':
    quant = int(input('Quantos cafés você deseja comprar? '))
    parcial = 10.0 * quant
    if quant >= 10:
        total = parcial - (parcial * 0.1)
        print(f'PARABÉNS!!! Você recebeu um desconto de 10% e está levando {quant} açúcar pelo valor de R${total}')
    else:
        print(f'Você está levando {quant} açúcar pelo valor de R${parcial}')