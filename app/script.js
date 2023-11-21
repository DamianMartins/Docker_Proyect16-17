document.addEventListener('DOMContentLoaded', function () {
    const taskInput = document.getElementById('task');
    const taskList = document.getElementById('taskList');
    const addTaskButton = document.getElementById('addTask');

    addTaskButton.addEventListener('click', function () {
        const taskText = taskInput.value.trim();
        if (taskText) {
            const taskItem = document.createElement('li');
            taskItem.innerHTML = `
                <input type="checkbox" class="completed">
                <span>${taskText}</span>
                <button class="delete">Eliminar</button>
            `;
            taskList.appendChild(taskItem);
            taskInput.value = '';

            // Marcar tarea como completada
            const checkbox = taskItem.querySelector('.completed');
            checkbox.addEventListener('change', function () {
                if (checkbox.checked) {
                    taskItem.classList.add('done');
                } else {
                    taskItem.classList.remove('done');
                }
            });

            // Eliminar tarea
            const deleteButton = taskItem.querySelector('.delete');
            deleteButton.addEventListener('click', function () {
                taskList.removeChild(taskItem);
            });
        }
    });
});
