from item import Item, TipoItem
from personagem_jose_carlos_tumelero import Personagem

# Criar itens de diferentes tipos
arma = Item("Espada", "Uma espada afiada", TipoItem.ARMA, 15)
vestimenta = Item("Armadura", "Proteção forte", TipoItem.VESTIMENTA, 20)
utilitario = Item("Poção", "Restaura vida", TipoItem.UTILITARIO, 10)

# Criar personagem
personagem = Personagem("José Carlos")

# Adicionar itens ao inventário
personagem.adicionar_item(arma)
personagem.adicionar_item(vestimenta)
personagem.adicionar_item(utilitario)

# Equipar itens
ataque_total, vida_total = personagem.equipar_item(arma)
ataque_total, vida_total = personagem.equipar_item(vestimenta)
ataque_total, vida_total = personagem.equipar_item(utilitario)

# Imprimir status finais
print(f"Ataque Total: {ataque_total}")
print(f"Vida Total: {vida_total}")
print("Pronto para a missão!")