import base64
import streamlit as st

st.sidebar.write("click [recommendation-diet](https://github.com/Kajal2000kk/Food_Recommendation)")
st.write("# Welcome to Diet Recommendation System! 👋")
st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo](https://github.com/Kajal2000kk/Food_Recommendation).
    """)
def main_page():
    st.markdown("# Page_2 ")
    st.sidebar.markdown("# Page_2 ")
def page_2():
    st.markdown("# Page_2 ❄️")
    st.sidebar.markdown("# Page_2 ❄️")
def page_3():
    st.markdown("# Page_2 ")
    st.sidebar.markdown("# Page_2 ")
page_names_to_funcs = {
     "Main Page": main_page,
     "Page_2": page_2,
     "Page_3": page_3,
}
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>

  ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('imgs/img2.jfif')
