from dataclasses import dataclass
from typing import Optional 
class Aluno:

    nome: str
    idade: int
    peso: str
    id_aluno: Optional[int] = None