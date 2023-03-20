import streamlit as st
from functions import get_todos, write_todos
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter the todo", label_visibility='hidden',
              placeholder="Add a new todo", key="new_todo",
              on_change=add_todo)