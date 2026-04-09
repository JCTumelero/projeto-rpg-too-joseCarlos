# -*- coding: utf-8 -*-
"""personagem .ipynb

"""

class Personagem:
  def __init__(self, nome):
    self.nome = nome
    self.__nivel = 1
    self.__vida = 100
    self.__xp = 0

  @property
  def nome(self):
      return self.__nome

  @property
  def nivel(self):
      return self.__nivel

  @property
  def vida(self): # Corrected from vidal
      return self.__vida

  @nome.setter
  def nome(self,valor):
    valor = valor.strip()
    if not valor: # Corrected indentation
      raise ValueError("O nome do personágem é obrigatório!!!")
    self.__nome = valor

  def __str__(self):
    return f"Personagem: {self.__nome} | Nível: {self.__nivel} "

  def __eq__(self, other):
    return isinstance(other, Personagem) and self.nome == other.__nome

  def exibir_dados(self): # Corrected method name and added parentheses and colon
    print(f"Nome: {self.__nome}")
    print(f"Nível: {self.__nivel}")
    print(f"XP: {self.__xp}")
    print(f"Vida: {self.__vida}")

