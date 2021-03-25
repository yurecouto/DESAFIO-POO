class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = list()
        self.contas = list()
    
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return None
        
        if cliente.conta not in self.contas:
            return None

        if cliente.conta.agencia not in self.agencias:
            return None

        return True