from faker import Faker
import uuid
import random

fake = Faker()

subjects = ["Calculus", "Linear Algebra", "Programming", "Data Structures", "Algorithms", "Databases", "Networks", "Operating Systems", "Artificial Intelligence", "Machine Learning"]

def generate_student_queries():
    queries = []
    for _ in range(10):
        student_id = uuid.uuid4()
        name = fake.name().replace("'", "''")
        course_id = uuid.uuid4()
        
        completed_subjects = {
            random.choice(subjects): (random.randint(1, 2), random.randint(2019, 2023), round(random.uniform(5.0, 10.0), 2))
            for _ in range(3)
        }
        
        completed_subjects_str = '{' + ', '.join(
            f"'{subject}': ({semester}, {year}, {grade})"
            for subject, (semester, year, grade) in completed_subjects.items()
        ) + '}'
        
        query = f"INSERT INTO students (student_id, name, course_id, completed_subjects) VALUES ({student_id}, '{name}', {course_id}, {completed_subjects_str});"
        queries.append(query)
    
    with open("students_queries.cql", "w") as f:
        f.write("\n".join(queries))
        
def generate_professor_queries():
    queries = []
    for _ in range(5):
        professor_id = uuid.uuid4()
        name = fake.name().replace("'", "''")
        department_id = uuid.uuid4()
        
        taught_subjects = {
            random.choice(subjects): (random.randint(1, 2), random.randint(2019, 2023))
            for _ in range(3)
        }
        
        taught_subjects_str = '{' + ', '.join(
            f"'{subject}': ({semester}, {year})"
            for subject, (semester, year) in taught_subjects.items()
        ) + '}'
        
        query = f"INSERT INTO professors (professor_id, name, department_id, taught_subjects) VALUES ({professor_id}, '{name}', {department_id}, {taught_subjects_str});"
        queries.append(query)

    with open("professors_queries.cql", "w") as f:
        f.write("\n".join(queries))

def generate_department_queries():
    queries = []
    for _ in range(3):
        department_id = uuid.uuid4()
        name = fake.company().replace("'", "''")  # Escape single quotes
        head_professor_id = uuid.uuid4()
        
        query = f"INSERT INTO departments (department_id, name, head_professor_id) VALUES ({department_id}, '{name}', {head_professor_id});"
        queries.append(query)
    
    with open("departments_queries.cql", "w") as f:
        f.write("\n".join(queries))

def generate_graduated_student_queries():
    queries = []
    for _ in range(5):
        year = random.randint(2019, 2023)
        semester = random.randint(1, 2)
        student_id = uuid.uuid4()
        name = fake.name().replace("'", "''")  # Escape single quotes
        
        query = f"INSERT INTO graduated_students (year, semester, student_id, name) VALUES ({year}, {semester}, {student_id}, '{name}');"
        queries.append(query)
    
    with open("graduated_students_queries.cql", "w") as f:
        f.write("\n".join(queries))

def generate_project_group_queries():
    queries = []
    for _ in range(3):
        group_id = uuid.uuid4()
        professor_id = uuid.uuid4()
        members = [str(uuid.uuid4()) for _ in range(2)]
        
        # Convert members list to a CQL list format
        members_str = '[' + ', '.join(members) + ']'
        
        query = f"INSERT INTO project_groups (group_id, professor_id, members) VALUES ({group_id}, {professor_id}, {members_str});"
        queries.append(query)
    
    with open("project_groups_queries.cql", "w") as f:
        f.write("\n".join(queries))

def generate_all_queries():
    generate_student_queries()
    generate_professor_queries()
    generate_department_queries()
    generate_graduated_student_queries()
    generate_project_group_queries()

def execute_queries_from_file(file_path, execute=False):
    if execute:
        from cassandra.cluster import Cluster
        from cassandra.auth import PlainTextAuthProvider

        # Configurações do AstraDB (substitua pelos seus detalhes)
        ASTRA_DB_CLIENT_ID = "BnKifOUoMvkwTEyNjNcGFZMJ"
        ASTRA_DB_CLIENT_SECRET = "de0bhWsg5K7F9XcXq7PRpHXrvRnhLUU,GMa3uEkKOayghWi3zrK68wDISyfCGxGTXZ,Di9zv4ybpiMO6HHkguoSrzQey+5hFZWqPoxM-DKWRnCaPt+2mrExcl3JmskBU"
        ASTRA_DB_SECURE_BUNDLE_PATH = "https://datastax-cluster-config-prod.s3.us-east-2.amazonaws.com/fb9d4960-1514-4f4e-bffe-2c090e14843a-1/secure-connect-projetodb.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2AIQRQ76XML7FLD6%2F20241106%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20241106T224513Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=69c67b9e5b4dd52f024a21feb80fbe07c2dd7cad0776e8228a106a90757d2acb"

        auth_provider = PlainTextAuthProvider(
            username=ASTRA_DB_CLIENT_ID, password=ASTRA_DB_CLIENT_SECRET
        )
        cluster = Cluster(cloud={'secure_connect_bundle': ASTRA_DB_SECURE_BUNDLE_PATH}, auth_provider=auth_provider)
        session = cluster.connect()

        with open(file_path, "r") as f:
            for query in f:
                session.execute(query.strip())
        
        print(f"Queries from {file_path} executed successfully.")
        cluster.shutdown()
    else:
        print(f"File {file_path} created with queries. To execute, set 'execute=True'.")

# Gerar e salvar todas as queries em arquivos
generate_all_queries()

# Exemplo de execução: Se quiser executar, chame a função com `execute=True`
# execute_queries_from_file("students_queries.cql", execute=True)
