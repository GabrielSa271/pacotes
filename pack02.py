try:
    value = int(input('Entre com um número: '))
    print('O valor: ', value, 'um dividido por valor é:' , 1/value)        
except ValueError:
    print('Erro. Verifique o valor fornecido.')
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero.')