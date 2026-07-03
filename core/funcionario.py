from dataclasses import dataclass
from typing import Optional

@dataclass
class Funcionario:
    nome: str
    idade: int
    cargo: str
    salario: float
    email: str
    telefone: Optional[str] = None

    id_funcionario: Optional[int] = None  # ID do funcionário, pode ser None se não for atribuído]
    
    def tem_permissao(self) -> bool:

        cargo_verificado = self.cargo.strip().upper()


        if cargo_verificado != "ADMIN" :
            print(f"[SEGURANÇA] Acesso negado: Usuario {self.usuario} nao possui nivel ADMIN. ")
            return False
        else:
            # Executado apenas se o cargo for estritamente igual a "ADMIN"
            print(f"[AUTORIZADO] Usuário {self.usuario} liberado para ações críticas.")
            return True
