// Selectors
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");
const filterOption = document.querySelector(".filter-todo");

// Event Listener
document.addEventListener("DOMContentLoaded", getTodos);
todoButton.addEventListener("click", addTodo);
todoList.addEventListener("click", deleteCheck);
filterOption.addEventListener("click", filterTodo);

// Functions
function addTodo(event) {
  event.preventDefault();
  const todoText = todoInput.value;
  // Call backend API to add todo
  // Example: fetch('/add_todo', { method: 'POST', body: JSON.stringify({ text: todoText }) })

  // Clear todo input value
  todoInput.value = "";
}

function deleteCheck(e) {
  const item = e.target;
  // Delete todo
  if (item.classList[0] === "trash-btn") {
    const todo = item.parentElement;
    // Call backend API to delete todo
    // Example: fetch(`/delete_todo/${todo.id}`, { method: 'DELETE' })
    todo.remove();
  }
  // Check mark
  if (item.classList[0] === "complete-btn") {
    const todo = item.parentElement;
    todo.classList.toggle("completed");
    // Call backend API to update todo status
    // Example: fetch(`/update_todo/${todo.id}`, { method: 'PUT', body: JSON.stringify({ completed: todo.classList.contains('completed') }) })
  }
}

function filterTodo() {
  // Logic to filter todos
}

function getTodos() {
  // Call backend API to get todos
  // Example: fetch('/get_todos').then(response => response.json()).then(data => renderTodos(data))
}

function renderTodos(todos) {
  todos.forEach(todo => {
    // Create todo elements and append to todoList
  });
}
