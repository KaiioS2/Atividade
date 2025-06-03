// Laço de repetiçao: While

let i = 1

while (i <= 5) {
    console.log(i)
    i++
}

// Exercicio: 
//  Solicite ao usuario uma nota,
//  caso seja menor que zero ou maior que dez,
//  faça a pergunta novamente.

console.clear()
const readline = require('readline-sync')
const numero = readline.questionInt('Digite um numero: ')

while (numero <0 || numero > 10){ 
    console.log('NUmero indesejado')
        break
}

// And == &&
// or == ||