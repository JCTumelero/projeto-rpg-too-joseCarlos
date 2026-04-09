from missao import Missao

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino:str, distancia_em_km:float):
        super().__init__(nome, descricao, recompensa)
        self.regiao_destino = regiao_destino
        self.distancia_em_km = distancia_em_km
        
    @property
    def regiao_destino(self):
        return self.__regiao_destino
    
    @regiao_destino.setter
    def regiao_destino(self, valor:str):
        valor = valor.strip()
        if not valor:
            raise ValueError("A região de destino para a missão de exploração é obrigatória!!!")
        self.__regiao_destino = valor  
        
    @property
    def distancia_em_km(self):
        return self.__distancia_em_km
    
    @distancia_em_km.setter
    def distancia_em_km(self, valor:float):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise TypeError("A distância em km para a missão de exploração deve ser um número positivo!!!")
        self.__distancia_em_km = float(valor)
        
    def ecibir_daddos(self):
        super().exibir_dados()
        print(f"Região de destino: {self.regiao_destino}")
        print(f"Distância em km: {self.distancia_em_km:.2f} km")