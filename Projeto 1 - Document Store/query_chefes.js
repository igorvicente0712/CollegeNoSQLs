db.departamentos.aggregate([
  { $lookup: {
      from: "professores",
      localField: "chefe",
      foreignField: "_id",
      as: "chefe_info"
  }},
  { $unwind: "$chefe_info" },
  { $project: {
      _id: 0,
      nome_professor: "$chefe_info.nome",
      nome_departamento: "$nome"
  }}
])
