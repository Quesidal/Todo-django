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
let deleteProjBtn = document.getElementsByClassName('delete-proj');

for (let i = 0; i < deleteProjBtn.length; i++) {
    deleteProjBtn[i].addEventListener("click", function (event) {
        let proj_uuid = this.id.slice(13);
        let elem_id = "proj-task-counter-" + this.id.slice(13);
        let count_task = document.getElementById(elem_id).innerHTML;
        if (count_task > 0) {
            Swal.fire({
                type: 'warning',
                title: 'Oops...',
                text: 'You have ' + count_task + ' unresolved tasks!',
            })
        } else {
            window.location.href = '/project/delete/' + proj_uuid;
        }
    });
}