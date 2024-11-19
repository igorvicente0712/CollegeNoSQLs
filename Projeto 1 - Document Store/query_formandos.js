db.alunos.aggregate([
  { $match: { "disciplinas.ano": 2023, "disciplinas.semestre": 2 } },  // Substitua pelo ano e semestre desejados
  { $lookup: {
      from: "cursos",
      localField: "curso",
      foreignField: "_id",
      as: "curso_info"
  }},
  { $unwind: "$curso_info" },
  { $project: {
      _id: 1,
      nome: 1,
      curso: 1,
      disciplinas: 1,
      curso_disciplinas: "$curso_info.disciplinas"
  }},
  { $addFields: {
      disciplinas_aprovadas: {
          $filter: {
              input: "$disciplinas",
              as: "disciplina",
              cond: { $gte: ["$$disciplina.nota", 6] }
          }
      }
  }},
  { $project: {
      _id: 1,
      nome: 1,
      curso: 1,
      todas_disciplinas: { $setEquals: ["$curso_disciplinas", "$disciplinas_aprovadas.codigo"] }
  }},
  { $match: { todas_disciplinas: true } },
  { $project: {
      _id: 1,
      nome: 1,
      curso: 1
  }}
])
