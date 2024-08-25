import streamlit as st
import functions

todoList = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todoList:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")
