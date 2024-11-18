// Aqui estão as queries para relatórios utilizando exemplos com os dados gerados pela última vez, encontrados nos arquivos na mesma pasta com nome create_nodes.cypher e create_relationships.cypher

// 1. Histórico escolar de qualquer aluno
MATCH (aluno:Aluno {matricula: '6698461'})-[r:CURSOU]->(disciplina:Disciplina)
RETURN disciplina.codigo, disciplina.nome, r.semestre, r.ano, r.nota
ORDER BY r.ano, r.semestre;

// 2. Histórico de disciplinas ministradas por qualquer professor
MATCH (professor:Professor {id_professor: '45183'})-[r:MINISTRA]->(disciplina:Disciplina)
RETURN disciplina.codigo, disciplina.nome, r.semestre, r.ano
ORDER BY r.ano, r.semestre;

// 3. Listar alunos que já se formaram em um ano semestre
// Dado a aleatoriedade da geração de dados e número de critérios, talvez não seja possível ver exemplos no banco em si... Mas em teoria funciona
MATCH (aluno:Aluno)-[r:CURSOU]->(disciplina:Disciplina)
WHERE (r.ano = 2024 AND r.semestre = 1) OR (r.ano < 2024) AND r.nota >= 5.0 // Exemplo para quem se formou até o primeiro semestre de 2024, inclusivo. Para o ano inteiro, deixar só a nota e "r.ano <= 20YY"
WITH aluno, collect(disciplina) as disciplinas_cursadas
MATCH (curso:Curso)-[:TEM]->(disciplina:Disciplina)
WITH aluno, curso, disciplinas_cursadas, collect(disciplina) as disciplinas_do_curso
WHERE size(disciplinas_cursadas) = size(disciplinas_do_curso)
RETURN aluno.nome, aluno.matricula;

// 4. Listar todos os professores que são chefes de departamento
MATCH (professor:Professor)-[:CHEFIA]->(departamento:Departamento)
RETURN professor.nome, departamento.nome;

// 5. Saber quais alunos formaram um grupo de TCC e qual professor foi o orientador
MATCH (grupo:GrupoTCC)-[:ORIENTA]-(professor:Professor),
      (aluno:Aluno)-[:PARTICIPA]->(grupo)
RETURN grupo.ano, grupo.semestre, professor.nome AS orientador, collect(aluno.nome) AS alunos;