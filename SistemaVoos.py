# SISTEMA DE CONTROLE DE VOOS - 08/02/2024
# Não utilizar funções recursivas e registros 

def printar_todas_reservas(lista_reservas):
    for reserva in lista_reservas:
        reserva.printar_info()

# Printa as informações do voo da reserva passada por ID
def printar_voo(lista_reservas, id):
    for reserva in lista_reservas:
        if reserva.id == id:
            reserva.voo.printar_info()

# Cria um novo voo
def cadastrar_voo(lista_voos):
    while True:
        num_voo = int(input("Numero do Voo:"))
        if num_voo != "":
            break
    while True:
        origem = input("Origem:")
        origem = origem.capitalize()
        if origem != "":
            break
    while True:
        destino = input("Destino:")
        destino = destino.capitalize()
        if destino != "":
            break
    while True:
        data = input("Data:")
        if data != "":
            break
    while True:
        hora = input("Hora:")
        if hora != "":
            break
    while True:
        capacidade_assentos = int(input("Capacidade de assentos:"))
        if capacidade_assentos != "":
            break
    assentos_disponiveis = []
    assentos_reservados = [] # vazio inicialmente
    for i in range(1, capacidade_assentos+1):
        assentos_disponiveis.append(i)

    novoVoo = Voo(num_voo, origem, destino, data, hora, capacidade_assentos, 
                  assentos_disponiveis, assentos_reservados)

    lista_voos.append(novoVoo)
    
    return lista_voos

# Faz um nova reserva
def reservar_assento(lista_voos, lista_reservas, id): 
    while True: 
        aux = True
        visualizar_info(lista_voos)
        
        print("\nTODAS AS RESERVAS FEITAS:")
        printar_todas_reservas(lista_reservas)

        num = int(input("Digite o numero do voo que deseja reservar: "))

        for voo in lista_voos: 
            if voo.num_voo == num:
                if not voo.assentos_disponiveis: 
                    print("Não há assentos disponíveis para esse voo. ") 
                    aux = False
                    break 

                while True:
                    assento = int(input("Digite o assento que deseja reservar: "))
                    if (assento in voo.assentos_reservados) or (assento not in voo.assentos_disponiveis):
                        print("Assento não disponivel")
                    else: 
                        voo.reservar(assento) 
                        nova_reserva = Reserva(id+1, voo) 
                        lista_reservas.append(nova_reserva)
                        print("Assento reservado. \n")

                        return lista_voos, lista_reservas
        if (aux):
            print("Voo não encontrado. Tentar novamente? ")
        else:
            print("Fazer uma nova reserva? ")  
        print("1 - SIM") 
        print("2 - NÃO")

        # Tratando entrada
        while True:
            try:
                escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha == 1 or escolha == 2:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')
        
        if escolha == 2:
            break

# Adiciona assento da reserva do id passado como parametro
def adicionar_assento(lista_voos, lista_reservas, id):
    print("INFORMAÇÃO DO VOO DA SUA RESERVA: \n")
    printar_voo(lista_reservas, id)

    while True:
        for reserva in lista_reservas:
            if reserva.id == id:
                assentoRetirar = int(input("Qual assento você quer adicionar na reserva? "))
                if assentoRetirar in reserva.voo.assentos_reservados:
                    reserva.adicionarAssento()
                    print("Assento adicionado na reserva. ")
                    
        print("Tentar novamente? ")
        print("1 - SIM")
        print("2 - NÃO")

        # Tratando entrada
        while True:
            try:
                escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha == 1 or escolha == 2:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')
        
        if escolha == 2:
            break

# Remove assento da reserva do id passado como parametro
def remover_assento(lista_voos, lista_reservas, id):
    print("INFORMAÇÃO DO VOO DA SUA RESERVA: \n")
    printar_voo(lista_reservas, id)

    while True:   
        for reserva in lista_reservas:
            if reserva.id == id:
                assentoRetirar = int(input("Qual assento você quer retirar da reserva? "))
                if assentoRetirar in reserva.voo.assentos_reservados:
                    reserva.retirarAssento()
                    print("Assento removido da reserva. \n")
                    
        print("Tentar novamente? ")  
        print("1 - SIM")
        print("2 - NÃO")

        # Tratando entrada
        while True:
            try:
                escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha == 1 or escolha == 2:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')
        
        if escolha == 2:
            break

# Adiciona ou retirar assentos de uma reserva
def alterar_reservas(lista_voos, lista_reservas, id):
    aux = True
    for reserva in lista_reservas: 
        if reserva.id == id:  
            aux = False
            print("Você que retirar ou adicionar assento? ")
            print("1 - RETIRAR") 
            print("2 - ADICIONAR")

            while True:
                try:
                    escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                    if escolha == 1 or escolha == 2:
                        break
                    else:
                        print('Inválido.') 
                except ValueError:
                    print('Inválido.') 
    if aux:
        print("Não foi encontrada reserva com esse ID. ") 
            
    # Retirar assento da reserva
    if escolha == 1:
        nova_lista_voos, nova_lista_reservas = remover_assento(lista_voos, lista_reservas, id)
        lista_voos = nova_lista_voos 
        lista_reservas = nova_lista_reservas 

    # Adicionar assento da reserva
    else: 
        nova_lista_voos, nova_lista_reservas = adicionar_assento(lista_voos, lista_reservas, id)
        lista_voos = nova_lista_voos 
        lista_reservas = nova_lista_reservas

    return nova_lista_voos, nova_lista_reservas

