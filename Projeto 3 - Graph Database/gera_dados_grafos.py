from faker import Faker
import random
from neo4j import GraphDatabase

fake = Faker()

NUM_ALUNOS = 100
NUM_PROFESSORES = 10
NUM_CURSOS = 10
NUM_DEPARTAMENTOS = 4
NUM_DISCIPLINAS = 40
NUM_GRUPOS_TCC = 10

alunos = []
professores = []
cursos = []
departamentos = []
disciplinas = []
grupos_tcc = []
queries = []

create_nodes_path = "create_nodes.cypher"
create_rel_path = "create_relationships.cypher"

for _ in range(NUM_ALUNOS):
    alunos.append({
        "nome": fake.name(),
        "matricula": fake.unique.random_number(digits=7)
    })

for _ in range(NUM_PROFESSORES):
    professores.append({
        "nome": fake.name(),
        "id_professor": fake.unique.random_number(digits=5)
    })

for _ in range(NUM_CURSOS):
    cursos.append({
        "nome": fake.job(),
        "codigo": fake.unique.random_number(digits=5)
    })

for _ in range(NUM_DEPARTAMENTOS):
    departamentos.append({
        "nome": fake.company(),
        "codigo": fake.unique.random_number(digits=4)
    })

for _ in range(NUM_DISCIPLINAS):
    disciplinas.append({
        "nome": fake.catch_phrase(),
        "codigo": fake.unique.random_number(digits=6),
        "departamento": random.choice(departamentos)["codigo"]
    })

for _ in range(NUM_GRUPOS_TCC):
    grupos_tcc.append({
        "ano": random.randint(2020, 2024),
        "semestre": random.randint(1, 2)
    })

curso_disciplinas = {curso["codigo"]: [] for curso in cursos}
for disciplina in disciplinas:
    curso_codigo = random.choice(list(curso_disciplinas.keys()))
    curso_disciplinas[curso_codigo].append(disciplina["codigo"])

def write_queries(filename, queries):
    with open(filename, 'w') as f:
        for query in queries:
            f.write(query + '\n')

# Criar Alunos
for aluno in alunos:
    queries.append(f"CREATE (:Aluno {{nome: '{aluno['nome']}', matricula: '{aluno['matricula']}'}});")

# Criar Professores
for professor in professores:
    queries.append(f"CREATE (:Professor {{nome: '{professor['nome']}', id_professor: '{professor['id_professor']}'}});")

# Criar Cursos
for curso in cursos:
    queries.append(f"CREATE (:Curso {{nome: '{curso['nome']}', codigo: '{curso['codigo']}'}});")

# Criar Departamentos
for departamento in departamentos:
    queries.append(f"CREATE (:Departamento {{nome: '{departamento['nome']}', codigo: '{departamento['codigo']}'}});")

# Criar Disciplinas
for disciplina in disciplinas:
    queries.append(f"CREATE (:Disciplina {{nome: '{disciplina['nome']}', codigo: '{disciplina['codigo']}'}});")

# Criar Grupos de TCC
for grupo in grupos_tcc:
    queries.append(f"CREATE (:GrupoTCC {{ano: {grupo['ano']}, semestre: {grupo['semestre']}}});")

# Alunos cursando cursos
for aluno in alunos:
    curso = random.choice(cursos)
    queries.append(f"MATCH (a:Aluno {{matricula: '{aluno['matricula']}'}}), (c:Curso {{codigo: '{curso['codigo']}'}}) CREATE (a)-[:CURSA]->(c);")

# Alunos cursando disciplinas
for aluno in alunos:
    curso_codigo = random.choice(list(curso_disciplinas.keys()))
    num_disciplinas = random.randint(1, len(curso_disciplinas[curso_codigo]))
    for _ in range(num_disciplinas):
        disciplina_codigo = random.choice(curso_disciplinas[curso_codigo])
        queries.append(f"MATCH (a:Aluno {{matricula: '{aluno['matricula']}'}}), (d:Disciplina {{codigo: '{disciplina_codigo}'}}) CREATE (a)-[:CURSOU {{ano: {random.randint(2020, 2024)}, semestre: {random.randint(1, 2)}, nota: {random.uniform(5, 10):.1f}}}]->(d);")

# Professores ministrando disciplinas
for professor in professores:
    num_disciplinas = random.randint(1, 3)
    for _ in range(num_disciplinas):
        disciplina = random.choice(disciplinas)
        queries.append(f"MATCH (p:Professor {{id_professor: '{professor['id_professor']}'}}), (d:Disciplina {{codigo: '{disciplina['codigo']}'}}) CREATE (p)-[:MINISTRA {{ano: {random.randint(2020, 2024)}, semestre: {random.randint(1, 2)}}}]->(d);")

# Professores chefiando departamentos
for professor in professores:
    if random.choice([True, False]):
        departamento = random.choice(departamentos)
        queries.append(f"MATCH (p:Professor {{id_professor: '{professor['id_professor']}'}}), (d:Departamento {{codigo: '{departamento['codigo']}'}}) CREATE (p)-[:CHEFIA]->(d);")

# Disciplinas pertencendo a departamentos
for disciplina in disciplinas:
    queries.append(f"MATCH (d:Disciplina {{codigo: '{disciplina['codigo']}'}}), (dep:Departamento {{codigo: '{disciplina['departamento']}'}}) CREATE (d)-[:PERTENCE]->(dep);")

# Alunos participando de grupos de TCC e professores orientando
for grupo in grupos_tcc:
    grupo_id = f"{grupo['ano']}_{grupo['semestre']}"
    num_participantes = random.randint(1, 3)
    orientador = random.choice(professores)
    queries.append(f"MATCH (g:GrupoTCC {{ano: {grupo['ano']}, semestre: {grupo['semestre']}}}), (p:Professor {{id_professor: '{orientador['id_professor']}'}}) CREATE (p)-[:ORIENTA]->(g);")
    for _ in range(num_participantes):
        aluno = random.choice(alunos)
        queries.append(f"MATCH (g:GrupoTCC {{ano: {grupo['ano']}, semestre: {grupo['semestre']}}}), (a:Aluno {{matricula: '{aluno['matricula']}'}}) CREATE (a)-[:PARTICIPA]->(g);")

write_queries('create_nodes.cypher', queries[:len(alunos) + len(professores) + len(cursos) + len(departamentos) + len(disciplinas) + len(grupos_tcc)])
write_queries('create_relationships.cypher', queries[len(alunos) + len(professores) + len(cursos) + len(departamentos) + len(disciplinas) + len(grupos_tcc):])

print(f"Queries escritas em '{create_nodes_path}' e '{create_rel_path}'")

def execute_queries(queries):
    with open(r"D:\GitHub\CollegeNoSQLs\Projeto 3 - Graph Database\Neo4j-5e9030ad-Created-2024-11-02.txt") as f:
        cred = f.read()

    uri = cred.split("\n")[1]
    uri = uri[uri.find("=") + 1:]

    user = cred.split("\n")[2]
    user = user[user.find("=") + 1:]

    password = cred.split("\n")[3]
    password = password[password.find("=") + 1:]

    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        for query in queries:
            session.run(query)
    driver.close()
    print("Queries executadas")

with open('create_nodes.cypher', 'r') as f:
    node_queries = f.readlines()

with open('create_relationships.cypher', 'r') as f:
    relationship_queries = f.readlines()

check_execute = input("Deseja executar as queries? (s/n)")
if check_execute == "s":
    execute_queries(node_queries)
    execute_queries(relationship_queries)
