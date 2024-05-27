const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const submitBtn = document.querySelector('.submitBtn');
const todoInput = document.getElementById('content');
const TODOS_KEY = 'todos';

function saveTodos(todos) {
    console.log(JSON.stringify(todos));
    localStorage.setItem(TODOS_KEY, JSON.stringify(todos));
}

function submitAddTodo(event) {
    event.preventDefault(); // 새로고침 방지

    const todoText = todoInput.value.trim();
    if (todoText !== '') {
        const newTodo = {
            text: todoText,
            id: Date.now(),
        };

        const li = document.createElement('li');
        const span = document.createElement('span');
        span.innerText = newTodo.text;
        li.appendChild(span); //

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = '삭제';
        deleteBtn.addEventListener('click', deleteTodo);

        li.appendChild(deleteBtn);
        todoList.appendChild(li);

        let todos = JSON.parse(localStorage.getItem('todos')) || [];
        todos.push(todoText);
        saveTodos(todos);

        todoInput.value = '';
    }
}

function deleteTodo(event) {
    const li = event.target.parentElement;
    const todoText = li.firstChild.textContent;

    let todos = JSON.parse(localStorage.getItem('todos')) || [];
    todos = todos.filter((todo) => todo !== todoText);
    saveTodos(todos);

    todoList.removeChild(li);
}

function loadTodos() {
    let todos = JSON.parse(localStorage.getItem('todos')) || [];
    todos.forEach((todo) => {
        const li = document.createElement('li');
        li.textContent = todo;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = '삭제';
        deleteBtn.addEventListener('click', deleteTodo);

        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });
}

todoForm.addEventListener('submit', submitAddTodo);
document.addEventListener('DOMContentLoaded', loadTodos);
