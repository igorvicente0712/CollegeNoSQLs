# Projeto 2 - Wide-Column Store (DataStax Astra)

Este projeto utiliza o DataStax Astra, um serviço de database totalmente gerenciado baseado no Apache Cassandra, para construir um banco de dados NoSQL do tipo wide-column store.  Esta seção descreve brevemente o DataStax Astra e o modelo de dados wide-column, destacando suas vantagens para este projeto.


**DataStax Astra:** É uma plataforma de banco de dados como serviço (DBaaS) que simplifica o processo de implantação, gerenciamento e dimensionamento de bancos de dados Cassandra.  Ele oferece alta disponibilidade, escalabilidade horizontal e tolerância a falhas, tornando-o ideal para aplicações que exigem alta performance e confiabilidade.  A escolha do Astra nesse projeto se justifica pela sua facilidade de uso, integração e escalabilidade sem a necessidade de gerenciamento de infraestrutura.


**Wide-Column Stores:**  Um banco de dados wide-column store, como o Apache Cassandra que embasa o DataStax Astra, difere dos bancos de dados relacionais tradicionais. Em vez de organizar dados em tabelas com linhas e colunas fixas, ele utiliza uma estrutura flexível de *colunas*.  Cada linha (ou "row") pode conter um número arbitrariamente grande de colunas, cada uma com seu próprio nome e valor.  As colunas não precisam existir previamente; elas são criadas dinamicamente conforme necessário.  Isso é particularmente vantajoso quando:

* **Dados são esparsos:**  Muitas colunas em uma linha podem ser vazias.  Um banco de dados relacional desperdiçaria espaço armazenando essas colunas vazias, enquanto um wide-column store somente armazena as colunas com valores.
* **Esquema é flexível:**  O esquema do banco de dados não precisa ser definido antecipadamente.  Novas colunas podem ser adicionadas facilmente sem a necessidade de alterar a estrutura da tabela.
* **Escalabilidade é crucial:** Wide-column stores são altamente escaláveis, permitindo o tratamento de grandes volumes de dados e alta concorrência de forma eficiente.

**Vantagens para o projeto:** Para este projeto específico, a escolha de um wide-column store, através do DataStax Astra, oferece as seguintes vantagens:

* **Escalabilidade:** A capacidade de escalar horizontalmente permite lidar com um volume crescente de dados e usuários sem perda de desempenho.
* **Flexibilidade:** A estrutura de colunas flexíveis facilita a adição de novos tipos de dados ou atributos à medida que o projeto evolui.
* **Desempenho:** A arquitetura distribuída e o design wide-column garantem alto desempenho em consultas de leitura e escrita.
* **Facilidade de gerenciamento:** O DataStax Astra abstrai a complexidade da infraestrutura, permitindo que a equipe se concentre no desenvolvimento do aplicativo.

Em resumo, o DataStax Astra, com seu modelo wide-column store, fornece uma solução robusta e escalável para os requisitos de armazenamento de dados deste projeto, facilitando o desenvolvimento e garantindo a confiabilidade e performance do sistema.

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

## Pré-requisitos

* Conta no DataStax Astra (astra.datastax.com)
* Python versão 3.8 ou inferior.
* `cassandra-driver` instalado via pip: `pip install cassandra-driver`  (Considere usar um ambiente virtual para isolar as dependências.)

## Configuração

1. **Criando o Database no DataStax Astra:**

   * Acesse o site do DataStax Astra e faça login ou crie uma conta.
   * Crie um novo Database:
     * Selecione "Serverless (Non-Vector)".
     * Nomeie o Database (ex: `faculdadedb`).
     * Nomeie o Keyspace (ex: `fei`).
     * Selecione uma região disponível.

2. **Obtendo o Secure Connect Bundle e Tokens:**

   * Na seção "Connect", selecione o driver Python e clique em "Download Bundle". Baixe o `secure-connect-projetodb.zip` e salve-o em um local de fácil acesso (ex: `D:/`).
   * Na seção "Tokens", clique em "Download" para obter o arquivo JSON contendo as credenciais (`clientId`, `secret`, `token`).  Este arquivo terá um formato semelhante a:

     ```json
     {
       "clientId": "token 1",
       "secret": "token 2",
       "token": "token 3"
     }
     ```

3. **Configurando os arquivos Python:**

   Substitua os placeholders nos arquivos `CreationTables.py`, `Inseridor.py` e `querys.py` com as informações obtidas:

   * **`secure_connect_bundle`:**  Defina o caminho completo para o arquivo `secure-connect-projetodb.zip`.  Exemplo: `'D:/secure-connect-projetodb.zip'`
   * **`auth_provider = PlainTextAuthProvider('token 1', 'token 2')`:** Substitua `'token 1'` e `'token 2'` pelos valores correspondentes do seu arquivo JSON de tokens.
   * **`session = cluster.connect('fei')`:** Certifique-se que o nome do keyspace esteja correto.

   **Exemplo de configuração em `CreationTables.py` (adapte para os outros arquivos):**

   ```python
   from cassandra.cluster import Cluster
   from cassandra.auth import PlainTextAuthProvider

   cloud_config = {
       'secure_connect_bundle': 'D:/secure-connect-projetodb.zip'
   }
   auth_provider = PlainTextAuthProvider('token 1', 'token 2')
   cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
   session = cluster.connect('fei')
   # ... resto do código ...
   ```

## Execução

1. **Criação das tabelas:** Execute `CreationTables.py`. Isso criará as tabelas necessárias no DataStax Astra.

2. **Geração e inserção de dados:** Execute `Gerador.py` para gerar os arquivos CQL de inserção. Em seguida, execute `Inseridor.py` para importar os dados para o DataStax Astra.

3. **Verificação dos dados:** Conecte-se ao console CQL do DataStax Astra e execute as seguintes queries para verificar a criação das tabelas e a inserção dos dados:

   ```cql
   USE fei;
   DESCRIBE TABLES;
   SELECT * FROM alunos;
   SELECT * FROM departamento;
   SELECT * FROM alunos_formado;
   SELECT * FROM grupo_proj;
   SELECT * FROM professor;
   ```

4. **Execução das queries:** Execute `querys.py` para executar as queries predefinidas.

## Solução de problemas

* **Erros de conexão:** Verifique as configurações do `secure_connect_bundle`, `clientId`, `secret` e o nome do keyspace.
* **Erros de instalação do driver:** Certifique-se de ter a versão correta do Python e use o `pip` corretamente.  Se houver problemas, tente instalar o driver manualmente a partir do diretório de instalação do Python.


Este README fornece uma guia completa para configurar e executar o projeto. Lembre-se de substituir os placeholders pelos seus valores reais.
