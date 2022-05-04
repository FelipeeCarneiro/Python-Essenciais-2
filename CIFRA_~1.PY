# plano : tornar a crifra César mais difícil (melhorar)

#pede ao utilizar uma linha de texto para encriptar
text = 'The die is cast'#input("Enter your message: ")

#MELHORADO deve forçar o utilizador a inserir um valor de deslocamento válido (1..25)
while True:

    #pede ao utilizador um valor de deslocamento
    passo = 25 #input("Enter a interval: ")

    #como a conversão de string-int pode levantar uma exceção, o melhor é continuar com a proteção do bloco try-except;
    try:

        # e tentar converter em número int; se funcionar...;
        passo = int(passo)

        # ... verifica se número inteiro está entre 1 e 25.
        if passo >= 1 and passo <= 25:
            break

        # caso não funcione, imprimir uma mensagem de diagnóstico mostrando ao utilizador o motivo da falha
        else:
            print(passo,"Is not a numver valid " + " Enter a valid interval: ")
    except:
            print(passo, "is not a number valid.")

#preparar uma string para uma mensagem encriptada (vazia por agora)
cipher = ''

#iniciar a iteração através da mensagem;
for char in text:

    #MELHORADO...se não for alfabético deixa-lo intocável.
    if not char.isalpha():
        cipher += char

    #MELHORADO... se for alfabético, verificar...
    if char.isalpha():

        #se for maiúscula...
        # if char.upper():
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):

            #MELHORADO!! (...)incrementá-lo de acordo com a VARIÁVEL "passo";
            code = ord(char) + passo

            #se o código resultante tiver “deixado” o alfabeto latino (se for maior do que o código Z)...
            if code > ord('Z'):
                #...alterá-lo para o código A;
                code = ord('A')
            #anexar o caratere recebido ao fim da mensagem encriptada
            cipher += chr(code)

        #MELHORADO letras minúsculas permanecerão minúsculas
        # if char.islower():
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            code = ord(char) + passo
            if code > ord('z'):
                code = ord('a')
            cipher += chr(code)

#imprime o texto codificado.
print(cipher)
