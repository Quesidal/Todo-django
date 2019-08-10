const isAddFormActive = false;
const addTaskBtn = document.getElementById('add-task-btn');
let cancelTaskBtn = document.getElementById('cancel-task-btn');
const addTaskForm = document.getElementById('add-task');

const showAddTaskForm = () => {
    addTaskForm.style.display = 'flex';
};

const hideAddTaskForm = () => {
    addTaskForm.style.display = 'none';
};

addTaskBtn.addEventListener('click', showAddTaskForm);
cancelTaskBtn.addEventListener('click', hideAddTaskForm);

const addProjBtn = document.getElementById('add-proj-btn');
let cancelProjBtn = document.getElementById('cancel-proj-btn');
const addProjForm = document.getElementById('add-proj');

const showAddProjForm = () => {
    addProjForm.style.display = 'flex';
};

const hideAddProjForm = () => {
    addProjForm.style.display = 'none';
};

addProjBtn.addEventListener('click', showAddProjForm);
cancelProjBtn.addEventListener('click', hideAddProjForm);