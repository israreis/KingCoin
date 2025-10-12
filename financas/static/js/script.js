// ===== Scroll Fade =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    entry.target.classList.toggle('visible', entry.isIntersecting);
  });
}, { threshold: 0.2 });

document.querySelectorAll('.scrollFade').forEach(el => observer.observe(el));

// ===== Toggle Menu Mobile =====
const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");
const iconOpen = document.getElementById("icon-open");
const iconClose = document.getElementById("icon-close");

menuBtn.addEventListener("click", () => {
  const isHidden = mobileMenu.classList.contains("menu-hidden");
  mobileMenu.classList.toggle("menu-hidden", !isHidden);
  iconOpen.classList.toggle("hidden", isHidden);
  iconClose.classList.toggle("hidden", !isHidden);
});

// ===== Toggle Tema Desktop =====
const themeToggle = document.getElementById("theme-toggle");
const sunIcon = document.getElementById("sun-icon");
const moonIcon = document.getElementById("moon-icon");

themeToggle.addEventListener("click", () => {
  const isDark = document.documentElement.classList.toggle("dark");
  sunIcon.classList.toggle("hidden", !isDark);
  moonIcon.classList.toggle("hidden", isDark);
});

// ===== Toggle Tema Mobile =====
const themeToggleMobile = document.getElementById("theme-toggle-mobile");
const sunIconMobile = document.getElementById("sun-icon-mobile");
const moonIconMobile = document.getElementById("moon-icon-mobile");

themeToggleMobile.addEventListener("click", () => {
  const isDark = document.documentElement.classList.toggle("dark");
  sunIconMobile.classList.toggle("hidden", !isDark);
  moonIconMobile.classList.toggle("hidden", isDark);
});
