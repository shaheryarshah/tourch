import streamlit as st

# Initialize state
if 'torch_on' not in st.session_state:
    st.session_state.torch_on = False

# Function to toggle the torch state
def toggle_torch():
    st.session_state.torch_on = not st.session_state.torch_on

# Button for toggling
st.button("Toggle Torch", on_click=toggle_torch)

# Display the state of the torch
if st.session_state.torch_on:
    st.write("Torch is ON")
else:
    st.write("Torch is OFF")
