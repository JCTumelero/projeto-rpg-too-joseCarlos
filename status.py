from enum import Enum

class Status(Enum): 
    PENDENTE  = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    CONCLUIDA  = "Concluída"
    FRACASSADA = "Fracassada"
    