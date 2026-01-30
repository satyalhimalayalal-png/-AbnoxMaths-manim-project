import { initAuth, signIn, signOut } from './src/auth/googleAuth.js';
import { renderSidebar, loadPage } from './src/ui/navigation.js';
import { renderHeroPage } from './src/ui/heroModule.js';
import { renderTaskPage } from './src/ui/taskModule.js';
import { getHero } from './src/rpg/gameLogic.js';

document.addEventListener('DOMContentLoaded', () => {
    renderSidebar();
    
    const authBtn = document.getElementById('auth-btn');
    authBtn.addEventListener('click', () => signIn());

    document.getElementById('menu-toggle').addEventListener('click', () => {
        document.getElementById('sidebar').classList.toggle('open');
    });

    initAuth((accessToken) => handleLoginSuccess());
});

function handleLoginSuccess() {
    document.getElementById('user-stats').classList.remove('hidden');
    
    const authBtn = document.getElementById('auth-btn');
    authBtn.innerText = 'Sign Out';
    authBtn.onclick = signOut;

    loadPage('home');
    console.log('User logged in. Ready to sync with Drive.');
}

window.addEventListener('hero-update', () => {
    const hero = getHero();
    document.getElementById('user-level').innerText = `Lvl ${hero.level}`;
    document.getElementById('user-gold').innerText = Math.floor(hero.gold);
    const avatar = document.getElementById('user-avatar');
    if(hero.classId === 'mage') avatar.style.background = '#3b82f6';
    if(hero.classId === 'warrior') avatar.style.background = '#ef4444';
});