def visualizar_info(lista_voos):
    print("\nVOOS DISPONÍVEIS: ")
    print("===========================")
    for i in lista_voos:
        i.printar_info()

class Voo: 
    def __init__(self, num_voo, origem, destino, data, hora, capacidade_assentos, assentos_reservados, assentos_disponiveis):
        self.num_voo = num_voo
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.capacidade_assentos = capacidade_assentos
        self.assentos_reservados = assentos_reservados
        self.assentos_disponiveis = assentos_disponiveis

    def printar_info(self): 
        print("\nINFORMAÇÕES DO VOO:")

        print("Numero do voo:", self.num_voo)
        print("Origem:", self.origem)
        print("Destino:", self.destino)
        print("Data:", self.data)
        print("Hora:", self.hora)
        print("Capacidade de assentos:", self.capacidade_assentos)
        print("Assentos reservados:", self.assentos_reservados)
        print("Assentos disponíveis:", self.assentos_disponiveis)
    
    def reservar(self, assento):
        self.assentos_disponiveis.remove(assento)
        self.assentos_reservados.append(assento)
        print("deu certo")

class Reserva:
    def __init__(self, id, voo):
        self.id = id
        self.voo = voo
 
    def printar_info(self):
        print("\n============================")
        print("ID da reserva:", self.id)
        print("Voo da reserva: ")
        self.voo.printar_info()
 
    def retirarAssento(self, assento):
        self.voo.assentos_reservados.remove(assento)
        self.voo.assentos_disponiveis.append(assento)

    def adicionarAssento(self, assento): 
        self.voo.assentos_disponiveis.remove(assento)
        self.voo.assentos_reservados.append(assento)  

def main():
    id_aux = 4 # valor inicial   
    # cada novo id criado vai sendo adicionado

    Voo1 = Voo(12, "Brasil", "Canada", "10/03/2024", "12:30", 8, [1, 4, 5, 8], [2, 3, 6, 7])
    Voo2 = Voo(32, "Africa do Sul", "China", "20/04/2024", "20:00", 7, [2, 3, 5], [1, 4, 6, 7])
    Voo3 = Voo(4, "Argentina", "Venezuela", "05/06/2024", "15:30", 6, [1, 2, 3, 4, 5, 6], [])
    Voo4 = Voo(10, "Alemanha", "Inglaterra", "02/01/2025", "13:00", 6, [1, 6], [2, 3, 4, 5])

    lista_voos = [Voo1, Voo2, Voo3, Voo4]

    reserva1 = Reserva(1, Voo1)
    reserva2 = Reserva(2, Voo2)
    reserva3 = Reserva(3, Voo3)
    reserva4 = Reserva(4, Voo4)

    lista_reservas = [reserva1, reserva2, reserva3, reserva4]
        
    print("\nSistema de Controle de Voos")
    print("=================================")
    print("O que você gostaria de realizar?\n")

    while True:
        # Escolhas
        print("1 - Gerenciamento de voos e assentos")
        print("2 - Alterar as reservas existentes")
        print("3 - Visualizar informações detalhadas sobre os voos disponíveis")

        # Tratando para casos inválidos
        while True:  
            try:
                escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha == 1 or escolha == 2 or escolha == 3:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')

        # Gerenciamento de voos e assentos 
        if escolha == 1:
            print("1 - Cadastrar novo voo")
            print("2 - Reservar assento(s)")

            while True:
                try:
                    escolha1 = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                    if escolha1 == 1 or escolha1 == 2:
                        break
                    else:
                        print('Inválido.')
                except ValueError:
                    print('Inválido.')
            
            if escolha1 == 1:
                lista_voos = cadastrar_voo(lista_voos)

            if escolha1 == 2: 
                nova_lista_voos, nova_lista_reservas = reservar_assento(lista_voos, lista_reservas, id_aux)
                lista_voos = nova_lista_voos 
                lista_reservas = nova_lista_reservas
                id_aux+= 1   

                while True:
                    print("\nGostaria de reservar mais um assento? ")
                    print("1 - SIM")
                    print("2 - NÃO")
                    while True:
                        try:
                            escolha = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                            if escolha == 1 or escolha == 2:
                                break
                            else:
                                print('Inválido.') 
                        except ValueError:
                            print('Inválido.')

                    if escolha == 1:  
                        reservar_assento(lista_voos, lista_reservas, id_aux)
                    else:
                        break

        if escolha == 2:  
            printar_todas_reservas(lista_reservas)
            id = int(input("Digite o ID da reserva que deseja alterar: ")) 

            nova_lista_voos, nova_lista_reservas = alterar_reservas(lista_voos, lista_reservas, id)
            lista_voos = nova_lista_voos
            lista_reservas = nova_lista_reservas 

        if escolha == 3:
            visualizar_info(lista_voos)

        print("Voce gostaria de continuar o programa?")
        print("1 - SIM")
        print("2 - NÃO")

        # Tratando entrada
        while True:
            try:
                continuar = int(input('\nESCOLHA O NÚMERO DA OPÇÃO: '))
                if continuar == 1 or continuar == 2:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')
        
        if continuar == 2:
            print("\nENCERRANDO PROGRAMA...")
            break

# PROGRAMA PRINCIPAL
main()   