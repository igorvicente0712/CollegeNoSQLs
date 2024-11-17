-- OBS: Dada a natureza do CQL, join de múltiplas queries são feitos através do código

-- Obter e salvar historico escolar
SELECT id_aluno, nome, disciplinas_concluidas, id_curso, id_disciplina FROM alunos;

-- Obter e salvar historico professor
SELECT id_professor, nome, disciplinas_ministradas, id_departamento FROM professor;

-- Alunos por semestre e nota
SELECT id_aluno, nome, disciplinas_concluidas FROM alunos;

-- Listar chefes e disciplinas
SELECT id_departamento, id_chefe_departamento, nome, disciplinas FROM departamento;
SELECT id_professor, nome FROM professor;

-- Alunos e orientadores tcc
SELECT id_grupo, id_professor, membros FROM grupo_proj;
SELECT id_professor, nome FROM professor;
SELECT id_aluno, nome FROM alunos;
