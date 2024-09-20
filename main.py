# from Grav import Estado  #corrigir

# organiza o arquivo de entrada em arquivos para estados, inicio, fins, e transiC'C5es
with open(
    "entrada.txt", "r"
) as entrada:  # abre o arquivo de texto recebido pelo professor para leitura
    with open(
        "estados.txt", "w"
    ) as estados:  # abre o arquivo predefinido para armazenar os estados (1B* linha)
        line = entrada.readline()
        estados.writelines(line)
    with open(
        "estIni.txt", "w"
    ) as ini:  # abre o arquivo predefinido para armazenar os estados iniciais (2B* linha)
        line = entrada.readline()
        ini.writelines(line)
    with open(
        "estFin.txt", "w"
    ) as fim:  # abre o arquivo predefinido para armazenar os estados finais (3B* linha)
        line = entrada.readline()
        fim.writelines(line)
    with open(
        "transi.txt", "w"
    ) as trans:  # abre o arquivo predefinido para armazenar as transiC'C5es (4B* linha em diante)
        transicoes = entrada.readlines()
        trans.writelines(transicoes)
    # print("{}".format(Lines))


# Seleciona as variC!veis no arquivo q define os estados possiveis
with open("estados.txt", "r") as estados:
    todosEsts = []
    contador = 0
    line = estados.readline()
    ests1 = line.split("\n")
    ests = ests1[0].split(" ")
    limite = (
        len(line) - 1
    ) / 2  # NC#o sei pq, mas tem que subtrair 1 e dividir por dois (mesmo o tamanho sendo 4)
    while contador < limite:
        todosEsts.append(ests[contador])
        print("Estado {}".format(ests[contador]))
        # Estado(ests[contador],False,False)    #Cria um estado que nC#o C) considerado como um atual, que nC#o consta como um estado final
        contador = contador + 1


Atual = []  # armazena os estados iniciais de cada transiC'C#o
Vari = []  # armazena as variaveis de cada transiC'C#o
Goto = []  # armazena os estados seguintes de cada transiC'C#o
num1 = 0
num2 = 1
num3 = 2
# Variaveis assossiadas a transiC'C5es
with open("transi.txt", "r") as trans:
    # contador = 0    #desnecessC!rio

    for line in transicoes:
        line = trans.readline()
        tra1 = line.split("\n")
        tra = tra1[0].split(" ")
        Atual.append(tra[num1])
        Vari.append(tra[num2])
        Goto.append(tra[num3])  # corrigir para prarar de guardar "\n" junto do numero
        print("{} {} {}".format(tra[num1], tra[num2], tra[num3]))
        # contador = contador + 1    #desnecessC!rio

ativos = []
with open(
    "estIni.txt", "r"
) as inicio:  # Seleciona a C:nica variC!vel no arquivo q define o estado inicial
    inicio.seek(0)
    inicial = []
    estIni1 = inicio.readline()
    estIni2 = estIni1.split("\n")
    estIni = estIni2[0]
    inicial.append(estIni)
    ativos.append(estIni)
    print("Inicio {}".format(estIni))
    # Estado(estIni,True,False)  #Cria um estado chamado "1" que C) considerado como um atual, que nC#o consta como um estado final


with open(
    "estFin.txt", "r"
) as final:  # Seleciona as variC!veis no arquivo q define os estados finais
    contador = 0
    finais = []
    line = final.readline()
    estFin1 = line.split("\n")
    estFin = estFin1[0].split(" ")
    limite = (
        len(line) - 1
    ) / 2  # NC#o sei pq, mas tem que subtrair 1 e dividir por dois (mesmo o tamanho sendo 4)
    while contador < limite:
        finais.append(estFin[contador])
        print("Final {}".format(estFin[contador]))
        # Estado(estFin[contador],False,True)    #Cria um estado que nC#o C) considerado como um atual, que consta como um estado final
        contador = contador + 1


cont1 = cont2 = cont3 = cont4 = 0
with open(
    "inputs.txt", "r"
) as inputs:  # Armazena as variC!veis de transiC'C#o q sC#o inseridas pelo usuC!rio no arquivo "inputs.txt"
    variaveis = []
    contador = 0
    inp = inputs.readline()
    varis = inp.split(" ")
    limite = (
        len(inp) 
    ) / 2  # NC#o sei pq, mas tem que subtrair 1 e dividir por dois (mesmo o tamanho sendo 4)
    while contador < limite:
        variaveis.append(varis[contador])
        print("variaveis {}".format(varis[contador]))
        # Estado(ests[contador],False,False)    #Cria um estado que nC#o C) considerado como um atual, que nC#o consta como um estado final
        contador = contador + 1
        
print("\n")
cont1 = 0
for x in inp:  # para cada input em input.txt
    cont1 = cont1 + 1
    cont2 = 0
    print("input: {}".format(varis[cont1-1]))
    for y in ativos:  # para cada estado ativo atual
        cont2 = cont2 + 1
        cont3 = 0
        print("ativos: {}".format(ativos[cont2-1]))
        for z in Atual:  # para cada transiC'C#o possivel
            cont3 = cont3 + 1
            if (
                y == z
            ):  # se os ativos atuais forem iguais a algum dos atuais(possuirem alguma transiC'C#o)
                if (
                    x == Vari[cont3-1]
                ):  # se o input atual for igual a variavel da transiC'C#o
                    print("{}: {}->{}".format(x, z, Goto[cont3 - 1]))
                    ativos.append(Goto[cont3 - 1])
            else:
                continue
    print("\nexclui")
    print(ativos)
    ativos.pop(0)
    print("excluido\n")
