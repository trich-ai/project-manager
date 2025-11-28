import streamlit as st

st.set_page_config(page_title="Tim’s Tiny Project Manager", page_icon="📝")

st.title("📝 Tiny Project Steps")
st.caption("A starter workflow you can expand any time.")

# ---- Initialize ----
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "Get client list", "done": False},
        {"text": "Pull tax data", "done": False}
    ]

# ---- Display Tasks ----
st.subheader("Project Steps")

for i, task in enumerate(st.session_state.tasks):
    checked = st.checkbox(task["text"], value=task["done"], key=f"task_{i}")
    st.session_state.tasks[i]["done"] = checked

# ---- Add new step ----
st.subheader("Add Additional Steps")
new_task = st.text_input("Describe next step:")
if st.button("Add Step"):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.rerun()

# ---- Clear completed ----
if st.button("Clear Completed"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.rerun()

st.caption("Session-based task list — no permanent storage yet.")
