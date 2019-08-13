const addTaskBtn = document.getElementById('add-task-btn');
let cancelTaskBtn = document.getElementById('cancel-task-btn');
const addTaskForm = document.getElementById('add-task');
const isProjectsEmpty = document.getElementsByClassName('projects-list')[0].children.length === 1;
const showAddTaskForm = () => {
    if (isProjectsEmpty) {
        Swal.fire({
            type: 'warning',
            title: 'Oops...',
            text: 'You have  unresolved tasks!',
        })
    } else {
        addTaskForm.style.display = 'flex';
    }
};

const hideAddTaskForm = () => {
    addTaskForm.style.display = 'none';
};

addTaskBtn.addEventListener('click', showAddTaskForm);
cancelTaskBtn.addEventListener('click', hideAddTaskForm);


/* for proj form*/
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

/*for del btn*/
const deleteProjBtn = document.getElementsByClassName('delete-proj');

for (let i = 0; i < deleteProjBtn.length; i++) {
    deleteProjBtn[i].addEventListener("click", function (event) {
        const projUuid = this.id.slice(13);
        const elemId = "proj-task-counter-" + this.id.slice(13);
        const countTask = document.getElementById(elemId).innerHTML;
        if (countTask > 0) {
            Swal.fire({
                type: 'warning',
                title: 'Oops...',
                text: 'You have ' + countTask + ' unresolved tasks!',
            })
        } else {
            window.location.href = '/project/delete/' + projUuid;
        }
    });
}