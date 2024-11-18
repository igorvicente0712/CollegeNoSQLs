from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os



# Função para carregar as credenciais do AstraDB
def get_astra_session():
    cloud_config = {
        'secure_connect_bundle': 'D:/secure-connect-projetodb.zip'
    }
    auth_provider = PlainTextAuthProvider('key.clientId', 'key.secret')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect('fei')  # Conectar ao keyspace "fei"
    return session

# Função para ler arquivos e executar comandos INSERT
def execute_inserts_from_files(file_names):
    session = get_astra_session()
    for file_name in file_names:
        if os.path.exists(file_name):
            print(f"Lendo o arquivo: {file_name}")
            try:
                # Tenta abrir com UTF-8 primeiro
                with open(file_name, 'r', encoding="utf-8") as file:
                    commands = file.read().split(';')
            except Exception as e:
                print(f"Erro ao abrir com UTF-8: {e}")
                try:
                    # Se falhar, tenta abrir com encoding padrão
                    print("Tentando abrir com encoding padrão do sistema...")
                    with open(file_name, 'r') as file:
                        commands = file.read().split(';')
                except Exception as e2:
                    print(f"Erro ao abrir o arquivo: {file_name}\nErro: {e2}")
                    continue # Pula para o próximo arquivo se nenhum encoding funcionar

            for command in commands:
                command = command.strip()
                if command.upper().startswith("INSERT"):
                    try:
                        session.execute(command + ";")
                        print("Comando executado com sucesso:", command)
                    except Exception as e:
                        print(f"Erro ao executar o comando: {command}\nErro: {e}")
        else:
            print(f"Arquivo {file_name} não encontrado.")

# Lista de arquivos específicos para serem lidos
file_names = [
    "1alunos_formados.cql", 
    "1alunos.cql", #UTF-8
    "1departamentos.cql", 
    "1grupo_proj.cql", 
    "1professores.cql" #UTF-8
]

# Chamada da função
execute_inserts_from_files(file_names)
