// --- Configuração dos Dropdowns ---
// Array de objetos para configurar os dois dropdowns (evita repetir código)
const dropdowns = [
  {
    button: "dropdownSaldoBtn",      // ID do botão
    menu: "dropdownSaldo",          // ID do menu
    selected: "selectedPeriodoSaldo", // ID do <span> que mostra o texto selecionado
    dados: dadosSaldo,              // Objeto de dados a usar
    valorId: "saldoValor",          // ID do elemento <p> do valor
    porcentId: "saldoPorcentagem",  // ID do <span> da porcentagem
    variacaoId: "saldoVariacao"     // ID do <span> da variação
  },
  {
    button: "dropdownInvestBtn",
    menu: "dropdownInvest",
    selected: "selectedPeriodoInvest",
    dados: dadosInvestimentos,
    valorId: "investValor",
    porcentId: "investPorcentagem",
    variacaoId: "investVariacao"
  },
];

// --- Lógica Principal dos Dropdowns ---
// Itera sobre cada configuração de dropdown
dropdowns.forEach(d => {
  // Pega os elementos do HTML usando os IDs da configuração
  const btn = document.getElementById(d.button);
  const menu = document.getElementById(d.menu);
  const selected = document.getElementById(d.selected);
  const valor = document.getElementById(d.valorId);
  const porcent = document.getElementById(d.porcentId);
  const variacao = document.getElementById(d.variacaoId);

  // Adiciona o evento de clique no BOTÃO PRINCIPAL (ex: "Este mês")
  btn.addEventListener("click", () => menu.classList.toggle("hidden")); // Mostra/esconde o menu

  // Adiciona o evento de clique em CADA OPÇÃO DENTRO DO MENU
  menu.querySelectorAll("button").forEach(option => {
    option.addEventListener("click", () => {
      // Pega o valor da opção (ex: "Último mês")
      const periodo = option.dataset.value;
      
      // Atualiza o texto do botão principal
      selected.textContent = periodo;
      
      // Esconde o menu
      menu.classList.add("hidden");

      // Atualiza os textos (Valor, Porcentagem, Variação) com base nos dados "fake"
      if (d.dados[periodo]) {
        valor.textContent = d.dados[periodo].valor;
        porcent.textContent = d.dados[periodo].porcentagem;
        variacao.textContent = d.dados[periodo].variacao;
      }

      // --- A MÁGICA ACONTECE AQUI: Lógica de cor SÓ para Investimentos ---
      if (d.button === "dropdownInvestBtn") {
        // Pega os elementos necessários para a lógica
        const card = valor.closest(".bg-gradient-to-l"); // Pega o 'pai' do card
        const valorAtual = parseValor(d.dados[periodo].valor);
        const valorUltimo = parseValor(d.dados["Último mês"].valor); // Referência fixa

        const pContainer = porcent.parentElement; // O <p> que segura a seta e os textos
        const arrowSvg = pContainer.querySelector("svg"); // A seta
        const menuOptions = menu.querySelectorAll("button"); // Os botões DENTRO do menu

        // --- 1. Limpeza ---
        // Limpa as classes de cor anteriores do CARD
        card.classList.remove(
          "border-red-600/40", "from-red-600/40",      // Classes vermelhas
          "border-emerald-900/70", "from-[#23b785]/25" // Classes verdes
        );

        // Limpa as classes de cor anteriores do MENU
        menu.classList.remove(
          "bg-[#1a0f0f]", "border-[#5a1717]", // Classes vermelhas
          "bg-[#0d1a15]", "border-[#1f5b46]"  // Classes verdes
        );

        // --- 2. Aplica as cores (Condicional) ---
        if (valorAtual > valorUltimo) {
          // 📈 SUBIU (VERDE)
          
          // Aplica classes verdes ao CARD
          card.classList.add("border-emerald-900/70", "from-[#23b785]/25", "bg-gradient-to-l", "via-transparent", "to-transparent");
          
          // Aplica classes verdes ao MENU
          menu.classList.add("bg-[#0d1a15]", "border-[#1f5b46]");

          // Muda o HOVER das OPÇÕES do menu para verde
          menuOptions.forEach(opt => {
            opt.classList.remove("hover:bg-[#301010]"); // Remove hover vermelho
            opt.classList.add("hover:bg-[#123124]");    // Adiciona hover verde
          });

          // Muda as cores dos TEXTOS para verde
          valor.classList.replace("text-red-600", "text-emerald-400");
          porcent.classList.replace("text-red-600", "text-emerald-400");
          variacao.classList.replace("text-red-600", "text-emerald-400");
          pContainer.classList.replace("text-red-600", "text-emerald-400");

          // Garante que a SETA aponte para cima (remove a rotação)
          if (arrowSvg) arrowSvg.classList.remove("rotate-180");

        } else {
          // 🔻 CAIU (VERMELHO)
          
          // Aplica classes vermelhas ao CARD
          card.classList.add("border-red-600/40", "from-red-600/40", "bg-gradient-to-l", "via-transparent", "to-transparent");
          
          // Aplica classes vermelhas ao MENU
          menu.classList.add("bg-[#1a0f0f]", "border-[#5a1717]");

          // Muda o HOVER das OPÇÕES do menu para vermelho
          menuOptions.forEach(opt => {
            opt.classList.remove("hover:bg-[#123124]");  // Remove hover verde
            opt.classList.add("hover:bg-[#301010]");    // Adiciona hover vermelho
          });

          // Muda as cores dos TEXTOS para vermelho
          valor.classList.replace("text-emerald-400", "text-red-600");
          porcent.classList.replace("text-emerald-400", "text-red-600");
          variacao.classList.replace("text-emerald-400", "text-red-600");
          pContainer.classList.replace("text-emerald-400", "text-red-600");

          // Garante que a SETA aponte para baixo (adiciona a rotação)
          if (arrowSvg) arrowSvg.classList.add("rotate-180");
        }
      }
    });
  });

  // --- Lógica para fechar o dropdown ao clicar fora ---
  document.addEventListener("click", e => {
    // Se o clique NÃO foi no menu E NÃO foi no botão
    if (!menu.contains(e.target) && !btn.contains(e.target)) {
      menu.classList.add("hidden"); // Esconde o menu
    }
  });
});

