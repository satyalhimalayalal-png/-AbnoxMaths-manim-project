export const CLASSES = {
    WARRIOR: { id: 'warrior', name: 'Warrior', base: { str: 15, int: 5, sta: 12, dex: 8 } },
    MAGE:    { id: 'mage', name: 'Mage',    base: { str: 5, int: 15, sta: 8, dex: 12 } },
    ROGUE:   { id: 'rogue', name: 'Rogue',   base: { str: 8, int: 10, sta: 8, dex: 15 } },
    HEALER:  { id: 'healer', name: 'Healer',  base: { str: 6, int: 12, sta: 15, dex: 7 } }
};
export const STATS = { STR:'STR', INT:'INT', STA:'STA', DEX:'DEX', NEUTRAL:'NEUTRAL' };
let hero = { name:'Player', classId:null, level:1, xp:0, maxXp:100, gold:0, stats:{str:10,int:10,sta:10,dex:10} };
export const getHero = () => hero;
export const setHeroClass = (classId) => { hero.classId = classId; hero.stats = {...CLASSES[classId.toUpperCase()].base}; hero.xp=0; hero.level=1; hero.gold=0; hero.maxXp=100; window.dispatchEvent(new CustomEvent('hero-update',{detail:hero})); };
export const calculateRewards = (difficulty, stat) => { let xp=10,gold=5; const diffMult=difficulty==='hard'?2:difficulty==='medium'?1.5:1; xp=Math.floor(xp*diffMult*(1+hero.stats.int*0.01)); gold=Math.floor(gold*diffMult*(1+hero.stats.dex*0.01)); return {xp,gold}; };
export const applyRewards = (rewards, statType) => { hero.xp+=rewards.xp; hero.gold+=rewards.gold; if(statType!=='NEUTRAL') hero.stats[statType.toLowerCase()]+=0.1; else Object.keys(hero.stats).forEach(k=>hero.stats[k]+=0.025); if(hero.xp>=hero.maxXp){ hero.level++; hero.xp-=hero.maxXp; hero.maxXp=Math.floor(hero.maxXp*1.5); alert('Leveled Up!'); } window.dispatchEvent(new CustomEvent('hero-update',{detail:hero})); return hero; };