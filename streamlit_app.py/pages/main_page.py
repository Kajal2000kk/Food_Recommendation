import streamlit as st
st.sidebar.write("Hello")
# Contents of ~/my_app/main_page.py
import streamlit as st

# st.set_page_config(page_title = "This is a Multipage WebApp")
# st.title("This is the Home Page Geeks.")
# st.sidebar.success("Select Any Page from here")
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
st.sidebar.success("Select Any Page from here")

# def main_page():
#     st.markdown("# Main page 🎈")
#     st.sidebar.markdown("# Main page 🎈")

# def page_2():
#     st.markdown("# Page_2 ❄️")
#     st.sidebar.markdown("# Page_2 ❄️")

# def page_3():
#     st.markdown("# Page 3 🎉")
#     st.sidebar.markdown("# Page 3 🎉")

# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Page_2": page_2,
#     "Page_3": page_3,
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()
