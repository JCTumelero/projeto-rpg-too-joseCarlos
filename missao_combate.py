from missao import Missao

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo:str, inimigos_a_derrotar:int):
        super().__init__(nome, descricao, recompensa)
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar

    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo
    
    @tipo_inimigo.setter
    def tipo_inimigo(self, valor:str):
        valor = valor.strip()
        if not valor:
            raise ValueError("O inimigo para a missão de combate é obrigatório!!!")
        self.__tipo_inimigo = valor
        
    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor:int):
        if not isinstance(valor, int) or valor <= 0:
            raise TypeError("A quantidade de inimigos a derrotar deve ser um número inteiro positivo!!!")
        self.__inimigos_a_derrotar = valor

    @property
    def local_combate(self):
        return self.__local_combate
    
 
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo do Inimigo: {self.tipo_inimigo}")
        print(f"Quantidade de inimigos a derrotar: {self.inimigos_a_derrotar}")