from status import Status

class Missao:
    def __init__(self, nome: str, descricao: str, recompensa: int):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = Status.PENDENTE
        
        #getters
        
    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def recompensa(self):
        return self.__recompensa
    @property
    def status(self):
        return self.__status
    
    #setters
    
    @nome.setter
    def nome(self, valor):
        valor = valor.strip()
        if not valor:
            raise ValueError("O nome da missão é obrigatório!!!")
        self.__nome = valor
        
    @descricao.setter
    def descricao(self, valor:str):
        valor = valor.strip()
        if not valor:
            raise ValueError("A descrição da missão é obrigatória!!!")
        self.__descricao = valor
    
    @recompensa.setter
    def recompensa(self, valor:int):
        if not isinstance(valor, int) or valor < 0:
            raise TypeError("A recompensa deve ser um número inteiro positivo!!!")
        if 1 <= valor <= 50:
            self.__recompensa = valor
        else:
            raise ValueError("A recompensa deve ser entre 1 e 50 pontos!!!")
   
    @status.setter
    def status(self, valor):
        if not isinstance(valor, Status):
            raise TypeError("O status deve ser uma instância da enumeração Status!!!")
        self.__status = valor
        
    def iniciar_missao(self):
        if self.status == Status.PENDENTE:
            self.status = Status.EM_ANDAMENTO
            print(f"A missão '{self.nome}' foi iniciada! Objetivo central: {self.descricao}")
        elif self.status == Status.EM_ANDAMENTO:
            raise ValueError("A missão já está em andamento!!! Não pode iniciar novamente.")
        elif self.status == Status.CONCLUIDA:
            raise ValueError("A missão já foi concluída!!! Não pode iniciar novamente.")
        else:
            raise ValueError("A missão está fracassada!!! Não pode iniciar novamente.")
        
    def concluir_missao(self):
        if self.status == Status.EM_ANDAMENTO:
            self.status = Status.CONCLUIDA
            print(f"Parabéns! Você concluiu a missão '{self.nome}' e ganhou {self.recompensa} pontos de recompensa!")
        elif self.status == Status.PENDENTE:
            raise ValueError("A missão ainda não foi iniciada!!! Não pode concluir.")
        else:
            raise ValueError("A missão não pode ser concluída neste estado.")
        
    def exibir_dados(self):
        print(f"===Dados da Missão: {self.nome}===")
        print(f"Descrição: {self.descricao}")
        print(f"Recompensa: {self.recompensa}")
        print(f"Status: {self.status.name}")
        
   
    def __str__(self):
        return f"Missao(nome='{self.nome}', status='{self.status.value}')"

    def __eq__(self, other):
        return isinstance(other, Missao) and self.nome == other.nome

