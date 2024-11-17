CREATE (:Departamento {dept_id: 'a105083d-ece1-426b-bb29-68d3c9996131', nome: 'Santos Ltda.'});
CREATE (:Departamento {dept_id: 'db3817de-5909-4a67-a11a-8a65d0b23736', nome: 'Fernandes S/A'});
CREATE (:Departamento {dept_id: '46c9006d-b2c2-4c10-b21b-47f5e4ced417', nome: 'Nunes'});

MATCH (d:Departamento {dept_id: 'a105083d-ece1-426b-bb29-68d3c9996131'}) CREATE (p:Professor {prof_id: 'a3608834-ddeb-4522-82bd-db7a3fb61b20', nome: 'Maria Liz Teixeira'})-[:CHEFIA]->(d);
MATCH (d:Departamento {dept_id: '46c9006d-b2c2-4c10-b21b-47f5e4ced417'}) CREATE (p:Professor {prof_id: '6ecd0705-72ed-478c-82d1-a260ba82c8ae', nome: 'Dante Ribeiro'})-[:CHEFIA]->(d);
MATCH (d:Departamento {dept_id: '46c9006d-b2c2-4c10-b21b-47f5e4ced417'}) CREATE (p:Professor {prof_id: '01f0bc07-dfaf-410d-ade4-8f448c818141', nome: 'Ana Júlia Moraes'})-[:CHEFIA]->(d);
MATCH (d:Departamento {dept_id: 'a105083d-ece1-426b-bb29-68d3c9996131'}) CREATE (p:Professor {prof_id: 'c99965f5-1558-488b-a3e9-6df9e615145b', nome: 'Nicole Pacheco'})-[:CHEFIA]->(d);
MATCH (d:Departamento {dept_id: '46c9006d-b2c2-4c10-b21b-47f5e4ced417'}) CREATE (p:Professor {prof_id: '68b0d2b6-9809-42c8-a9e5-5321926c9f71', nome: 'Catarina Silveira'})-[:CHEFIA]->(d);

