import { calculateRewards, applyRewards } from '../rpg/gameLogic.js';
let tasks = [];
export const getTasks = () => tasks;
export const addTask = (title,type,stat,difficulty='easy') => { const newTask={id:Date.now(),title,type,stat,difficulty,completed:false}; tasks.push(newTask); window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks})); return newTask; };
export const completeTask = (taskId) => { const t=tasks.find(t=>t.id===taskId); if(!t) return; if(t.type==='todo') t.completed=true; const r=calculateRewards(t.difficulty,t.stat); applyRewards(r,t.stat); window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks})); return r; };
export const deleteTask = (taskId) => { tasks=tasks.filter(t=>t.id!==taskId); window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks})); };