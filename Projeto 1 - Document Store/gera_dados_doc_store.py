from faker import Faker
import random
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

fake = Faker()

# Configurações
NUM_ALUNOS = 10
NUM_PROFESSORES = 5
NUM_CURSOS = 3
NUM_DEPARTAMENTOS = 2
NUM_DISCIPLINAS = 10
NUM_GRUPOS_TCC = 3

# Listas para armazenar dados
alunos = []
professores = []
cursos = []
departamentos = []
disciplinas = []
grupos_tcc = []

# Gerar cursos
for _ in range(NUM_CURSOS):
    cursos.append({
        "_id": str(fake.unique.random_number(digits=5)),
        "nome": fake.job(),
        "disciplinas": []
    })

# Gerar departamentos
for _ in range(NUM_DEPARTAMENTOS):
    departamentos.append({
        "_id": str(fake.unique.random_number(digits=4)),
        "nome": fake.company(),
        "chefe": None
    })

# Gerar disciplinas e associar a cursos e departamentos
for _ in range(NUM_DISCIPLINAS):
    disciplina_id = str(fake.unique.random_number(digits=6))
    disciplina = {
        "_id": disciplina_id,
        "nome": fake.catch_phrase(),
        "departamento": random.choice(departamentos)["_id"]
    }
    disciplinas.append(disciplina)
    random.choice(cursos)["disciplinas"].append(disciplina_id)

# Gerar professores e associar a disciplinas
for _ in range(NUM_PROFESSORES):
    professor_id = str(fake.unique.random_number(digits=5))
    professor = {
        "_id": professor_id,
        "nome": fake.name(),
        "disciplinas": [
            {
                "codigo": disc["_id"],
                "ano": random.randint(2020, 2024),
                "semestre": random.randint(1, 2)
            } for disc in random.sample(disciplinas, random.randint(1, 3))
        ]
    }
    professores.append(professor)

# Atribuir chefes aos departamentos
for departamento in departamentos:
    chefe = random.choice(professores)
    departamento["chefe"] = chefe["_id"]
    chefe["departamento"] = departamento["_id"]

# Gerar alunos e associar a cursos e disciplinas
for _ in range(NUM_ALUNOS):
    curso = random.choice(cursos)
    aluno = {
        "_id": str(fake.unique.random_number(digits=7)),
        "nome": fake.name(),
        "curso": curso["_id"],
        "disciplinas": [
            {
                "codigo": disc_id,
                "ano": random.randint(2020, 2024),
                "semestre": random.randint(1, 2),
                "nota": round(random.uniform(5, 10), 1)
            } for disc_id in random.sample(curso["disciplinas"], random.randint(1, len(curso["disciplinas"])))
        ],
        "tcc": None
    }
    alunos.append(aluno)

# Gerar grupos de TCC e associar a alunos e professores
for _ in range(NUM_GRUPOS_TCC):
    grupo_id = str(fake.unique.random_number(digits=3))
    grupo = {
        "_id": grupo_id,
        "ano": random.randint(2020, 2024),
        "semestre": random.randint(1, 2),
        "alunos": random.sample(alunos, random.randint(2, 4)),
        "orientador": random.choice(professores)["_id"]
    }
    grupos_tcc.append(grupo)
    for aluno in grupo["alunos"]:
        aluno["tcc"] = {
            "grupo_id": grupo_id,
            "orientador": grupo["orientador"]
        }

# Função para escrever dados em arquivos JSON
def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Escrever dados em arquivos JSON
write_json('alunos.json', alunos)
write_json('professores.json', professores)
write_json('cursos.json', cursos)
write_json('departamentos.json', departamentos)
write_json('disciplinas.json', disciplinas)
write_json('grupos_tcc.json', grupos_tcc)

print("Dados foram escritos nos arquivos JSON.")

check_execute = input("Deseja executar as queries? (s/n) ")
if check_execute == "s":
    with open(r"D:\GitHub\CollegeNoSQLs\Projeto 1 - Document Store\cred.txt") as f:
        cred = f.read()

    uri = cred.split("\n")[0]

    # Conectar ao MongoDB
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['faculdade']

    # Inserir dados nas coleções
    db.alunos.insert_many(alunos)
    db.professores.insert_many(professores)
    db.cursos.insert_many(cursos)
    db.departamentos.insert_many(departamentos)
    db.disciplinas.insert_many(disciplinas)
    db.grupos_tcc.insert_many(grupos_tcc)

    print("Dados foram inseridos no MongoDB.")

    # Fechar a conexão
    client.close()
