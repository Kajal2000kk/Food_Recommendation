import streamlit as st
from streamlit.logger import get_logger
import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/jpg;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_jpg_as_page_bg('imgs/img4.jpg')

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
       this is testing.
    """
    )


if __name__ == "__main__":
    run()
