// Função para simular prompt no Node.js, caso não esteja no navegador
// Em um navegador, 'prompt' já é global.
const getNumberInput = async (message) => {
    if (typeof window !== 'undefined' && window.prompt) {
        // No navegador, use window.prompt
        return parseInt(window.prompt(message));
    } else {
        // No Node.js, use readline
        const readline = await import('node:readline'); // Importação dinâmica
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        return new Promise(resolve => {
            rl.question(message, (answer) => {
                rl.close();
                resolve(parseInt(answer));
            });
        });
    }
};

async function contagemRegressiva() {
    let numeroInicial = await getNumberInput("Digite um número para iniciar a contagem regressiva:");

    // Validação da entrada
    if (isNaN(numeroInicial) || numeroInicial <= 0) {
        console.log("Por favor, digite um número inteiro positivo válido.");
        return;
    }

    console.log(`Iniciando contagem regressiva a partir de ${numeroInicial}...`);

    for (let i = numeroInicial; i >= 1; i--) {
        console.log(i);
        // Aguarda 1 segundo antes de exibir o próximo número
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

    console.log("Contagem regressiva concluída!");
}

// Chama a função principal
contagemRegressiva();