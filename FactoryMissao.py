from missao_combate import MissaoCombate
from missao_coleta import MissaoColeta  
from missao_exploracao import MissaoExploracao

class FactoryMissao:
    @staticmethod
    def criar_missao_combate(nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
        return MissaoCombate(nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar)
            

    @staticmethod
    def criar_missao_coleta(nome, descricao, recompensa, item_necessario, quantidade_item):
        return MissaoColeta(nome, descricao, recompensa, item_necessario, quantidade_item)
    
    
    @staticmethod
    def criar_missao_exploracao(nome, descricao, recompensa, regiao_destino, distancia_em_km):
        return MissaoExploracao(nome, descricao, recompensa, regiao_destino, distancia_em_km)
    