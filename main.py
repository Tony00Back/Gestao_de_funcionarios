import datetime



def registar_funcionario():

    num_func=int(input("QUANTOS FUNCIONÁRIOS PRETENDE REGISTAR? : "))
    lista_funci=[]

     #adicionando funcionários


    while num_func>0:


        codigo=numero_de_func()+1
        print(f"Codigo:{codigo}")
        nome=input('NOME DO FUNCIONÁRIO: ')
        print("DATA DE NASCIMENTO:")
        ano=int(input("Ano:"))
        mes=int(input("Mes:"))
        dia=int(input("Dia:"))
        data=datetime.date(ano,mes,dia)
        morada=input('MORADA: ')
        idade=int(input('IDADE: '))
        telefone=input('TELEFONE: ')
        email=input('EMAIL: ')
        lista_funci.append((dict(Codigo=codigo,Nome=nome,Data=data,
                            Morada=morada,Idade=idade,Telefone=telefone,email=email)))
        print(f"Funcionário Registado!\n "
              f"Codigo de Funcionario: {codigo}\n"
              f"Nome Completo: {nome}\n"
              f"Data de Nascimento: {data}\n"
              f"Morada: {morada}\n"
              f"Idade: {idade}\n"
              f"Telefone: {telefone}\n"
              f"Email: {email}\n")

        with open('tabela de funcionarios.txt','a+') as f:
            for item in lista_funci:
                f.write("%s\n"%item)

        num_func-=1


def listar_funcionarios():
    with open('tabela de funcionarios.txt','r') as fp:
        for line in fp:
            print(line)
def listar_5():

    file = open('tabela de funcionarios.txt')

    content = file.readlines()

    print(content[0],"\n")
    print(content[1], "\n")
    print(content[2], "\n")
    print(content[3], "\n")
    print(content[4], "\n")


def listar_por_codigo():

    codigo=int(input("\nCodigo do funcionario: "))
    file = open('tabela de funcionarios.txt')

    content = file.readlines()
    print(content[codigo-1])

def numero_de_func():
    with open('tabela de funcionarios.txt','r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def remover_func():
    try:
        funcionario=int(input("CODIGO DE FUNCIONARIO: "))
        with open('tabela de funcionarios.txt', 'r') as fr:

            lines = fr.readlines()
            ptr = 1

            with open('tabela de funcionarios.txt', 'w') as fw:
                for line in lines:


                    if ptr !=funcionario:
                        fw.write(line)
                    ptr += 1
        print("Registo apagado")

    except:
        print("ERRO!")

def alterar_func():
    with open('tabela de funcionarios.txt', 'r', encoding='utf-8') as file:
        dados = file.readlines()

    print(dados)
    codigo=int(input('Codigo do Funcionario: '))
    dados[codigo-1]=input("alteração: ")


    with open('tabela de funcionarios.txt', 'w', encoding='utf-8') as file:
        file.writelines(dados)
        print("Dados alterados com sucesso!")


opcao=0
print('*'*40)
print("PROGRAMA DE GESTÃO DE FUNCIONÁRIOS")
print('*'*40)
print("")

print("\tMENU DE OPÇÕES")
print(f'1- REGISTAR  NOVOS FUNCIONÁRIOS\n'
      f'2- PESQUISAR FUNCIONÁRIO\n'
      f'3- LISTAR TODOS OS FUNCIONÁRIOS\n'
      f'4- LISTAR OS PRIMEIROS 5 FUNCIONÁRIOS\n'
      f'5- REMOVER FUNCIONÁRIOS\n'
      f'6- ACTUALIZAR DADOS DO FUNCIONÁRIO\n'
      f'7- MOSTRAR QUANTIDADE DE FUNCIONÁRIOS\n')


opcao=input('ESCOLHA UMA OPÇÃO (1-7):')

if opcao=='1':
    registar_funcionario()
if opcao=='2':
    listar_por_codigo()
if opcao=='3':
    listar_funcionarios()
if opcao=='4':
    listar_5()
if opcao=='5':
    remover_func()
if opcao=='6':
    alterar_func()
if opcao == '7':
    print(numero_de_func(), "Funcionários Cadastrados. ")