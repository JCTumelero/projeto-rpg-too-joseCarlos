import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Adiciona o diretório raiz do projeto ao sys.path para permitir a importação dos módulos

from missao_combate import MissaoCombate
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao 
  

def rodar_teste(missao):
    print("\n--------------------------------------------")
    missao.iniciar_missao()
    missao.concluir_missao()
    missao.exibir_dados()
    
if __name__ == "__main__":
    m1 = MissaoCombate(nome="Limpar a estrada", descricao="Derrotar as ameaças que estão na rota comercial.", recompensa=20, tipo_inimigo="Goblins", inimigos_a_derrotar=5)
    m2 = MissaoColeta(nome="Ervas Raras", descricao="Coletar recursos para o alquimista.", recompensa=15,item_necessario="Erva_lunar", quantidade_item=10)
    m3 = MissaoExploracao(nome="Ruinas Antigas", descricao="Explorar a regiao desconhecida ao norte.", recompensa=15, regiao_destino="Norte de Arcadia", distancia_em_km=12.5)

    rodar_teste(m1)
    rodar_teste(m2)
    rodar_teste(m3)