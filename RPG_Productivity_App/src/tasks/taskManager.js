import { calculateRewards, applyRewards } from '../rpg/gameLogic.js';
let tasks = [];
export const getTasks = () => tasks;
export const addTask = (title,type,stat,difficulty='easy')=>{
    const newTask={ id:Date.now(), title,type,stat,difficulty,completed:false };
    tasks.push(newTask);
    window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks}));
    return newTask;
};
export const completeTask=(taskId)=>{
    const task = tasks.find(t=>t.id===taskId);
    if(!task) return;
    if(task.type==='todo') task.completed=true;
    const rewards = calculateRewards(task.difficulty,task.stat);
    applyRewards(rewards,task.stat);
    window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks}));
    return rewards;
};
export const deleteTask=(taskId)=>{ tasks = tasks.filter(t=>t.id!==taskId); window.dispatchEvent(new CustomEvent('tasks-update',{detail:tasks})); };