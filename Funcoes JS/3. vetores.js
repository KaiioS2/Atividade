// Criando um vetor.
const alunos = ['Marta', 'Jose', 'Maria']
console.log('\nExibindo todos os elementos. ')
console.log(alunos)

console.log('\nExibindo apena o primeiro elementos.')
console.log(alunos[0])

console.log('\nExibindo apena o ultimo elementos.')
console.log(alunos[2])

console.log('\nAdicionando um elemento final ao vetor.')
alunos.push('Ana')
console.log(alunos)

console.log('\nAdicionando um elemento no inicio do vetor.')
alunos.unshift('Marilia')
console.log(alunos)

console.log('\nremovendo um elemento final do vetor.')
alunos.pop()
console.log(alunos)

console.log('\nRemovendo apena um elemento do vetor.')
alunos.pop(2) // Removendo o terceiro elemento do vector
console.log(alunos)
