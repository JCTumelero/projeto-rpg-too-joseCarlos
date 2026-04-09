from missao import Missao 

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario:str, quantidade_item:int):
        super().__init__(nome, descricao, recompensa)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item
        
    @property
    def item_necessario(self):
        return self.__item_necessario
    @item_necessario.setter
    def item_necessario(self, valor:str):
        valor = valor.strip()
        if not valor:
            raise ValueError("O item necessário para a missão de coleta é obrigatório!!!")
        self.__item_necessario = valor
    
    @property
    def quantidade_item(self):
        return self.__quantidade_item
    
    @quantidade_item.setter
    def quantidade_item(self, valor:int):
        if not isinstance(valor, int) or valor <= 0:
            raise TypeError("A quantidade do item necessário deve ser um número inteiro positivo!!!")
        self.__quantidade_item = valor
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Item necessário: {self.item_necessario}")
        print(f"Quantidade do item necessário: {self.quantidade_item}")