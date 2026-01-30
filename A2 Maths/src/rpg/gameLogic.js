// src/rpg/gameLogic.js
export const CLASSES = {
    WARRIOR: { id: 'warrior', name: 'Warrior', base: { str: 15, int: 5, sta: 12, dex: 8 } },
    MAGE:    { id: 'mage', name: 'Mage',    base: { str: 5, int: 15, sta: 8, dex: 12 } },
    ROGUE:   { id: 'rogue', name: 'Rogue',   base: { str: 8, int: 10, sta: 8, dex: 15 } },
    HEALER:  { id: 'healer', name: 'Healer',  base: { str: 6, int: 12, sta: 15, dex: 7 } }
};

export const STATS = { STR:'Strength', INT:'Intelligence', STA:'Stamina', DEX:'Dexterity', NEUTRAL:'Neutral' };

let hero = { name:'Player', classId:null, level:1, xp:0, maxXp:100, gold:0, stats:{str:10,int:10,sta:10,dex:10} };

export const getHero = () => hero;

export const setHeroClass = (classId) => {
    if(!CLASSES[classId.toUpperCase()]) return;
    hero.classId = classId;
    hero.stats = { ...CLASSES[classId.toUpperCase()].base };
    hero.xp=0; hero.level=1; hero.gold=0; hero.maxXp=100;
    saveHeroState();
};

export const calculateRewards = (taskDifficulty, statType) => {
    let xp = 10, gold = 5;
    const diffMult = taskDifficulty==='hard'?2:taskDifficulty==='medium'?1.5:1;
    const xpBonus = 1 + (hero.stats.int*0.01);
    xp = Math.floor(xp*diffMult*xpBonus);
    const goldBonus = 1 + (hero.stats.dex*0.01);
    const isCrit = Math.random() < (hero.stats.dex*0.005);
    gold = Math.floor(gold*diffMult*goldBonus*(isCrit?1.5:1));
    return { xp, gold, isCrit };
};

export const applyRewards = (rewards, statType) => {
    hero.xp += rewards.xp;
    hero.gold += rewards.gold;
    if(statType==='NEUTRAL'){['str','int','sta','dex'].forEach(s=>hero.stats[s]=parseFloat((hero.stats[s]+0.025).toFixed(3)));}
    else { const key = statType.toLowerCase(); if(hero.stats[key]!==undefined) hero.stats[key]=parseFloat((hero.stats[key]+0.1).toFixed(3)); }
    if(hero.xp>=hero.maxXp){ hero.level++; hero.xp=hero.xp-hero.maxXp; hero.maxXp=Math.floor(hero.maxXp*1.5); alert(`Leveled Up! You are now Level ${hero.level}!`);}
    saveHeroState(); return hero;
};

function saveHeroState(){ window.dispatchEvent(new CustomEvent('hero-update',{detail:hero})); }