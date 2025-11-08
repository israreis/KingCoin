
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



// // --- Configuração do Gráfico (Chart.js) ---
// // Pega o "contexto" 2D do canvas
// const ctx = document.getElementById('graficoCarteira').getContext('2d');

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
//       x: { ticks: { color: '#10b981' }, grid: { display: false } },
//       // Estilização do eixo Y
//       y: { ticks: { color: '#10b981' }, grid: { color: 'rgba(255,255,255,0.05)' } }
//     }
//   }
// });


// Aguardar o DOM carregar completamente
document.addEventListener('DOMContentLoaded', function() {
    console.log('Iniciando carregamento dos gráficos...');
    
    // --- Gráfico de Linha (Evolução da Carteira) ---
    const ctxLine = document.getElementById('graficoCarteira');
    if (ctxLine) {
        new Chart(ctxLine, {
            type: 'line',
            data: {
                labels: ['Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out'],
                datasets: [{
                    label: 'Saldo (R$)',
                    data: [14500, 15200, 15800, 16300, 16550, 16800],
                    fill: true,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.4,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { 
                    legend: { display: false }
                },
                scales: {
                    x: { 
                        ticks: { color: '#10b981' }, 
                        grid: { display: false }
                    },
                    y: { 
                        ticks: { color: '#10b981' }, 
                        grid: { color: 'rgba(255,255,255,0.05)' }
                    }
                }
            }
        });
        console.log('Gráfico de linha criado');
    }

    // --- Gráfico de Barras (Despesas por Categoria) ---
    const ctxBarras = document.getElementById('graficoBarras');
    if (ctxBarras) {
        new Chart(ctxBarras, {
            type: 'bar',
            data: {
                labels: ['Alimentação', 'Transporte', 'Moradia', 'Lazer', 'Saúde', 'Educação'],
                datasets: [{
                    label: 'Valor Gasto (R$)',
                    data: [1200, 800, 1500, 600, 400, 300],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)',
                        'rgba(255, 159, 64, 0.8)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1,
                    borderRadius: 8,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `R$ ${context.parsed.y.toLocaleString('pt-BR')}`;
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { 
                            color: '#10b981',
                            font: { size: 11 }
                        },
                        grid: { display: false }
                    },
                    y: {
                        ticks: { 
                            color: '#10b981',
                            callback: function(value) {
                                return 'R$ ' + value.toLocaleString('pt-BR');
                            }
                        },
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        beginAtZero: true
                    }
                }
            }
        });
        console.log('Gráfico de barras criado');
    }

    // --- Gráfico de Pizza (Distribuição de Receitas) ---
    const ctxPizza = document.getElementById('graficoPizza');
    if (ctxPizza) {
        new Chart(ctxPizza, {
            type: 'pie',
            data: {
                labels: ['Salário', 'Freelance', 'Investimentos', 'Bônus', 'Outros'],
                datasets: [{
                    data: [65, 15, 12, 5, 3],
                    backgroundColor: [
                        'rgba(34, 197, 94, 0.8)',
                        'rgba(59, 130, 246, 0.8)',
                        'rgba(168, 85, 247, 0.8)',
                        'rgba(249, 115, 22, 0.8)',
                        'rgba(156, 163, 175, 0.8)'
                    ],
                    borderColor: [
                        'rgba(34, 197, 94, 1)',
                        'rgba(59, 130, 246, 1)',
                        'rgba(168, 85, 247, 1)',
                        'rgba(249, 115, 22, 1)',
                        'rgba(156, 163, 175, 1)'
                    ],
                    borderWidth: 2,
                    hoverOffset: 15
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#10b981',
                            padding: 15,
                            font: { size: 11 }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: ${context.parsed}%`;
                            }
                        }
                    }
                }
            }
        });
        console.log('Gráfico de pizza criado');
    }

    // --- Gráfico de Rosca (Metas de Economia) ---
    const ctxRosca = document.getElementById('graficoRosca');
    if (ctxRosca) {
        new Chart(ctxRosca, {
            type: 'doughnut',
            data: {
                labels: ['Concluído', 'Em Andamento', 'Pendente'],
                datasets: [{
                    data: [45, 30, 25],
                    backgroundColor: [
                        'rgba(34, 197, 94, 0.8)',
                        'rgba(59, 130, 246, 0.8)',
                        'rgba(239, 68, 68, 0.8)'
                    ],
                    borderColor: [
                        'rgba(34, 197, 94, 1)',
                        'rgba(59, 130, 246, 1)',
                        'rgba(239, 68, 68, 1)'
                    ],
                    borderWidth: 2,
                    hoverOffset: 15,
                    cutout: '60%'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#10b981',
                            padding: 15,
                            font: { size: 11 }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: ${context.parsed}%`;
                            }
                        }
                    }
                }
            }
        });
        console.log('Gráfico de rosca criado');
    }

    console.log('Todos os gráficos processados');
});