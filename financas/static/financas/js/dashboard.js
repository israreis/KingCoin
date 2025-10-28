
// // --- Configuração do Gráfico (Chart.js) ---
// // Pega o "contexto" 2D do canvas
// const ctx = document.getElementById('graficoCarteira').getContext('2d');

// const root = document.body;
// const textColor = getComputedStyle(root).getPropertyValue('--text-color').trim() || '';

// // Cria um novo gráfico
// new Chart(ctx, {
//   type: 'line', // Tipo de gráfico: linha
//   data: {
//     labels: ['Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out'], // Rótulos do eixo X
//     datasets: [{
//       label: 'Saldo (R$)',
//       data: [14500, 15200, 15800, 16300, 16550, 16800], // Dados do eixo Y
//       fill: true, // Preencher a área abaixo da linha
//       borderColor: '#10b981', // Cor da linha (verde)
//       backgroundColor: 'rgba(16, 185, 129, 0.1)', // Cor do preenchimento (verde transparente)
//       tension: 0.4, // Deixa a linha curvada
      
//     }]
//   },
//   options: {
//     responsive: true, // Torna o gráfico responsivo
//     plugins: { legend: { display: false } }, // Esconde a legenda
//     scales: {
//       // Estilização do eixo X
//       x: { ticks: { color: textColor }, grid: { display: false } },
//       // Estilização do eixo Y
//       y: { ticks: { color: textColor }, grid: { color: 'rgba(255,255,255,0.05)' } }
//     }
//   }
// });



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
      x: { ticks: { color: '#10b981' }, grid: { display: false } },
      // Estilização do eixo Y
      y: { ticks: { color: '#10b981' }, grid: { color: 'rgba(255,255,255,0.05)' } }
    }
  }
});