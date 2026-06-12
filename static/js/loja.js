const botoes = document.querySelectorAll('.botao-comprar')
const pontuacaoHTML = document.getElementById('pontuacao')
const botaoSalvarCompra = document.querySelector('.botao-sair-salvar')
var pontuacao = parseInt(pontuacaoHTML.textContent.split(' ')[1])

botaoSalvarCompra.addEventListener('click', () => {
    console.log('Salvando compra...');
    
    const tokencsrf = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    
    fetch('/api/salvarCompra', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': tokencsrf
        },
        body: JSON.stringify({
            'estoque': listaEstoque,
            'pontuacao': pontuacao
        })
    })
    // 1️⃣ Transforma a resposta bruta do Flask em um objeto JavaScript (JSON)
    .then(response => response.json())
    
    // 2️⃣ Agora sim! A variável 'dados' nasce aqui com o que o Python respondeu
    .then(dados => {
        console.log('Resposta do servidor:', dados);
        
        if (dados.status === 'sucesso') {
            // Mostra o flash verde usando a mensagem vinda do Python
            flash(dados.mensagem, 'success'); 
            
            // Opcional: Se quiser limpar o carrinho/lista local após salvar:
            // listaEstoque = []; 
        } else {
            // Se o Python mandou um status de erro, mostra o flash vermelho
            flash(dados.mensagem, 'danger');
        }
    })
    // 3️⃣ Caso o servidor esteja desligado ou a rede caia totalmente
    .catch(error => {
        console.error('Erro no fetch:', error);
        flash('Erro crítico ao salvar a compra.', 'danger');
    });
});

async function carregarItensAPI() {
    try{
        const response = await fetch('/api/itensLoja')
        return await response.json()
        
    }catch(error){
        console.error('Erro ao carregar itens da loja:', error)
    }
}

async function carregarEstoqueAPI() {
    try{
        const response = await fetch('/api/estoque')
        return await response.json()
    }  catch(error){
        console.error('Erro ao carregar estoque:', error)
    }
}

let listaItens = await carregarItensAPI()
let listaEstoque = await carregarEstoqueAPI()

botoes.forEach(botao =>{
    botao.addEventListener('click', async (event) => {
        const itemId = event.target.classList[1]
        let item = listaItens.find(item => item.idItem == itemId)
        console.log(item)
        let valor = item?.valor || 0
        if (pontuacao < valor){
            flash(`Você precisa de ${valor} pontos, mas só tem ${pontuacao}!`, 'alerta');
            return 
        }
        pontuacao -= valor
        pontuacaoHTML.textContent = `pontuação: ${pontuacao}`
        salvarCompra(itemId)
        renderizarEstoque()
            
    })
})

    

function salvarCompra(itemId) {
    const item = listaEstoque.find(item => item.idItem == itemId)
    if (item){
        item.qtd += 1
    }
    else{
        let itemLista = listaItens.find(item => item.idItem == itemId)
        listaEstoque.push({idItem: itemId, qtd: 1, nome: itemLista.nome})
    }
    renderizarEstoque()
}

function renderizarEstoque(){
    listaEstoque.forEach(item=>{
        const container = document.querySelector('#inventario-dados')
        const div = document.createElement('div')
        div.classList.add('item-inventario')
        container.innerHTML = ''
        const spanNome = document.createElement('span')
        const spanQtd = document.createElement('span')
        
        spanNome.classList.add('nome-item-inventario')
        spanQtd.classList.add('qtd-item-inventario')
        
        spanNome.innerHTML = item.nome 
        spanQtd.innerHTML = item.qtd
        div.append(spanNome,spanQtd)
        container.append(div)
    })
}




function flash(mensagem, tipo = 'sucesso') {
    // Procura o container na tela
    let container = document.getElementById('flash-container');
    
    // Se o container não existir no HTML, o JS cria ele sozinho agora:
    if (!container) {
        container = document.createElement('div');
        container.id = 'flash-container';
        document.body.appendChild(container);
    }
    
    // Cria o elemento da mensagem
    const div = document.createElement('div');
    div.classList.add('flash-message', `flash-${tipo}`);
    div.innerText = mensagem;
    
    // Adiciona na tela
    container.appendChild(div);
    
    // Remove automaticamente após 4 segundos
    setTimeout(() => {
        div.remove();
    }, 4000);
}