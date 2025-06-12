function gerarTabuada() {
    const numeroInput = document.getElementById('numeroInput');
    let numero = parseInt(numeroInput.value);

    const resultadoDiv = document.getElementById('resultadoTabuada');
    resultadoDiv.innerHTML = ''; // Limpa o conteúdo anterior

    // Validação para verificar se o input é um número válido
    if (isNaN(numero) || numeroInput.value.trim() === '') {
        resultadoDiv.innerHTML = '<p>Por favor, digite um número válido.</p>';
        return; // Sai da função se não for um número
    }

    resultadoDiv.innerHTML += `<h2>Tabuada do ${numero}</h2>`;

    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i;
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`;
    }
}

const gerarBotao = document.getElementById('gerarBotao');
gerarBotao.addEventListener('click', gerarTabuada);
