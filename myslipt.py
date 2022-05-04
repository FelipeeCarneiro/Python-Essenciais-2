#
# Lab 2.3.1.18 O seu próprio split
#
# def mysplit(strng):

#     # return strng.split()
def mysplit(String):
    if String == '' or String == ' ':
        return [ ]
    lista = []
    palavra = ''
    em_palavra = not String[0].isspace()
    for i in String:
        if em_palavra:
            if not i.isspace():
                palavra += i
            else:
                lista.append(palavra)
                em_palavra = False
        else:
            if not i.isspace():
                em_palavra = True
                palavra = i
            else:
                pass
    if em_palavra:
        lista.append(palavra)
    return lista



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
