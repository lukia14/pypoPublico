const A = document.getElementById("A");
const B = document.getElementById("B");
const C = document.getElementById("C");
const D = document.getElementById("D");
const alternativas = document.querySelectorAll(".botao");
const pergunta = document.getElementById('pergunta')
const pontuacaoHTML = document.getElementById("pontuacao");
const sequenciaHTML = document.getElementById("sequencia");

const containerLink = document.getElementById("container-link");
var pontuacao = 100;
var sequenciaAcerto = 0;

var listaExercicios = JSON.parse(document.getElementById("listaExercicios").value);
var numeroExercicio = 1;
console.log(listaExercicios)
carregarExercicio(1)

alternativas.forEach((botao) => {//percorre cada botão

    botao.addEventListener("click", function() {//adiciona o evento de clique

        const respostaCorreta = listaExercicios[numeroExercicio - 1].resposta.toLowerCase();//pega a resposta do exercício atual e coloca em minúscula
        
        if(botao.id.toLowerCase() === respostaCorreta) {//compara o id do botão clicado com a resposta 
            botao.classList.add("acerto");//adiciona a classe correto
            desabilitarAlternativas()
            sequenciaAcerto++
            pontuacao += 10 * sequenciaAcerto
            numeroExercicio++
            pontuacaoHTML.innerHTML = `Pontos: ${pontuacao}`;
            sequenciaHTML.innerHTML = `<i class="fa-solid fa-square-check fa-beat" style="color: #0e2349;"></i>sequência: ${sequenciaAcerto}`;
            const div = document.querySelector('.botao_continuar')
            const botaoPassar = document.createElement('button')
            botaoPassar.innerHTML = `<strong>Continuar <i class="fa-solid fa-arrow-right" class="icon1"></i></strong>` 
            botaoPassar.classList.add('botao_passar')
            div.append(botaoPassar)
            botaoPassar.addEventListener('click', function() {
                carregarExercicio(numeroExercicio)
                botaoPassar.remove()
                alternativas.forEach((b) => b.disabled = false);
                alternativas.forEach((b) => b.classList.remove("acerto", "erro"));
            }
            
            
    )} 
        else {
            botao.classList.add("erro");//adiciona a classe errado
            if (pontuacao <= 25){
                pontuacao = 0
            }
            else{
                pontuacao -= 25
            }
            
            sequenciaAcerto = 0
            pontuacaoHTML.innerHTML = `Pontos: ${pontuacao}`;
        }
    })
})

// continuar.addEventListener("click", function() {
//     numeroExercicio++;
//     carregarExercicio(numeroExercicio);
// })




// Funções de auxilio
function enviarPontuacaoFlask(pontuacao,idFase){
    const tokencsrf = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    return fetch('/api/salvarPontuacaoFase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokencsrf
        },
        body: JSON.stringify({
            'idFase': parseInt(idFase)+1,
            'pontuacao': pontuacao
        })
    })
}

function carregarExercicio(num) {
    if (num > listaExercicios.length) {
        const a = document.createElement("a");
        const idFase = document.getElementById("idFase").value;
        enviarPontuacaoFlask(pontuacao,idFase)
        .then(response => {
            if (response.ok) {
                // SÓ MUDA DE PÁGINA SE O SERVIDOR DEU OK
                console.log('js foi')
                const a = document.createElement("a");
                const linkBase = containerLink.getAttribute("data-url-fase");
                const linkProximaFase = linkBase.replace("999999", pontuacao).replace("777777", idFase);
                
                a.href = linkProximaFase;
                a.click();
            } else {
                console.error("O Flask recebeu o pedido, mas retornou um erro.");
            }
        })
        .catch(error => {
            console.error("Erro crítico na requisição de salvar:", error);
        });
        return
    }
    pergunta.innerText = listaExercicios[num-1].enunciado;
    A.innerText = listaExercicios[num-1].alternativaA;
    B.innerText = listaExercicios[num-1].alternativaB;
    C.innerText = listaExercicios[num-1].alternativaC;
    D.innerText = listaExercicios[num-1].alternativaD;
    
    
}
/* ATRIBUTOS DO OBJETO EXERCICIO:
idExercicio
titulo
enunciado
alternativaA
alternativaB
alternativaC
alternativaD
resposta
*/

function desabilitarAlternativas() {//função para desabilitar os botões
    alternativas.forEach((b) => b.disabled = true);//desabilita todos os botões
}

function enviarFlask(dict){
    /*
const enviarFlask = [
    {pontuacao: pontuacao},
    {sequencia: sequenciaAcerto
    }
]

//const continuar = document.getElementById("continuar");
const finalizar = document.getElementById("finalizar");

finalizar.addEventListener("click", async function() {

    const res = await fetch("/fase1/finalizar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({pontuacao: pontuacao})
    })
    const data = await res.json();
    console.log(data);
})
*/

}
// Garantir que o script rode apenas após o HTML carregar completamente
window.addEventListener("load", function () {
    const btnMochila = document.getElementById("btn-mochila");
    const navMochila = document.getElementById("mochila-lateral");
    const fecharMochila = document.getElementById("fechar-mochila");

    // Só adiciona o evento de clique se os elementos realmente existirem na página atual
    if (btnMochila && navMochila) {
        btnMochila.addEventListener("click", function (e) {
            e.preventDefault(); // Evita qualquer comportamento padrão do navegador
            navMochila.classList.add("aberta");
        });
    }

    if (fecharMochila && navMochila) {
        fecharMochila.addEventListener("click", function (e) {
            e.preventDefault();
            navMochila.classList.remove("aberta");
        });
    }
});