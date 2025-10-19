const sidebar = document.getElementById('sidebar');
        const themeToggle = document.querySelector('.theme-toggle');
        const body = document.body;
        const navItems = document.querySelectorAll('.nav-item');
        
        // 1. Inicialização - Garantir estado correto no carregamento
        function initializeSidebar() {
            // Verificar se é mobile e ajustar estado inicial
            if (window.innerWidth <= 640) {
                sidebar.classList.remove('collapsed'); // Garantir que comece como navbar inferior
            }
        }

        // 2. Alternar Tema Claro/Escuro
        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            body.classList.toggle('light-mode');
            
            // Alternar ícone (Sol <-> Lua)
            const icon = themeToggle.querySelector('i');
            if (body.classList.contains('dark-mode')) {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            } else {
                 icon.classList.remove('fa-moon');
                 icon.classList.add('fa-sun');
            }
        });

        // 3. Sistema de Navegação Ativa
        navItems.forEach(item => {
            if (!item.classList.contains('mobile-logo-placeholder')) {
                item.addEventListener('click', (e) => {
                    // Remove classe active de todos os itens
                    navItems.forEach(navItem => {
                        navItem.classList.remove('active');
                    });
                    // Adiciona classe active apenas ao item clicado
                    item.classList.add('active');
                    
                    // Atualiza o conteúdo principal baseado no item clicado
                    updateMainContent(item);
                    
                    // No mobile, recolhe o menu após clicar em um item (exceto logo)
                    if (window.innerWidth <= 640 && !item.classList.contains('mobile-logo-placeholder')) {
                        sidebar.classList.remove('collapsed');
                    }
                });
            }
        });

        // 4. Expandir/Contrair (Lógica Centralizada para Desktop e Mobile)
        
        // Listener para a logo do DESKTOP (dentro do sidebar-header)
        const desktopLogoContainer = document.querySelector('.sidebar-header .logo-container');
        if (desktopLogoContainer) {
             desktopLogoContainer.addEventListener('click', () => {
                if (window.innerWidth > 640) { 
                    sidebar.classList.toggle('collapsed'); 
                }
            });
        }
        
        // Listener para a logo do MOBILE (dentro do mobile-logo-placeholder)
        const mobileLogoPlaceholder = document.querySelector('.mobile-logo-placeholder .logo-container');
        if (mobileLogoPlaceholder) {
            mobileLogoPlaceholder.addEventListener('click', () => {
                if (window.innerWidth <= 640) { 
                    sidebar.classList.toggle('collapsed');
                }
            });
        }

        // 5. Botão de voltar no menu expandido mobile
        function createBackButton() {
            const backButton = document.createElement('div');
            backButton.className = 'mobile-back-button';
            backButton.innerHTML = `
                <button class="back-btn">
                    <i class="fas fa-chevron-down"></i>
                    <span>Voltar ao Menu</span>
                </button>
            `;
            return backButton;
        }

        // Adiciona botão de voltar quando em modo mobile expandido
        function checkMobileMenu() {
            const sidebarFooter = document.querySelector('.sidebar-footer');
            const existingBackButton = document.querySelector('.mobile-back-button');
            
            if (window.innerWidth <= 640 && sidebar.classList.contains('collapsed')) {
                if (!existingBackButton) {
                    const backButton = createBackButton();
                    sidebarFooter.parentNode.insertBefore(backButton, sidebarFooter);
                    
                    // Adiciona evento de clique no botão voltar
                    backButton.querySelector('.back-btn').addEventListener('click', () => {
                        sidebar.classList.remove('collapsed');
                    });
                }
            } else {
                if (existingBackButton) {
                    existingBackButton.remove();
                }
            }
        }

        // 6. Atualizar conteúdo principal
        function updateMainContent(selectedItem) {
            const mainContent = document.getElementById('main-content');
            const itemText = selectedItem.querySelector('.nav-text').textContent;
            
            let contentHTML = '';
            
            switch(itemText) {
                case 'Dashboard':
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Dashboard</h1>
                            <div class="content-grid">
                                <div class="card">Saldo Atual: R$ 1.250,00</div>
                                <div class="card">Transações do Mês: 15</div>
                                <div class="card">Investimentos: R$ 5.000,00</div>
                            </div>
                        </div>
                    `;
                    break;
                case 'Carteira':
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Carteira</h1>
                            <div class="content-section">
                                <h2>Suas Carteiras</h2>
                                <p>Gerencie suas carteiras digitais aqui.</p>
                            </div>
                        </div>
                    `;
                    break;
                case 'Transações':
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Transações</h1>
                            <div class="content-section">
                                <h2>Histórico de Transações</h2>
                                <p>Visualize todas as suas transações recentes.</p>
                            </div>
                        </div>
                    `;
                    break;
                case 'Relatórios':
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Relatórios</h1>
                            <div class="content-section">
                                <h2>Relatórios Financeiros</h2>
                                <p>Gere relatórios detalhados do seu desempenho financeiro.</p>
                            </div>
                        </div>
                    `;
                    break;
                case 'Configurações':
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Configurações</h1>
                            <div class="content-section">
                                <h2>Configurações da Conta</h2>
                                <p>Personalize suas preferências e configurações de segurança.</p>
                            </div>
                        </div>
                    `;
                    break;
                default:
                    contentHTML = `
                        <div class="content-wrapper">
                            <h1>Conteúdo Principal do Webapp</h1>
                            <p>Aqui você verá o conteúdo das páginas.</p>
                        </div>
                    `;
            }
            
            mainContent.innerHTML = contentHTML;
        }

        // 7. Gerenciamento de Responsividade
        function handleResponsive() {
            if (window.innerWidth <= 640) {
                // Mobile: garantir que comece como navbar inferior
                if (!sidebar.classList.contains('initialized-mobile')) {
                    sidebar.classList.remove('collapsed');
                    sidebar.classList.add('initialized-mobile');
                }
            } else {
                // Desktop: remover marcação de mobile
                sidebar.classList.remove('initialized-mobile');
            }
            checkMobileMenu();
        }

        // Event Listeners
        sidebar.addEventListener('transitionend', checkMobileMenu);
        window.addEventListener('resize', handleResponsive);
        
        // Inicialização
        initializeSidebar();
        handleResponsive();
        checkMobileMenu();