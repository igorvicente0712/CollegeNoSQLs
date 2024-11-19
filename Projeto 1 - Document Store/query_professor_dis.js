db.professores.aggregate([
  { $match: { _id: "p001" } },  // Substitua pelo ID do professor desejado
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
      ano: "$disciplinas.ano"
  }},
  { $sort: { ano: 1, semestre: 1 } }
])
