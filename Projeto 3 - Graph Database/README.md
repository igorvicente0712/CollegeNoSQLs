# Projeto 3 - Graph Database

![image](https://github.com/user-attachments/assets/38fce547-ba19-486d-9b45-e7f218884f29)


Esta pasta apresenta o Projeto 3 - Graph Database, realizado em Neo4J. Nela, é possível encontrar:

gera_dados_grafos.py - Código em Python para geração de dados fictícios, criação de arquivos com as queries de criação e, caso o usuário desejar, execução direta no banco de dados.

queries_consulta_grafos.cypher - Arquivo contendo as 5 consultas para relatórios exigidas nas especificações do projeto, contendo comentários caso hajam pontos de atenção para a execução.

create_nodes.cypher - Arquivo com os dados de nodes gerados pela última vez para o teste.

create_relationships.cypher - Arquivo com os dados de relações gerados pela última vez para o teste.

<h2>Dependências</h2>

```
Python
faker
neo4j
```
Uma instância no Neo4J (https://neo4j.com/) para carregar os dados.

<h2>Instruções</h2>

Após a instalação das dependêcias, basta executar o código gera_dados_grafos.py que dois arquivos serão criados para a execução manual na interface do Neo4J.

Para execução automática, basta alterar no código as variáveis uri, user e password, onde será apresentado um prompt para input do usuário (s/n).

No código, é possível alterar as variáveis constantes (letra maiúscula) para alterar os números de nodes e assim testar com um número maior ou menor de dados.

<h2>Modelo de dados</h2>

A ideia original segue, onde temos:

```

Nodes
  Aluno: (nome,matricula)
  Professor: (nome,id_professor)
  Curso: (nome,codigo)
  Departamento: (nome,codigo)
  Disciplina: (nome,codigo)
  GrupoTCC: (ano,semestre)

Relações e Propriedades
  Aluno -[:CURSA]-> Curso
  Aluno -[:CURSOU]-> Disciplina: (ano,semestre,nota) 
  Professor -[:MINISTRA]-> Disciplina: (ano,semestre)
  Professor -[:CHEFIA]-> Departamento 
  Disciplina -[:PERTENCE]-> Departamento
  Curso -[:TEM]-> Disciplina
  Aluno -[:PARTICIPA]-> GrupoTCC
  Professor -[:ORIENTA]-> GrupoTCC
```
