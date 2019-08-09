const isAddFormActive = false;
const addTaskBtn = document.getElementById('add-task-btn');
let cancelBtn = document.getElementById('cancel');
const addTaskForm = document.getElementById('add-task');

const showAddTaskForm = () => {
    addTaskForm.style.display = 'flex';
}

const hideAddTaskForm = () => {
    addTaskForm.style.display = 'none';
}

addTaskBtn.addEventListener('click', showAddTaskForm)
cancelBtn.addEventListener('click', hideAddTaskForm)