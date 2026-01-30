import { getTasks, addTask, completeTask } from '../tasks/taskManager.js';
import { STATS } from '../rpg/gameLogic.js';
export const renderTaskPage=(container)=>{
    container.innerHTML=`
        <div class="task-page">
            <div class="task-form panel">
                <input type="text" id="task-input" placeholder="What needs to be done?" />
                <select id="task-type"><option value="todo">Todo</option><option value="daily">Daily</option><option value="habit">Habit</option></select>
                <select id="task-stat">${Object.keys(STATS).map(k=>`<option value="${k}">${STATS[k]}</option>`).join('')}</select>
                <select id="task-diff"><option value="easy">Easy</option><option value="medium">Medium</option><option value="hard">Hard</option></select>
                <button id="add-task-btn" class="btn-primary">+</button>
            </div>
            <div class="task-columns">
                <div class="column" id="col-habit"><h3>Habits</h3><div class="list"></div></div>
                <div class="column" id="col-daily"><h3>Dailies</h3><div class="list"></div></div>
                <div class="column" id="col-todo"><h3>To-Dos</h3><div class="list"></div></div>
            </div>
        </div>`;
    document.getElementById('add-task-btn').onclick=()=>{const t=document.getElementById('task-input').value,ty=document.getElementById('task-type').value,s=document.getElementById('task-stat').value,d=document.getElementById('task-diff').value;if(t){addTask(t,ty,s,d);document.getElementById('task-input').value=''; refreshLists();}};
    refreshLists();
};
const refreshLists=()=>{
    const tasks=getTasks();
    ['habit','daily','todo'].forEach(type=>{document.querySelector(`#col-${type} .list`).innerHTML='';});
    tasks.forEach(task=>{
        if(task.completed && task.type==='todo') return;
        const el=document.createElement('div');
        el.className=`task-card ${task.difficulty}`;
        el.innerHTML=`<div class="task-main"><span class="task-stat-badge ${task.stat}">${task.stat}</span><span>${task.title}</span></div><button class="check-btn">✔</button>`;
        el.querySelector('.check-btn').onclick=()=>{completeTask(task.id); refreshLists();};
        document.querySelector(`#col-${task.type} .list`).appendChild(el);
    });
};