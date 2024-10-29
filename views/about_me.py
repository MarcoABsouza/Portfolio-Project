import streamlit as st

# --- Section --- #
col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image('assets/Foto-Marco-Aurelio.jpg', width=230)
with col2:
    st.title('Marco Aurelio', anchor=False)
    st.write(
        " Hi, I'm a recent Computer Science graduate ready to turn data into strategic information and drive smart decision-making. I'm also ready to create automations and systems to simplify everyday tasks. "
    )
    st.subheader("Contact Me")
    st.write(":material/mail: mabdsouza@outlook.com")

# --- Experience & Qualifications --- #
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Degree in Computer Science from UFCAT in Brazil.
    - 1 year's experience working with NLP.
    - 1 year's experience in systems development and automation work.
    - Good communication and proactive in starting new challenges.
    - Good undestanding of statistical principles and their respective applications.
    """
)

# --- Skills --- #
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Python e Java
    - Power BI
    - ETL (Extract, Transform, Load)
    - MySQL e MongoDB
    - Artificial Intelligence
    """
)



