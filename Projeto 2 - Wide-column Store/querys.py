from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def get_astra_session():
    cloud_config = {
        'secure_connect_bundle': 'D:/secure-connect-projetodb.zip'
    }
    auth_provider = PlainTextAuthProvider('ZDemCUxMGyWMhnryqfatkmrg', 'y9XZp9xXE6M82MJrobYFF6gZQNxCnjzWC2xs,ZemZ0GLUU5pFZ42m5fwT8OR52rX+OlznFx_nD+1yCx1UmAaWLZz4oBpsHvhDuNdo-IId+irWBYOySa2DotCFRZiom_D')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect('fei')
    return session


def obter_e_salvar_historico_escolar(session, nome_arquivo="Query1.txt"):
    query = "SELECT id_aluno, nome, disciplinas_concluidas, id_curso, id_disciplina FROM alunos" # Corrigido nome da tabela e query
    result = session.execute(query)

    with open(nome_arquivo, 'w') as arquivo:
        for row in result:
            arquivo.write(f"Aluno: {row.nome} (ID: {row.id_aluno})\n") # id_aluno incluído
            arquivo.write(f"Curso: {row.id_curso} \n") # id_curso incluído

            if row.disciplinas_concluidas: # Verifica se o dicionário está vazio
                arquivo.write("Disciplinas Concluídas:\n")
                for disciplina, dados in row.disciplinas_concluidas.items():
                    semestre, ano, nota = dados  # Desempacota os dados da disciplina
                    nota_formatada = "{:.2f}".format(nota)
                    arquivo.write(f"  - {disciplina} (ID: {row.id_disciplina}): Semestre {semestre}/{ano}, Nota: {nota_formatada}\n")
            else:
                arquivo.write("Nenhuma disciplina concluída.\n")

            arquivo.write("-" * 20 + "\n")

def obter_e_salvar_historico_professor(session, nome_arquivo="Query2.txt"):
    query = "SELECT id_professor, nome, disciplinas_ministradas, id_departamento FROM professor"
    result = session.execute(query)

    with open(nome_arquivo, 'w') as arquivo:
        for row in result:
            arquivo.write(f"Professor: {row.nome} (ID: {row.id_professor})\n")
            arquivo.write(f"Departamento: {row.id_departamento}\n")

            if row.disciplinas_ministradas:
                arquivo.write("Disciplinas Ministradas:\n")
                for disciplina, dados in row.disciplinas_ministradas.items():
                    semestre, ano = dados # Desempacota semestre e ano
                    arquivo.write(f"  - {disciplina}: Semestre {semestre}/{ano}\n")
            else:
                arquivo.write("Nenhuma disciplina ministrada.\n")

            arquivo.write("-" * 20 + "\n")

def alunos_por_semestre_e_nota(session, semestre, nota_minima, nome_arquivo="Query3.txt"):
    query = "SELECT id_aluno, nome, disciplinas_concluidas FROM alunos"
    result = session.execute(query)

    alunos_selecionados = []

    for row in result:
        disciplinas_aprovadas = {}
        if row.disciplinas_concluidas:
            for disciplina, dados in row.disciplinas_concluidas.items():
                s, ano, nota = dados
                if s == semestre and nota >= nota_minima:
                    disciplinas_aprovadas[disciplina] = (s, ano, nota)

        if disciplinas_aprovadas:
            alunos_selecionados.append({
                "id_aluno": row.id_aluno,
                "nome": row.nome,
                "disciplinas_aprovadas": disciplinas_aprovadas
            })

    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos_selecionados:
            arquivo.write(f"Aluno: {aluno['nome']} (ID: {aluno['id_aluno']})\n")
            arquivo.write(f"Disciplinas Aprovadas (Semestre {semestre}, Nota mínima {nota_minima}):\n")
            for disciplina, dados in aluno['disciplinas_aprovadas'].items():
                s, ano, nota = dados
                nota_formatada = "{:.2f}".format(nota)
                arquivo.write(f"  - {disciplina}: Semestre {s}/{ano}, Nota: {nota_formatada}\n")
            arquivo.write("-" * 20 + "\n")


