class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = {}

    def adicionar_quarto(self, quarto):
        self.quartos[quarto.numero] = quarto

    def listar_quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.quartos.values():
            if quarto.esta_disponivel():
                quartos_disponiveis.append(quarto)
        return quartos_disponiveis

    def reservar_quarto(self, numero_quarto):
        quarto = self.quartos.get(numero_quarto)
        if quarto and quarto.esta_disponivel():
            quarto.esta_reservado = True
            return True
        return False

    def cancelar_reserva(self, numero_quarto):
        quarto = self.quartos.get(numero_quarto)
        if quarto and quarto.esta_reservado:
            quarto.esta_reservado = False
            return True
        return False


class Quartos:
    def __init__(self, numero, capacidade, preco):
        self.numero = numero
        self.capacidade = capacidade
        self.preco = preco
        self.esta_reservado = False

    def esta_disponivel(self):
        return not self.esta_reservado

    def obter_detalhes_quarto(self):
        return f"Apartamento {self.numero} - Capacidade: {self.capacidade} pessoas, Preço: {self.preco} por noite"


class ApartamentoSimples(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=1, preco=150)

    def info():
        print("Um quarto simples de hotel, com uma atmosfera acolhedora e funcional. Mobília essencial inclui \numa confortável cama de solteiro com lençóis limpos e macios. Uma pequena mesa de trabalho fica \nao lado da janela, que oferece uma vista discreta. No canto, encontra-se um banheiro compacto \ncom chuveiro, toalhas limpas e amenidades básicas.")

# o "super()" que nós utilizamos é para acessar os métodos e atributos da classe pai "Quartos" em uma hierarquia

class ApartamentoSimplesCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=180)
    
    def info():
        print("Um quarto simples de hotel, com uma atmosfera acolhedora e funcional. Mobília essencial \ninclui uma confortável cama de casal com lençóis limpos e macios. Uma pequena mesa de \ntrabalho fica ao lado da janela, que oferece uma vista discreta. No canto, encontra-se \num banheiro compacto com chuveiro, toalhas limpas e amenidades básicas.")

class ApartamentoDuplo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=200)

    def info():
        print("Um quarto duplo de hotel, projetado para proporcionar conforto compartilhado. \nDuas camas de solteiro dispostas de forma agradável e com lençóis suaves \noferecem um descanso relaxante para dois hóspedes.")


class ApartamentoDuploCasal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=220)

    def info():
        print("Um quarto duplo de casal cuidadosamente projetado para oferecer conforto e intimidade. \nA peça central é uma espaçosa cama de casal adornada com lençóis macios, proporcionando \numa noite de sono relaxante para dois hóspedes")


class ApartamentoLuxo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=300)

    def info():
        print("Adentre o requinte absoluto neste quarto de luxo de hotel. Uma suíte espaçosa que combina \nelegância e conforto em perfeita harmonia. A majestosa cama king-size é um convite ao \ndescanso, vestida com lençóis de alta qualidade que acariciam a pele. A decoração refinada \né complementada por móveis cuidadosamente selecionados e obras de arte sofisticadas adornando as paredes")


class ApartamentoMaster(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=400)

    def info():
        print("A imponente cama king-size, adornada com roupas de cama de alta qualidade, é o epicentro \ndo relaxamento. A decoração exala sofisticação, com móveis elegantes meticulosamente \ndispostos e detalhes de design que impressionam. Uma espaçosa área de estar é ideal para \nreceber convidados ou desfrutar de momentos de tranquilidade. O banheiro é um retiro de \nbem-estar, equipado com banheira de hidromassagem, chuveiro de luxo e produtos de cuidados \npessoais premium. Os hóspedes deste quarto têm acesso a serviços exclusivos, incluindo mordomo \ndedicado e acesso a áreas VIP.")