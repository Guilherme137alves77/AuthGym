# importa as estruturas necessarias para tipagem e facilidade de criaçao de classes 
from dataclasses import dataclass
# importa o tipo Optional para tratar chaves primairas nulas antes dec inserçao no banco de dados
from typing import Optional 

@dataclass
class Aluno:
    """
    Representa a entidade de um aluno matriculado no GymVault.
    Contém dados cadastrais e o estado atual de seu plano financeiro.
    """
    nome: str
    idade: int
    peso: str
    plano_status:str
    id_aluno: Optional[int] = None

    def pode_treinar(self) -> bool:

       cpf_numerico = self.cpr.replace(".", "").replace("-", "").strip()


       if self.nome.strip() == "":
           print(f"[ERRO DE CADASTRO] O nome do aluno não pode estar vazio.")
           return False

       elif len(cpf_numerico) != 11:
            print(f"[ERRO DE CADASTRO] O CPF '{self.cpf}' é invalido. Deve conter 11 digitos.")
            return False


       else:
            print(f"[SUCESSO] Dados do aluno {self.nome} validados internamente ")
            return True
       
    def pode_treinar(self) -> bool:
     status_limpo = self.plano_status.strip().lower()

     if status_limpo == "ativo":
         print(f"[SUCESSO] O aluno {self.nome} está apto a treinar.")
         return True
     else:
         print(f"[ERRO] O aluno {self.nome} não está apto a treinar. Status do plano: '{self.plano_status}'.")
         return False