# Projeto 1 - Document Store 

Esta pasta apresenta o Projeto 1 - Document Store, realizado em MongoDB. Nela, é possível encontrar:

gera_dados_doc_store.py - Código em Python para geração de dados fictícios, criação de arquivos JSON para a inserção e, caso o usuário desejar, execução direta no banco de dados.

query_*.js - 5 arquivos contendo as 5 consultas para relatórios exigidas nas especificações do projeto.

*.json - Arquivos json com dados para a inserção no banco de dados.

<h2>Integrantes</h2>

```json
[
  {
    "Nome": "Yuri Bykoff",
    "RA": "22.121.045-3"
  },
  {
    "Nome": "Daniel Eiji Osato Yoshida",
    "RA": "22.121.131-1"
  },
  {
    "Nome": "Igor Vicente Cutalo",
    "RA": "22.123.062-6"
  },
  {
    "Nome": "Arthur Veloso",
    "RA": "22.221.038-7"
  }
]
```

<h2>Dependências</h2>

```
Python
faker
mongopy
```

Um Cluster no MongoDB (https://www.mongodb.com/) para carregar os dados.

<h2>Instruções</h2>

Após a instalação das dependêcias, além de criar um banco de dados no MongoDB, basta executar o código gera_dados_doc_store.py que serão criados os arquivos JSON para a inserção manual na interface ou shell do MongoDB.

Para execução automática, basta alterar no código as variáveis uri, onde será apresentado um prompt para input do usuário (s/n).

No código, é possível alterar as variáveis constantes (letra maiúscula) para alterar os números de nodes e assim testar com um número maior ou menor de dados.

Para a execução das queries para relatórios, basta realizar a execução no shell ou, caso esteja usando interface gráfica no browser ou através do MongoDB Compass, basta acessar o banco de dados, selecionar a coleção que será utilizada para a query e executar após remover "db.COLLECTIONNAME.aggregate" do início.

<h2>Modelo de dados</h2>

A ideia original segue, onde temos:

Estrutura JSON para alunos

```
{
  "_id": "1234567",
  "nome": "Nome do Aluno",
  "curso": "12345",
  "disciplinas": [
    {
      "codigo": "123456",
      "ano": 2022,
      "semestre": 1,
      "nota": 8.5
    },
    {
      "codigo": "654321",
      "ano": 2023,
      "semestre": 2,
      "nota": 7.0
    }
  ],
  "tcc": {
    "grupo_id": "123",
    "orientador": "54321"
  }
}
```

Estrutura JSON para professores

```
{
  "_id": "54321",
  "nome": "Nome do Professor",
  "disciplinas": [
    {
      "codigo": "123456",
      "ano": 2022,
      "semestre": 1
    },
    {
      "codigo": "654321",
      "ano": 2023,
      "semestre": 2
    }
  ],
  "departamento": "1234"
}
```

Estrutura JSON para cursos

```
{
  "_id": "12345",
  "nome": "Nome do Curso",
  "disciplinas": [
    "123456",
    "654321"
  ]
}
```

Estrutura JSON para departamentos

```
{
  "_id": "1234",
  "nome": "Nome do Departamento",
  "chefe": "54321"
}
```

Estrutura JSON para disciplinas

```
{
  "_id": "123456",
  "nome": "Nome da Disciplina",
  "departamento": "1234"
}
```

Estrutura JSON para grupos_tcc

```
{
  "_id": "123",
  "ano": 2023,
  "semestre": 1,
  "alunos": [
    {
      "_id": "1234567",
      "nome": "Nome do Aluno"
    },
    {
      "_id": "7654321",
      "nome": "Nome do Aluno 2"
    }
  ],
  "orientador": "54321"
}
```
