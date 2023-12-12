import streamlit as st

st.set_page_config(
    page_title="Nabhan's Portofolio",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="	:ear_of_rice:"
)

def main():
    a1, a2 = st.columns((3,8))
    
    with a1:
        image_path = "https://github.com/euclideands/Projects/blob/main/Nabhan%20Portofolio/Profile%20Picture.png?raw=true"  # Replace with the actual path or URL of your image
        st.image(image_path, 
                 caption='Your Image Caption', 
                 width = 200)
    with a2:
        st.title("Nabhan Nabilah's Portofolio Site")
        st.write("TRDYTFVYBYJHBJKNJKNJKNJ")
        st.download_button(
            label = " 📄 Download Resume",
            data = PDFbyte,
            file_name = resume_file.name,
            mime = "application/octet-stream",
        )
        st.write("📫", EMAIL)
if __name__ == "__main__":
    main()
