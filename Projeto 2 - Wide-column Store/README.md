# Projeto 2 - Wide-Column Store (DataStax Astra)

Este README descreve como configurar e executar o projeto 2, que utiliza o DataStax Astra como wide-column store.

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
