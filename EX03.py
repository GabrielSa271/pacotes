while True:
    try:
        numero = int(input('Entre com um número: '))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou Não é possivel dividir por zero")
    except:
        print("Desculpe, algo errado aconteceu...")