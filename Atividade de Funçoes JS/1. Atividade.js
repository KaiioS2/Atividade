console.clear()
const readline = require('readline-sync')
const numero = readline.questionInt('Digite um numero: ')

function verificar(numero) {
    if (numero >= 0) {
      return 'O número é positivo ou zero.';
    } else {
      return 'O número é negativo.';
    }
  }
const meuNumero = 10; // Defina um número para testar
const resultado = verificar(meuNumero);
console.log(resultado)