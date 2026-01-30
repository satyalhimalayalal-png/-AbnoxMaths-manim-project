import { getIcon } from './icons.js';
import { renderHeroPage } from './heroModule.js';
import { renderTaskPage } from './taskModule.js';
const pages=[{id:'home',title:'Quest Log'},{id:'hero',title:'Hero'},{id:'tasks',title:'Tasks'}];
export const renderSidebar=()=>{ const navList=document.getElementById('nav-list'); navList.innerHTML=''; pages.forEach(p=>{ const li=document.createElement('li'); li.innerHTML=`<span class="nav-link" data-page="${p.id}">${getIcon(p.id)} ${p.title}</span>`; li.querySelector('span').onclick=()=>loadPage(p.id); navList.appendChild(li); }); };
export const loadPage=(pageId)=>{ const content=document.getElementById('content-area'); if(pageId==='hero') renderHeroPage(content); else if(pageId==='tasks') renderTaskPage(content); else content.innerHTML='<h2>Welcome!</h2>'; };