def listar_chefes_e_disciplinas(session, nome_arquivo="Query4.txt"):
    query_dep = "SELECT id_departamento, id_chefe_departamento, nome, disciplinas FROM departamento"
    query_prof = "SELECT id_professor, nome FROM professor"

    departamentos = session.execute(query_dep)
    professores = session.execute(query_prof)

    #cria um dicionário para busca rápida de professores pelo id
    prof_dict = {row.id_professor: row.nome for row in professores}


    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Chefes de Departamento e suas Disciplinas:\n")
        for dep in departamentos:
            arquivo.write(f"Departamento: {dep.nome} (ID: {dep.id_departamento})\n")
            if dep.id_chefe_departamento in prof_dict: #verifica se o chefe existe na tabela de professores
                arquivo.write(f"Chefe: {prof_dict[dep.id_chefe_departamento]}\n")
            else:
                arquivo.write(f"Chefe: ID {dep.id_chefe_departamento}. \n")

            if dep.disciplinas:
                arquivo.write("Disciplinas:\n")
                for disciplina in dep.disciplinas:
                    arquivo.write(f"  - {disciplina}\n")
            else:
                arquivo.write("Nenhuma disciplina associada a este departamento.\n")
            arquivo.write("-" * 20 + "\n")

def alunos_e_orientadores_tcc(session, nome_arquivo="Query5.txt"):
    query_grupos = "SELECT id_grupo, id_professor, membros FROM grupo_proj"
    query_professores = "SELECT id_professor, nome FROM professor"
    query_alunos = "SELECT id_aluno, nome FROM alunos"

    grupos = session.execute(query_grupos)
    professores = session.execute(query_professores)
    alunos = session.execute(query_alunos)


    #cria dicionários para acesso rápido
    prof_dict = {row.id_professor: row.nome for row in professores}
    aluno_dict = {row.id_aluno: row.nome for row in alunos}

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Grupos de TCC, Alunos e Orientadores:\n")
        for grupo in grupos:
            arquivo.write(f"Grupo: {grupo.id_grupo}\n")
            if grupo.id_professor in prof_dict:
                arquivo.write(f"Orientador: {prof_dict[grupo.id_professor]} (ID: {grupo.id_professor})\n")
            else:
                arquivo.write(f"Orientador: ID {grupo.id_professor} não encontrado.\n")

            arquivo.write("Alunos:\n")
            if grupo.membros:
                for aluno_id in grupo.membros:
                    if aluno_id in aluno_dict:
                        arquivo.write(f"  - {aluno_dict[aluno_id]} (ID: {aluno_id})\n")
                    else:
                        arquivo.write(f"  - Aluno ID {aluno_id} não encontrado.\n")
            else:
                arquivo.write("  - Nenhum aluno encontrado neste grupo.\n")

            arquivo.write("-" * 20 + "\n")



if __name__ == "__main__":
    session = get_astra_session()
    # Obter histórico escolar de todos os alunos (Query1)
    obter_e_salvar_historico_escolar(session)
    print("Histórico escolar dos alunos salvo em Query1.txt")

    # Obter histórico de disciplinas ministradas pelos professores (Query2 - assumindo que você tenha essa função)
    obter_e_salvar_historico_professor(session) # Certifique-se que esta função esteja definida
    print("Histórico de disciplinas ministradas pelos professores salvo em Query2.txt")

    # Obter alunos por semestre e nota (Query3)
    semestre_escolhido = int(input("Informe o semestre (1-8): ")) #alterado a mensagem para o usuário
    while semestre_escolhido < 1 or semestre_escolhido > 8 : #alterado o critério de validação
        print("Semestre inválido. Digite um número entre 1 e 8.")
        semestre_escolhido = int(input("Informe o semestre (1-8): "))
    alunos_por_semestre_e_nota(session, semestre_escolhido, 5.0)
    print(f"Alunos do semestre {semestre_escolhido} com notas maiores ou iguais a 5.0 salvos em Query3.txt")
    # Obtem a lista de Professores quesão chefe de departamento

    listar_chefes_e_disciplinas(session)
    print("Informações sobre chefes de departamento salvas em Query4.txt")

    #Obtem a lista de Alunos que formaram um grupo de tcc e o professor orientador
    alunos_e_orientadores_tcc(session)
    print("Informações sobre grupos de TCC salvas em Query5.txt")