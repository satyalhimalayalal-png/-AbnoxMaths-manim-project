import { getHero, setHeroClass, CLASSES } from '../rpg/gameLogic.js';
export const renderHeroPage = (container) => {
    const hero = getHero();
    if(!hero.classId){ renderClassSelection(container); return; }
    container.innerHTML=`
        <div class="hero-dashboard">
            <div class="hero-header">
                <div class="avatar-large">${hero.classId==='mage'?'🧙‍♂️':hero.classId==='warrior'?'⚔️':'🗡️'}</div>
                <div><h2>${hero.name}</h2><p>Level ${hero.level} ${CLASSES[hero.classId.toUpperCase()].name}</p></div>
            </div>
            <div class="bars-container">
                <div class="bar-label"><span>XP</span> <span>${hero.xp}/${hero.maxXp}</span></div>
                <div class="progress-bar"><div class="fill xp-fill" style="width:${(hero.xp/hero.maxXp)*100}%"></div></div>
            </div>
            <div class="stats-grid">
                ${renderStatBox('STR',hero.stats.str,'💪')}
                ${renderStatBox('INT',hero.stats.int,'🧠')}
                ${renderStatBox('STA',hero.stats.sta,'❤️')}
                ${renderStatBox('DEX',hero.stats.dex,'🦵')}
            </div>
            <div class="inventory-preview"><h3>💰 Gold: ${hero.gold}</h3></div>
        </div>`;
};
const renderStatBox=(label,value,icon)=>`<div class="stat-card"><div class="stat-icon">${icon}</div><div class="stat-info"><span class="stat-label">${label}</span><span class="stat-value">${Math.floor(value)}</span></div></div>`;
const renderClassSelection=(container)=>{
    container.innerHTML=`<h1>Choose Your Path</h1><div class="class-grid" id="class-grid"></div>`;
    const grid=container.querySelector('#class-grid');
    Object.values(CLASSES).forEach(cls=>{
        const card=document.createElement('div');
        card.className='class-card';
        card.innerHTML=`<h3>${cls.name}</h3><p>STR:${cls.base.str} INT:${cls.base.int} STA:${cls.base.sta} DEX:${cls.base.dex}</p><button class="btn-primary">Select ${cls.name}</button>`;
        card.querySelector('button').onclick=()=>{setHeroClass(cls.id); renderHeroPage(container);};
        grid.appendChild(card);
    });
};