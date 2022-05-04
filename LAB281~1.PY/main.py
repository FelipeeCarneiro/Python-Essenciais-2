def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            valor = int(input(prompt))
            ok = True
        except ValueError:
            print('Erro: input errado')
        if ok:
            ok = valor >= min and valor <= max
        if not ok:
            print('Erro: o valor não é permitido entre(' + str(min) + '..' + str(max) + ')')
    return valor;

# https://edube.org/learn/python-essentials-2-prt/ler-ints-em-seguranca

v = read_int("Enter a number from -10 to 10: ", -10, 10)    # <== Argumentos

print("The number is:", v)
