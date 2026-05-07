# -*- coding: utf-8 -*-
"""personagem .ipynb

"""

from item import Item, TipoItem

class Personagem:
  def __init__(self, nome):
    self.nome = nome
    self.__nivel = 1
    self.__vida = 100
    self.__xp = 0
    self.ataqueBase = 10
    self.inventario = []
    self.arma_equipada = None
    self.vestimenta_equipada = None
    self.utilitario_equipado = None

  @property
  def nome(self):
      return self.__nome

  @property
  def nivel(self):
      return self.__nivel

  @property
  def vida(self): # Corrected from vidal
      return self.__vida

  @property
  def ataque_total(self):
      bonus = self.arma_equipada.valorEfeito if self.arma_equipada else 0
      return self.ataqueBase + bonus

  @property
  def vida_total(self):
      base = self.__vida
      bonus_percent = 0
      if self.vestimenta_equipada:
          bonus_percent += self.vestimenta_equipada.valorEfeito
      if self.utilitario_equipado:
          bonus_percent += self.utilitario_equipado.valorEfeito
      total = base * (1 + bonus_percent / 100)
      return min(total, 100)

  @nome.setter
  def nome(self,valor):
    valor = valor.strip()
    if not valor: # Corrected indentation
      raise ValueError("O nome do personágem é obrigatório!!!")
    self.__nome = valor

  def equipar_item(self, item):
    if item not in self.inventario:
      raise ValueError("O item deve estar no inventário para ser equipado.")
    if item.tipo == TipoItem.ARMA:
      self.arma_equipada = item
    elif item.tipo == TipoItem.VESTIMENTA:
      self.vestimenta_equipada = item
    elif item.tipo == TipoItem.UTILITARIO:
      self.utilitario_equipado = item
    else:
      raise ValueError("Tipo de item inválido.")
    return self.ataque_total, self.vida_total

  def adicionar_item(self, item):
    self.inventario.append(item)

  def __str__(self):
    return f"Personagem: {self.__nome} | Nível: {self.__nivel} "

  def __eq__(self, other):
    return isinstance(other, Personagem) and self.nome == other.__nome

  def exibir_dados(self): # Corrected method name and added parentheses and colon
    print(f"Nome: {self.__nome}")
    print(f"Nível: {self.__nivel}")
    print(f"XP: {self.__xp}")
    print(f"Vida: {self.__vida}")
    print(f"Ataque Total: {self.ataque_total}")
    print(f"Vida Total: {self.vida_total}")
    print(f"Ataque Base: {self.ataqueBase}")
    print(f"Inventário: {[item.nome for item in self.inventario]}")
    print(f"Arma Equipada: {self.arma_equipada.nome if self.arma_equipada else 'Nenhuma'}")
    print(f"Vestimenta Equipada: {self.vestimenta_equipada.nome if self.vestimenta_equipada else 'Nenhuma'}")
    print(f"Utilitário Equipado: {self.utilitario_equipado.nome if self.utilitario_equipado else 'Nenhum'}")

