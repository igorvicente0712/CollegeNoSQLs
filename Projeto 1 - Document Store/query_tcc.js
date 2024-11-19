db.alunos.aggregate([
  { $match: { _id: "2021001" } },  // Substitua pelo ID do aluno desejado
  { $unwind: "$disciplinas" },
  { $lookup: {
      from: "disciplinas",
      localField: "disciplinas.codigo",
      foreignField: "_id",
      as: "disciplina_info"
  }},
  { $unwind: "$disciplina_info" },
  { $project: {
      _id: 0,
      codigo: "$disciplinas.codigo",
      nome: "$disciplina_info.nome",
      semestre: "$disciplinas.semestre",
      ano: "$disciplinas.ano",
      nota: "$disciplinas.nota"
  }},
  { $sort: { ano: 1, semestre: 1 } }
])
