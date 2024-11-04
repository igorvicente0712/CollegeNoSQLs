import uuid
from astrapy import DataAPIClient
import faker
import random
from unidecode import unidecode

ASTRA_DB_APPLICATION_TOKEN = "token do frifas aqui"
ASTRA_DB_API_ENDPOINT = "codiginho do frifas aqui"

# Inicializa o cliente
client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN)
db = client.get_database_by_api_endpoint(
    ASTRA_DB_API_ENDPOINT,
    keyspace="default_keyspace"
)
fk = faker.Faker('pt_BR')

# --- Geração de Dados (Adaptada para NoSQL/Document DB) ---
n_alunos = 100
n_cursos = 7
n_grupos = 20  # Número máximo de grupos


alunos = []
for _ in range(n_alunos):
    nome = fk.name()
    email = ".".join(unidecode(nome).split(" ")[:2]).lower() + "@collegedb.com"
    id_curso = random.randint(1, n_cursos)
    id_grupo = random.randint(1, n_grupos) if random.random() < 0.7 else None # 70% de chance de ter um grupo
    # Usando UUIDs para os IDs no banco de dados NoSQL
    id_aluno = str(uuid.uuid4())

    alunos.append({
        "id_aluno": id_aluno,  # Adicionando ID único
        "nome": nome,
        "email": email,
        "id_curso": id_curso,
        "id_grupo": id_grupo
    })


# --- Inserção no Astra DB ---

collection_name = "aluno" # Nome da coleção

try:
    results = db[collection_name].insert_many(alunos)
    print("Documentos inseridos com sucesso!")
    print(f"Número de documentos inseridos: {len(results.inserted_ids)}")
except Exception as e:
    print(f"Erro ao inserir documentos: {e}")



# --- Geração de outros dados (Adapte conforme necessário) ---
'''
# Exemplo para cursos:
cursos = []
nomes_cursos = [
    "Ciência da Computação",
    "Engenharia Elétrica",
    # ... outros cursos
]
for nome in nomes_cursos:
  cursos.append({"id_curso": str(uuid.uuid4()), "nome": nome})

collection_name = "curso"
try:
    results = db[collection_name].insert_many(cursos)
    print("Cursos inseridos com sucesso!")
    print(f"Número de cursos inseridos: {len(results.inserted_ids)}")
except Exception as e:
    print(f"Erro ao inserir cursos: {e}")
'''


# Repita o processo para as demais entidades (departamento, disciplina, etc.), 
# adaptando a estrutura dos dados para o formato de documento e gerando UUIDs