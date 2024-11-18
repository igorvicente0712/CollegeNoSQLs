import uuid
import random

from faker import Faker


fake = Faker('pt_BR')

disciplinas = ["Cálculo I", "Álgebra Linear", "Complexidade de Algoritmo", "Computação Grafica", "CC6240", "Compilador",
                "Banco de Dados", "Redes de Computadores","Software orientado a objetos","Sistemas Operacionais"]
departamentos_ids = []
alunos_ids = []
professor_ids = []


def generate_insert_statements(num_alunos=25, num_professores=8, num_departamentos=5, num_alunos_formados=20, num_grupos=4):

    alunos_inserts = []
    professores_inserts = []
    departamentos_inserts = []
    alunos_formados_inserts = []
    grupo_proj_inserts = []

    # --- Alunos ---
    for _ in range(num_alunos):
        id_aluno = uuid.uuid4()
        alunos_ids.append(id_aluno)  # Armazena os IDs dos alunos
        nome = fake.name()
        id_curso = uuid.uuid4()
        id_disciplina = uuid.uuid4()

        disciplinas_concluidas = {}
        num_disciplinas_concluidas = random.randint(1, len(disciplinas))
        for _ in range(num_disciplinas_concluidas):
            disciplina = random.choice(disciplinas)
            semestre = random.randint(1, 8)
            ano = random.randint(2018, 2024)
            nota = round(random.uniform(0, 10), 2)
            disciplinas_concluidas[disciplina] = (semestre, ano, nota)

        alunos_inserts.append(
            f"INSERT INTO alunos (id_aluno, nome, id_curso, id_disciplina, disciplinas_concluidas) VALUES ({id_aluno}, '{nome}', {id_curso}, {id_disciplina}, {disciplinas_concluidas});"
        )

    # --- Departamentos ---
    for _ in range(num_departamentos):
        id_departamento = uuid.uuid4()
        departamentos_ids.append(id_departamento)
        id_chefe_departamento = uuid.uuid4()  
        nome_departamento = fake.company()
        departamento_disciplinas = random.sample(disciplinas, 1) 
        disciplinas_str = ','.join([f"'{d}'" for d in departamento_disciplinas])
        departamentos_inserts.append(
            f"INSERT INTO departamento (id_departamento, id_chefe_departamento, nome, disciplinas) "
            f"VALUES ({id_departamento}, {id_chefe_departamento}, '{nome_departamento}', {{ {disciplinas_str} }});"
        )

    # --- Professores ---
    for _ in range(num_professores):
        id_professor = uuid.uuid4()
        professor_ids.append(id_professor) 
        nome = fake.name()
        id_departamento = random.choice(departamentos_ids)
        disciplinas_ministradas = {}
        num_disciplinas_ministradas = random.randint(1, len(disciplinas))
        for _ in range(num_disciplinas_ministradas):
            disciplina = random.choice(disciplinas)
            semestre = random.randint(1, 2)
            ano = random.randint(2018, 2024)
            disciplinas_ministradas[disciplina] = (semestre, ano)

        professores_inserts.append(
            f"INSERT INTO professor (id_professor, disciplinas_ministradas, id_departamento, nome) "
            f"VALUES ({id_professor}, {disciplinas_ministradas}, {id_departamento}, '{nome}');"
        )

    # --- Alunos Formados ---
    for _ in range(num_alunos_formados):
        ano = random.randint(2020, 2024)
        semestre = random.randint(1, 2)
        id_aluno = random.choice(alunos_ids)  # Escolhe um ID de aluno da lista
        nome = fake.name()
        alunos_formados_inserts.append(
            f"INSERT INTO alunos_formado (ano, semestre, id_aluno, nome) VALUES ({ano}, {semestre}, {id_aluno}, '{nome}');"
        )

    # --- Grupo Proj ---
    for _ in range(num_grupos):
        id_grupo = uuid.uuid4()
        id_professor = random.choice(professor_ids)
        membros = random.sample(alunos_ids, random.randint(2, 5))
        membros_str = '[' + ', '.join([str(membro) for membro in membros]) + ']'

        grupo_proj_inserts.append(
            f"INSERT INTO grupo_proj (id_grupo, id_professor, membros) VALUES ({id_grupo}, {id_professor}, {membros_str});"
        )

    return (
        alunos_inserts,
        professores_inserts,
        departamentos_inserts,
        alunos_formados_inserts,
        grupo_proj_inserts,
    )


def save_to_cql_files(alunos, professores, departamentos, formados, grupos):
    def write_to_file(filename, queries):
        with open(filename, 'w', encoding='utf-8') as f:
            for query in queries:
                f.write(query + '\n')

    write_to_file('1alunos.cql', alunos)
    write_to_file('1professores.cql', professores)
    write_to_file('1departamentos.cql', departamentos)
    write_to_file('1alunos_formados.cql', formados)
    write_to_file('1grupo_proj.cql', grupos)


alunos, professores, departamentos, formados, grupos = generate_insert_statements()
save_to_cql_files(alunos, professores, departamentos, formados, grupos)
