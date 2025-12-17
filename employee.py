import streamlit as st
import sqlite3
import pandas as pd
# Database Connection
conn = sqlite3.connect("emp.db", check_same_thread=False)
cursor = conn.cursor()
# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER,
    name TEXT,
    sal INTEGER
)
""")
conn.commit()
# Page Config
st.title("Employee Management System")
menu = ["INSERT", "VIEW"]
choice = st.sidebar.selectbox("Menu", menu)
# Add Employee
if choice == "INSERT":
    eid = st.number_input("ID", step=1)
    name = st.text_input("NAME")
    sal = st.number_input("SALARY", step=1)
    if st.button("SAVE"):
        cursor.execute(
            "INSERT INTO employee(id, name, sal) VALUES (?, ?, ?)",
            (eid, name, sal)
        )
        conn.commit()
        st.snow()
        st.success("EMPLOYEE ADDED SUCCESSFULLY")
# View Employee
if choice == "VIEW":
    st.subheader("Employee Records")
    data = cursor.execute("SELECT * FROM employee")
    st.dataframe(data)
