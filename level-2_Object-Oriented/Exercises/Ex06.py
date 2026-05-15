class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'O titular do saldo é {self.titular}, e o seu saldo da conta {self.saldo} e essa conta está {self.ativo}'
    
    def ativar_conta(self):
            self.ativo = True
    
    def conferir_ativo(self):
         if self.ativo:
            return 'ativo'
         else:
              return 'desativo'
    
conta1 = ContaBancaria('Ana Luisa', 1000000000.00)
conta1.ativar_conta()
conta1.conferir_ativo()
conta2 = ContaBancaria('Itallo', 1000000000.00)
conta2.conferir_ativo()

print(f'{conta1} \n {conta2}')

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
          self._titular = titular
          self._saldo = saldo
          self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
         return self._saldo
    
    @property
    def ativo(self):
         return self._ativo
    
    def ativar_conta(self):
         self._ativo = True

conta_pythonica1 = ContaBancariaPythonica('Ana Luisa', 100000000.00)

print(f'Titular da conta: {conta_pythonica1.titular}')


# -------------------------------------------------------------------------------------------------

# TERMINAR

# 7) Crie um método de classe para a conta `ClienteBanco`.
class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")