CREATE (:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0', nome: 'Clínico geral'});
MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (dis:Disciplina {disc_id: '7db0eada-d274-40ec-bc11-74dfc3265972', nome: 'Deliver ubiquitous functionalities', codigo: 'S999', semestre: '2', ano: 2021}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (dis:Disciplina {disc_id: '3a4c018f-e352-424c-980e-09acc27c6c66', nome: 'Target rich relationships', codigo: 'S630', semestre: '2', ano: 2020}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (dis:Disciplina {disc_id: 'e6a2a0d9-17ce-4b87-814f-2357caf666c4', nome: 'Benchmark leading-edge bandwidth', codigo: 'S785', semestre: '2', ano: 2022}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (dis:Disciplina {disc_id: '46fb8b3c-9d2a-4ffe-add4-5af8d83701b8', nome: 'Maximize best-of-breed technologies', codigo: 'S682', semestre: '2', ano: 2022}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (dis:Disciplina {disc_id: 'f522428e-4b84-4fae-bacc-56575d1ea62c', nome: 'Mesh seamless deliverables', codigo: 'S817', semestre: '1', ano: 2019}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
CREATE (:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647', nome: 'Jardineiro'});
MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (dis:Disciplina {disc_id: 'f52706c3-f6bb-4ac0-b568-275cf5bed823', nome: 'Cultivate wireless functionalities', codigo: 'S375', semestre: '1', ano: 2019}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (dis:Disciplina {disc_id: 'bfc6ea2a-b9c8-42d7-8585-2bf1757393ba', nome: 'Incentivize global solutions', codigo: 'S870', semestre: '1', ano: 2023}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (dis:Disciplina {disc_id: 'e3d69d93-b58a-4c66-84fc-585b18d96f78', nome: 'Integrate efficient channels', codigo: 'S709', semestre: '2', ano: 2023}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (dis:Disciplina {disc_id: '25c84578-cd6c-49c0-b146-e09131b2dae9', nome: 'Re-intermediate real-time e-markets', codigo: 'S596', semestre: '1', ano: 2022}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (dis:Disciplina {disc_id: 'a923c839-3a6d-44d1-bc47-687e2469d68d', nome: 'Matrix killer metrics', codigo: 'S178', semestre: '1', ano: 2023}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
CREATE (:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658', nome: 'Profissional de manutenção industrial'});
MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (dis:Disciplina {disc_id: '4870efaf-f6ca-46a7-ad75-5d67df583818', nome: 'Redefine transparent relationships', codigo: 'S972', semestre: '1', ano: 2020}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (dis:Disciplina {disc_id: '18d6dde9-d301-4d2f-90b9-bfe5bf35ce72', nome: 'Whiteboard enterprise users', codigo: 'S880', semestre: '2', ano: 2020}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (dis:Disciplina {disc_id: '06cc5010-d9e9-478a-8a77-ce7f270797b7', nome: 'Cultivate collaborative infrastructures', codigo: 'S411', semestre: '1', ano: 2021}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (dis:Disciplina {disc_id: 'f5e46c96-a89b-4590-9bdf-1cd92de7579c', nome: 'Empower user-centric architectures', codigo: 'S707', semestre: '2', ano: 2021}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);
MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (dis:Disciplina {disc_id: 'bb10a93d-ba53-4952-9236-631b543492e3', nome: 'Expedite proactive eyeballs', codigo: 'S564', semestre: '1', ano: 2022}) CREATE (c)-[:TEM_NO_CURRICULO]->(dis);

CREATE (a:Aluno {aluno_id: '11d8f579-c7e9-4c93-8d3f-67724afaf3b7', nome: 'Luna Melo'}) WITH a MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '11d8f579-c7e9-4c93-8d3f-67724afaf3b7'}) MATCH (dis:Disciplina {disc_id: 'a3b2ccdf-3ed6-4c5a-a470-22241f621460'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2023, nota: 8.91}]->(dis);
MATCH (a:Aluno {aluno_id: '11d8f579-c7e9-4c93-8d3f-67724afaf3b7'}) MATCH (dis:Disciplina {disc_id: '35341e23-3ed2-4a90-9aa1-bb45ef1104b4'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2019, nota: 9.64}]->(dis);
MATCH (a:Aluno {aluno_id: '11d8f579-c7e9-4c93-8d3f-67724afaf3b7'}) MATCH (dis:Disciplina {disc_id: 'fc8edaea-ec9c-4cd5-8cd9-1301f58ff742'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2019, nota: 7.56}]->(dis);
CREATE (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d', nome: 'Nathan Ribeiro'}) WITH a MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d'}) MATCH (dis:Disciplina {disc_id: 'bbc6f707-4c06-4201-a1a9-4805f18432b2'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2020, nota: 6.05}]->(dis);
MATCH (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d'}) MATCH (dis:Disciplina {disc_id: '0329348a-bec5-4b01-9627-154ae9f73155'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2022, nota: 7.17}]->(dis);
MATCH (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d'}) MATCH (dis:Disciplina {disc_id: '6a58622c-f747-4846-856c-e51bac8106ee'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2021, nota: 6.01}]->(dis);
CREATE (a:Aluno {aluno_id: '6506023a-c370-406e-8a82-875b2019eae2', nome: 'Brayan Freitas'}) WITH a MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '6506023a-c370-406e-8a82-875b2019eae2'}) MATCH (dis:Disciplina {disc_id: '4ddb8465-9b4f-42f4-bd22-5d01532e0b5d'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2022, nota: 6.74}]->(dis);
MATCH (a:Aluno {aluno_id: '6506023a-c370-406e-8a82-875b2019eae2'}) MATCH (dis:Disciplina {disc_id: '59339cc5-a654-4b44-9c1d-399b879eac04'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2019, nota: 6.9}]->(dis);
MATCH (a:Aluno {aluno_id: '6506023a-c370-406e-8a82-875b2019eae2'}) MATCH (dis:Disciplina {disc_id: 'b4e34255-e819-4577-ac52-07cd8830f7d6'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2022, nota: 5.09}]->(dis);
CREATE (a:Aluno {aluno_id: 'e39eb5de-c981-4e95-8d18-160026b29955', nome: 'Srta. Maya Mendes'}) WITH a MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: 'e39eb5de-c981-4e95-8d18-160026b29955'}) MATCH (dis:Disciplina {disc_id: '5fb188a5-a3dd-4231-aa3f-aa0d6b9111b2'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2023, nota: 6.57}]->(dis);
MATCH (a:Aluno {aluno_id: 'e39eb5de-c981-4e95-8d18-160026b29955'}) MATCH (dis:Disciplina {disc_id: 'eaa1182e-f945-44f2-bde6-8533c418b3a6'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2023, nota: 9.15}]->(dis);
MATCH (a:Aluno {aluno_id: 'e39eb5de-c981-4e95-8d18-160026b29955'}) MATCH (dis:Disciplina {disc_id: '3933a5f1-6080-47bb-9fd1-6faa946832d3'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2023, nota: 9.48}]->(dis);
CREATE (a:Aluno {aluno_id: 'da84953c-98ca-4815-a4d6-0ba84a57b253', nome: 'Isaque Nunes'}) WITH a MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: 'da84953c-98ca-4815-a4d6-0ba84a57b253'}) MATCH (dis:Disciplina {disc_id: 'f4027d49-c145-43d8-b31c-ca179ce29f40'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2019, nota: 9.82}]->(dis);
MATCH (a:Aluno {aluno_id: 'da84953c-98ca-4815-a4d6-0ba84a57b253'}) MATCH (dis:Disciplina {disc_id: 'f7d6502a-0cba-46c8-95af-0d474707229b'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2019, nota: 7.38}]->(dis);
MATCH (a:Aluno {aluno_id: 'da84953c-98ca-4815-a4d6-0ba84a57b253'}) MATCH (dis:Disciplina {disc_id: 'df903652-759f-4a15-b905-93eb556b4a32'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2021, nota: 9.19}]->(dis);
CREATE (a:Aluno {aluno_id: '1e207618-c362-4570-8e91-5830e7c71b38', nome: 'Davi Lucca Gonçalves'}) WITH a MATCH (c:Curso {curso_id: 'de49ab01-20b1-4a06-bdac-432fcc2151c0'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '1e207618-c362-4570-8e91-5830e7c71b38'}) MATCH (dis:Disciplina {disc_id: '9ad40961-6200-46ec-ae0c-a0b52cb0fded'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2022, nota: 8.86}]->(dis);
MATCH (a:Aluno {aluno_id: '1e207618-c362-4570-8e91-5830e7c71b38'}) MATCH (dis:Disciplina {disc_id: 'fc1cd70f-0984-49dd-8bdb-c34f535d9037'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2021, nota: 8.88}]->(dis);
MATCH (a:Aluno {aluno_id: '1e207618-c362-4570-8e91-5830e7c71b38'}) MATCH (dis:Disciplina {disc_id: 'f8b72da7-5450-40ed-af0c-84c8298272fe'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2020, nota: 6.66}]->(dis);
CREATE (a:Aluno {aluno_id: '9eed32d1-7bcd-4aee-95f3-3b341021c2ee', nome: 'Sra. Stephany Alves'}) WITH a MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '9eed32d1-7bcd-4aee-95f3-3b341021c2ee'}) MATCH (dis:Disciplina {disc_id: '7f27dea8-be82-4d2e-bf5a-fca58a4ffb3b'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2021, nota: 8.23}]->(dis);
MATCH (a:Aluno {aluno_id: '9eed32d1-7bcd-4aee-95f3-3b341021c2ee'}) MATCH (dis:Disciplina {disc_id: 'ebfc854e-7e6f-46a9-bc4b-4cfc2f6ffe67'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2021, nota: 5.05}]->(dis);
MATCH (a:Aluno {aluno_id: '9eed32d1-7bcd-4aee-95f3-3b341021c2ee'}) MATCH (dis:Disciplina {disc_id: '256efef1-80b5-4443-8e14-94ae2d511716'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2021, nota: 5.46}]->(dis);
CREATE (a:Aluno {aluno_id: '69677a3a-b74c-48a0-badf-d5bd2d741fda', nome: 'Yuri Farias'}) WITH a MATCH (c:Curso {curso_id: '80efc224-4fe3-4896-b15a-dbb1618b9658'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '69677a3a-b74c-48a0-badf-d5bd2d741fda'}) MATCH (dis:Disciplina {disc_id: '45190ec0-16ed-4596-83e4-18a7d85c6978'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2022, nota: 9.82}]->(dis);
MATCH (a:Aluno {aluno_id: '69677a3a-b74c-48a0-badf-d5bd2d741fda'}) MATCH (dis:Disciplina {disc_id: '3aab42a2-4697-4f4c-b8a8-55a1090cd4c7'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2022, nota: 9.58}]->(dis);
MATCH (a:Aluno {aluno_id: '69677a3a-b74c-48a0-badf-d5bd2d741fda'}) MATCH (dis:Disciplina {disc_id: 'f81d5fde-57b1-4579-a066-a424f62b3eaf'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2022, nota: 8.51}]->(dis);
CREATE (a:Aluno {aluno_id: 'f6e8a0f6-a727-47e1-9291-913418670f30', nome: 'Yuri Siqueira'}) WITH a MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: 'f6e8a0f6-a727-47e1-9291-913418670f30'}) MATCH (dis:Disciplina {disc_id: '7536bda1-1b34-4c88-8391-237550bb90fc'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2020, nota: 6.34}]->(dis);
MATCH (a:Aluno {aluno_id: 'f6e8a0f6-a727-47e1-9291-913418670f30'}) MATCH (dis:Disciplina {disc_id: 'a839c656-31bb-4c02-a2d9-3120256a6c0e'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2021, nota: 9.78}]->(dis);
MATCH (a:Aluno {aluno_id: 'f6e8a0f6-a727-47e1-9291-913418670f30'}) MATCH (dis:Disciplina {disc_id: 'da1807a8-b103-46ff-ac0a-c7e01fee576b'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2019, nota: 5.53}]->(dis);
CREATE (a:Aluno {aluno_id: '4ebf6312-23bd-4479-ad28-4fa94b1c123a', nome: 'Aylla Vargas'}) WITH a MATCH (c:Curso {curso_id: '15f14cf6-c9a9-4eb4-a858-bdcb1ac95647'}) CREATE (a)-[:MATRICULOU_EM]->(c);
MATCH (a:Aluno {aluno_id: '4ebf6312-23bd-4479-ad28-4fa94b1c123a'}) MATCH (dis:Disciplina {disc_id: '5f2b64a3-4560-4b53-90e4-1b6363d87041'}) CREATE (a)-[:COMPLETOU {semestre: '2', ano: 2023, nota: 9.75}]->(dis);
MATCH (a:Aluno {aluno_id: '4ebf6312-23bd-4479-ad28-4fa94b1c123a'}) MATCH (dis:Disciplina {disc_id: '7010e7e8-5bb3-4dec-99dd-6c861db49a2e'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2019, nota: 7.65}]->(dis);
MATCH (a:Aluno {aluno_id: '4ebf6312-23bd-4479-ad28-4fa94b1c123a'}) MATCH (dis:Disciplina {disc_id: 'b5c38a3f-7080-419e-bf0b-2ad6819bf0ab'}) CREATE (a)-[:COMPLETOU {semestre: '1', ano: 2020, nota: 5.33}]->(dis);

CREATE (g:GrupoProjeto {grupo_id: 'b9218e85-1570-41ae-b0ea-639b58bbed0a'}) WITH g MATCH (p:Professor {prof_id: '01f0bc07-dfaf-410d-ade4-8f448c818141'}) CREATE (g)-[:ORIENTADO_POR]->(p);
MATCH (a:Aluno {aluno_id: '69677a3a-b74c-48a0-badf-d5bd2d741fda'}) MATCH (g:GrupoProjeto {grupo_id: 'b9218e85-1570-41ae-b0ea-639b58bbed0a'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);
MATCH (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d'}) MATCH (g:GrupoProjeto {grupo_id: 'b9218e85-1570-41ae-b0ea-639b58bbed0a'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);
CREATE (g:GrupoProjeto {grupo_id: '879d37af-16a9-40a3-895b-55d466468e5a'}) WITH g MATCH (p:Professor {prof_id: '68b0d2b6-9809-42c8-a9e5-5321926c9f71'}) CREATE (g)-[:ORIENTADO_POR]->(p);
MATCH (a:Aluno {aluno_id: '11d8f579-c7e9-4c93-8d3f-67724afaf3b7'}) MATCH (g:GrupoProjeto {grupo_id: '879d37af-16a9-40a3-895b-55d466468e5a'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);
MATCH (a:Aluno {aluno_id: '6506023a-c370-406e-8a82-875b2019eae2'}) MATCH (g:GrupoProjeto {grupo_id: '879d37af-16a9-40a3-895b-55d466468e5a'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);
CREATE (g:GrupoProjeto {grupo_id: '99756729-50de-437f-a633-aca2ff07f863'}) WITH g MATCH (p:Professor {prof_id: 'a3608834-ddeb-4522-82bd-db7a3fb61b20'}) CREATE (g)-[:ORIENTADO_POR]->(p);
MATCH (a:Aluno {aluno_id: 'f6e8a0f6-a727-47e1-9291-913418670f30'}) MATCH (g:GrupoProjeto {grupo_id: '99756729-50de-437f-a633-aca2ff07f863'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);
MATCH (a:Aluno {aluno_id: '29c6f7f5-605f-46e9-801e-afa548fd002d'}) MATCH (g:GrupoProjeto {grupo_id: '99756729-50de-437f-a633-aca2ff07f863'}) CREATE (s)-[:PARTE_DO_GRUPO]->(g);