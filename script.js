// script.js
let selecionadas = [];
let botoesSelecionados = [];
let encontradas = new Set();
let isMouseDown = false;
let totalPalavras = 0;

// CONTROLE DE NÍVEIS
let nivelAtual = 1;
const maxNiveis = 3;

// Inicia o jogo carregando o nível 1
carregarJogo(nivelAtual);

function carregarJogo(nivel) {
    // Reseta estados visuais e dados
    selecionadas = [];
    botoesSelecionados = [];
    encontradas = new Set();
    document.getElementById("tela-vitoria").style.display = "none";
    document.getElementById("titulo-nivel").innerText = "NÍVEL " + nivel;

    // Busca dados do nível específico
    fetch(`/dados?nivel=${nivel}`)
    .then(res => res.json())
    .then(dados => {
        totalPalavras = dados.palavras.length;
        criarGrade(dados.grade);
        atualizarLista(dados.palavras);
    });
}

function criarGrade(letras) {
    const grade = document.getElementById("grade");
    grade.innerHTML = ""; 

    letras.forEach(letra => {
        const btn = document.createElement("button");
        btn.textContent = letra;

        btn.onmousedown = (e) => {
            e.preventDefault();
            isMouseDown = true;
            selecionarLetra(letra, btn);
        };

        btn.onmouseover = () => {
            if (isMouseDown) {
                selecionarLetra(letra, btn);
            }
        };

        grade.appendChild(btn);
    });
}

window.onmouseup = () => {
    if (isMouseDown) {
        isMouseDown = false;
        verificarPalavraNoServidor();
    }
};

function selecionarLetra(letra, botao) {
    if (!botoesSelecionados.includes(botao)) {
        selecionadas.push(letra);
        botoesSelecionados.push(botao);
        botao.classList.add("selecionada");
    }
}

function verificarPalavraNoServidor() {
    const palavra = selecionadas.join("");

    // Envia a palavra E o nível atual para verificação
    fetch("/verificar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ palavra: palavra, nivel: nivelAtual })
    })
    .then(res => res.json())
    .then(resp => {
        if (resp.valida && !encontradas.has(palavra)) {
            encontradas.add(palavra);
            
            marcarLista(palavra);

            botoesSelecionados.forEach(b => {
                b.classList.remove("selecionada");
                b.classList.add("correta");
            });
            
            checarVitoria();
        } else {
            botoesSelecionados.forEach(b => b.classList.remove("selecionada"));
        }
        selecionadas = [];
        botoesSelecionados = [];
    })
    .catch(err => console.error("Erro:", err));
}

function marcarLista(palavra) {
    const itens = document.querySelectorAll("#lista li");
    itens.forEach(li => {
        if (li.textContent === palavra) {
            li.style.textDecoration = "line-through";
            li.style.color = "#5555ff";
        }
    });
}

function checarVitoria() {
    if (encontradas.size === totalPalavras) {
        const telaVitoria = document.getElementById("tela-vitoria");
        const btnReiniciar = document.getElementById("btn-reiniciar");
        const msgVitoria = document.getElementById("mensagem-vitoria");
        
        telaVitoria.style.display = "flex"; 
        
        // Lógica de transição de níveis
        if (nivelAtual < maxNiveis) {
            msgVitoria.textContent = "NÍVEL COMPLETO!";
            btnReiniciar.textContent = "Próximo Nível >>";
            btnReiniciar.onclick = () => {
                nivelAtual++;
                carregarJogo(nivelAtual);
            };
        } else {
            msgVitoria.textContent = "VOCÊ ZEROU O JOGO!";
            btnReiniciar.textContent = "Jogar Novamente";
            btnReiniciar.onclick = () => {
                nivelAtual = 1;
                carregarJogo(nivelAtual);
            };
        }
        
        // Confetes
        dispararConfetes();
    }
}

function dispararConfetes() {
    var duration = 3000;
    var end = Date.now() + duration;

    (function frame() {
        confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 } });
        confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 } });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());
}

function atualizarLista(palavras) {
    const ul = document.getElementById("lista");
    ul.innerHTML = ""; 
    palavras.forEach(p => {
        const li = document.createElement("li");
        li.textContent = p;
        ul.appendChild(li);
    });
}