import os, time

def NdV(data='08101990'):
    while True:
        if os.system == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print("The Digit of Life")
        time.sleep(2)

        # insira um hastag na frente da linha abaixo se a função "test()" estiver descomentada. Ou seja, comente abaixo se não, não vai funcionar o test
        data = input('Informe o seu aniversário, apenas o números.\nExemplo: para um de janeiro de 2017: 01012017.\nSeu aniversário: ')

        if len (data) != 8 or not data.isdigit():                                           #.isdigit() só funfa com string
            print('[error]\nFormato inválido da data.\nTente AAAAMMDD, ou AAAADDMM, ou MMDDAAAA.\n\
    A ordem dos dígitos não importa na verdade')
            time.sleep(5)
            os.system('clear')
        else:
            while len(data) > 1:
                soma = 0
                for cada_num in data:
                    soma += int(cada_num)
                    print(f'calculando {data}...')
                    data = str(soma)
                    time.sleep(.5)
                    os.system('clear')
            print("Dígito da Vida é",data)
            time.sleep(2)
            return data

def test():
    pai = NdV('05051959')
    mãe = NdV('23021959')
    irmã = NdV('20011992')
    os.system('clear')
    print(f'Dígito da Vida de pai {pai} mãe {mãe} irmã {irmã}.')


# test()    # descomente parar exemplificar
NdV()
