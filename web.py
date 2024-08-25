import streamlit as st
import functions

todoList = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todoList.append(todo)
    functions.write_todos(todoList)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todoList):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todoList.pop(index)
        functions.write_todos(todoList)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Todo Add", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")


st.session_state
