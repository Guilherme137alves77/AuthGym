# importa a classe Aluno diretamente do pacote core 
from core.aluno import Aluno
# importa a classe funcionario do pacorte core
from core.funcionario import Funcionario
from sys import sys

def executar_teste():
    print("=" * 50)
    print("Iniciando Testes do Sistema GymVault")
    print("=" * 50)

# CENÁRIO 1: VALIDAÇÃO DE PERMISSÕES DE FUNCIONÁRIOS
    print("\nCENÁRIO 1: Validação de Permissões de Funcionários")
    print("=" * 50)

    admin = Funcionario(nome="Camacho", usuario="camacho_admin", senha_hash="hash_brycrypt_1", cargo="ADMIN")

    recepcao = Funcionario(nome="guilherme", usuario="guilherme_recep", senha_hash="hash_bcrypt_2", cargo="recepcao")


    print("\n[TESTE V2] Verificando Consistência com Controle de Fluxo Ativo...")
    print("-" * 50)

    aluno_valido = Aluno(nome="Carlos Silva", cpf="123.456.789-00", plano_status="ATIVO")
    aluno_cpf_errado = Aluno(nome="Mariana Souza", cpf="123.456", plano_status="ATIVO")

    if aluno_valido.validar_dados() == True:
        print("[OK] Teste de cadastro válido passou com sucesso.")
    else:
        print("[ALERTA CRÍTICO] O sistema bloqueou um aluno com dados legítimos! Parando sistema.")
    sys.exit(1) # Encerra o script imediatamente impedindo qualquer execução posterior
# CASO 2: Testando o aluno inválido (O sistema DEVE retornar False)
    if aluno_cpf_errado.validar_dados() == False:
        print("[OK] Segurança Lógica Funcionando: O sistema barrou o CPF curto de forma correta.")
    else:
        print("[ALERTA DE VULNERABILIDADE] O sistema aceitou um CPF inválido! Abortando por segurança.")
    sys.exit(1) # Força a parada caso a segurança tenha falhado e aceitado o dado ruim


if __name__ == "___main__" :
    executar_teste