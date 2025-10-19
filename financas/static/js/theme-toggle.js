const toggle = document.getElementById('theme-toggle');
const body = document.body;
const card = document.getElementById('login-card');
const descText = document.getElementById('description-text');
const bottomText = document.getElementById('bottom-text');
const bgImage = document.getElementById('bg-image');
const logoImg = document.getElementById('logo-img');

const BG_DARK = "url('{% static 'img/background-escuro.png' %}')";
const BG_LIGHT = "url('{% static 'img/background-claro.png' %}')";
const LOGO_DARK = "{% static 'img/KingCoinLogo.svg' %}";
const LOGO_LIGHT = "{% static 'img/KingCoin-Logo-Light.svg' %}";

function applyTheme(isLight) {
    if (isLight) {
        body.classList.replace('bg-[#000805]', 'bg-[#fffcf0]');
        body.classList.replace('text-white', 'text-[#000805]');
        card.classList.replace('glass-dark', 'glass-light');
        descText.classList.replace('text-gray-300', 'text-[#4b4b4b]');
        bottomText.classList.replace('text-gray-300', 'text-[#4b4b4b]');
        bgImage.style.backgroundImage = BG_LIGHT;
        logoImg.src = LOGO_LIGHT;
        toggle.checked = true;
        localStorage.setItem('theme', 'light');
    } else {
        body.classList.replace('bg-[#fffcf0]', 'bg-[#000805]');
        body.classList.replace('text-[#000805]', 'text-white');
        card.classList.replace('glass-light', 'glass-dark');
        descText.classList.replace('text-[#4b4b4b]', 'text-gray-300');
        bottomText.classList.replace('text-[#4b4b4b]', 'text-gray-300');
        bgImage.style.backgroundImage = BG_DARK;
        logoImg.src = LOGO_DARK;
        toggle.checked = false;
        localStorage.setItem('theme', 'dark');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    applyTheme(savedTheme === 'light');
    body.classList.remove('transition-colors', 'duration-500');
    setTimeout(() => {
        body.classList.add('transition-colors', 'duration-500');
    }, 100);
});

toggle.addEventListener('change', () => {
    applyTheme(toggle.checked);
});