// --- Botões de Ação (Ganhos, Despesas, Investir) ---
// Apenas mostram um alerta por enquanto
document.getElementById("btnGanhos").addEventListener("click", () => alert("Abrir modal para adicionar ganhos 💰"));
document.getElementById("btnDespesas").addEventListener("click", () => alert("Abrir modal para adicionar despesas 💸"));
document.getElementById("btnInvestir").addEventListener("click", () => alert("Abrir modal para adicionar investimentos 📈"));

// --- Configuração do Gráfico (Chart.js) ---
// Pega o "contexto" 2D do canvas
const ctx = document.getElementById('graficoCarteira').getContext('2d');

// Cria um novo gráfico
new Chart(ctx, {
  type: 'line', // Tipo de gráfico: linha
  data: {
    labels: ['Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out'], // Rótulos do eixo X
    datasets: [{
      label: 'Saldo (R$)',
      data: [14500, 15200, 15800, 16300, 16550, 16800], // Dados do eixo Y
      fill: true, // Preencher a área abaixo da linha
      borderColor: '#10b981', // Cor da linha (verde)
      backgroundColor: 'rgba(16, 185, 129, 0.1)', // Cor do preenchimento (verde transparente)
      tension: 0.4, // Deixa a linha curvada
      
    }]
  },
  options: {
    responsive: true, // Torna o gráfico responsivo
    plugins: { legend: { display: false } }, // Esconde a legenda
    scales: {
      // Estilização do eixo X
      x: { ticks: { color: '#aaa' }, grid: { display: false } },
      // Estilização do eixo Y
      y: { ticks: { color: '#aaa' }, grid: { color: 'rgba(255,255,255,0.05)' } }
    }
  }
});