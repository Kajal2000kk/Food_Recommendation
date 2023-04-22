import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)
def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Food Solutions! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
    We are the foodie who love to eat and explore different food but we are engineers also so here is combination of both.
    so people who love to eat here we have complete soltion for them for food recommendation.
    """
    )


if __name__ == "__main__":
    run()
