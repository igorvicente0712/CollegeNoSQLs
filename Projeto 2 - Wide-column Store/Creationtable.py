from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import key

def get_astra_session():
    cloud_config = {
        'secure_connect_bundle': 'D:/secure-connect-projetodb.zip' 
    }
    auth_provider = PlainTextAuthProvider('key.clientId', 'key.secret')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect('fei') # Conectar ao keyspace "fei" 
    return session

def create_tables(session):
    session.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id_aluno uuid PRIMARY KEY,
            nome text,
            id_curso uuid,
            id_disciplina uuid,
            disciplinas_concluidas map<text, frozen<tuple<int, int, float>>>
        )
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS professor (
            id_professor uuid PRIMARY KEY,
            nome text,
            id_departamento uuid,
            disciplinas_ministradas map<text, frozen<tuple<int, int>>>
        )
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS departamento (
            id_departamento uuid PRIMARY KEY,
            nome text,
            id_chefe_departamento uuid,
            disciplinas set<text>
        )
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS alunos_formado (
            ano int,
            semestre int,
            id_aluno uuid,
            nome text,
            PRIMARY KEY ((ano, semestre), id_aluno)
        ) WITH CLUSTERING ORDER BY (id_aluno ASC)
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS grupo_proj (
            id_grupo uuid PRIMARY KEY,
            id_professor uuid,
            membros list<uuid>
        )
    """)

if __name__ == "__main__":
    session = get_astra_session()
    create_tables(session)
    print("Tables created successfully!")
    session.cluster.shutdown()  
