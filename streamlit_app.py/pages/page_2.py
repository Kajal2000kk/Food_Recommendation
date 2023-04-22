import streamlit as st
import test2
from PIL import Image
import base64
t = test2.result()
# st.sidebar.write("click [recommendation-diet](https://Kajal2000kk/Food_Recommendation)")
# st.write("# Welcome to Diet Recommendation System! 👋")
# st.sidebar.success("Select a recommendation app.")

# st.markdown(
#     """
#     A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
#     You can find more details and the whole project on my [repo](https://github.com/zakaria-narjis/Diet-Recommendation-System).
#     """)
foods = t.food()

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



# favicon = Image.open("imgs/logo.png")
# st.set_page_config(page_title='Tasty Foods', page_icon = favicon)

st.markdown("<h1 style='text-align: center;'>Tasty Foods </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Food Recommendation System </h1>", unsafe_allow_html=True)

food_choice = st.selectbox("Pick a Food ", foods)
st.write("------------------")

c1, c2, c3 = st.columns(3)

m1, m2, m3 = t.query(food_choice)

with c1:
    st.subheader("Simple Content Based Filtering")
    st.write("Recommends food based on similar foods")
    st.write("------------------")
    for index, ele in enumerate(m1):
        st.write(index,ele.title())
    st.write("------------------")

with c2:
    st.subheader("Collaborative Based Filtering")
    st.write("Recommends food based on similar users")
    st.write("------------------")
    if m3 == None:
        st.write("**Less user ratings for this food item !!!**")
        st.write("So, the recommender cannot pull any recommendations ")
    else:
        for index, ele in enumerate(m3):
            st.write(index, ele.title())
    st.write("------------------")

with c3:
    st.subheader("Advanced Content Based Filtering")
    st.write("Recommends food based on similar foods and its features")
    st.write("------------------")
    for index, ele in enumerate(m2):
        st.write(index, ele.title())
    st.write("------------------")
Footer
