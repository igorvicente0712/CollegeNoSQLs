from faker import Faker
from neo4j import GraphDatabase
import random

fake = Faker('pt_BR')

with open(r"D:\GitHub\CollegeNoSQLs\Projeto 3 - Graph Database\Neo4j-5e9030ad-Created-2024-11-02.txt") as f:
    cred = f.read()

uri = cred.split("\n")[1]
uri = uri[uri.find("=") + 1:]

username = cred.split("\n")[2]
username = username[username.find("=") + 1:]

password = cred.split("\n")[3]
password = password[password.find("=") + 1:]

driver = GraphDatabase.driver(uri, auth=(username, password))

# Função para gerar dados fictícios
def gera_dados():
    dados = {
        'departamentos': [],
        'professores': [],
        'cursos': [],
        'alunos': [],
        'grupos': []
    }

    # Criar departamentos
    for _ in range(3):
        dept_id = fake.uuid4()
        depts = fake.company()
        dados['departamentos'].append({'dept_id': dept_id, 'nome': depts})

    # Criar professores e associá-los a departamentos
    for _ in range(5):
        prof_id = fake.uuid4()
        profs = fake.name()
        dept_id = random.choice(dados['departamentos'])['dept_id']
        dados['professores'].append({'prof_id': prof_id, 'nome': profs, 'dept_id': dept_id})

    # Criar cursos e matrizes curriculares
    for _ in range(3):
        curso_id = fake.uuid4()
        cursos = fake.job()
        dados['cursos'].append({'curso_id': curso_id, 'nome': cursos})

        # Criar disciplinas e associar ao curso
        for _ in range(5):
            disc_id = fake.uuid4()
            disciplinas = fake.bs().capitalize()
            semestre = random.choice(['1', '2'])
            ano = random.randint(2019, 2023)
            dados['cursos'][-1].setdefault('disciplinas', []).append({
                'disc_id': disc_id, 'nome': disciplinas,
                'codigo': f'S{random.randint(100, 999)}',
                'semestre': semestre, 'ano': ano
            })

    # Criar alunos e matrículas
    for _ in range(10):
        aluno_id = fake.uuid4()
        alunos = fake.name()
        curso_id = random.choice(dados['cursos'])['curso_id']
        dados['alunos'].append({'aluno_id': aluno_id, 'nome': alunos, 'curso_id': curso_id})

        # Associar disciplinas cursadas pelo aluno
        for _ in range(3):
            disc_id = fake.uuid4()
            semestre = random.choice(['1', '2'])
            ano = random.randint(2019, 2023)
            notas = round(random.uniform(5.0, 10.0), 2)
            dados['alunos'][-1].setdefault('discs_completas', []).append({
                'disc_id': disc_id, 'semestre': semestre, 'ano': ano, 'nota': notas
            })

    # Criar grupos de TCC e orientadores
    for _ in range(3):
        grupo_id = fake.uuid4()
        professor = random.choice(dados['professores'])
        dados['grupos'].append({'grupo_id': grupo_id, 'prof_id': professor['prof_id']})

        # Associar alunos ao grupo de TCC
        for _ in range(2):
            aluno_id = random.choice(dados['alunos'])['aluno_id']
            dados['grupos'][-1].setdefault('membros', []).append(aluno_id)

    return dados

# Função para escrever queries em um arquivo
def write_queries_to_file(dados, filename="queries.cypher"):
    with open(filename, 'w', encoding='utf-8') as file:
        # Criar departamentos
        for dept in dados['departamentos']:
            file.write(f"CREATE (:Departamento {{dept_id: '{dept['dept_id']}', nome: '{dept['nome']}'}});\n")
        file.write("\n")
        # Criar professores e associar a departamentos
        for prof in dados['professores']:
            file.write(f"MATCH (d:Departamento {{dept_id: '{prof['dept_id']}'}}) "
                       f"CREATE (p:Professor {{prof_id: '{prof['prof_id']}', nome: '{prof['nome']}'}})-[:CHEFIA]->(d);\n")
        file.write("\n")
        # Criar cursos e matrizes curriculares
        for curso in dados['cursos']:
            file.write(f"CREATE (:Curso {{curso_id: '{curso['curso_id']}', nome: '{curso['nome']}'}});\n")
            for disc in curso.get('disciplinas', []):
                file.write(f"MATCH (c:Curso {{curso_id: '{curso['curso_id']}'}}) "
                           f"CREATE (dis:Disciplina {{disc_id: '{disc['disc_id']}', nome: '{disc['nome']}', "
                           f"codigo: '{disc['codigo']}', semestre: '{disc['semestre']}', ano: {disc['ano']}}}) "
                           f"CREATE (c)-[:TEM_NO_CURRICULO]->(dis);\n")
        file.write("\n")
        # Criar alunos e matrículas
        for aluno in dados['alunos']:
            file.write(f"CREATE (a:Aluno {{aluno_id: '{aluno['aluno_id']}', nome: '{aluno['nome']}'}}) "
                       f"WITH a MATCH (c:Curso {{curso_id: '{aluno['curso_id']}'}}) "
                       f"CREATE (a)-[:MATRICULOU_EM]->(c);\n")
            for disc in aluno.get('discs_completas', []):
                file.write(f"MATCH (a:Aluno {{aluno_id: '{aluno['aluno_id']}'}}) "
                           f"MATCH (dis:Disciplina {{disc_id: '{disc['disc_id']}'}}) "
                           f"CREATE (a)-[:COMPLETOU {{semestre: '{disc['semestre']}', ano: {disc['ano']}, nota: {disc['nota']}}}]->(dis);\n")
        file.write("\n")
        # Criar grupos de TCC e orientadores
        for grupo in dados['grupos']:
            file.write(f"CREATE (g:GrupoProjeto {{grupo_id: '{grupo['grupo_id']}'}}) "
                       f"WITH g MATCH (p:Professor {{prof_id: '{grupo['prof_id']}'}}) "
                       f"CREATE (g)-[:ORIENTADO_POR]->(p);\n")
            for member_id in grupo.get('membros', []):
                file.write(f"MATCH (a:Aluno {{aluno_id: '{member_id}'}}) "
                           f"MATCH (g:GrupoProjeto {{grupo_id: '{grupo['grupo_id']}'}}) "
                           f"CREATE (s)-[:PARTE_DO_GRUPO]->(g);\n")

# Função para executar queries diretamente no Neo4J
def execute_queries_in_neo4j(dados):
    with driver.session() as session:
        # Função auxiliar para executar uma query
        def execute_query(query, params=None):
            session.run(query, params or {})

        # Criar departamentos, professores, cursos, alunos, e grupos de TCC com as mesmas queries acima,
        # usando `execute_query(query, params)` no lugar de `file.write(...)`

# Gerar dados, salvar em arquivo e/ou executar no Neo4J
dados = gera_dados()
write_queries_to_file(dados)
# execute_queries_in_neo4j(dados)
