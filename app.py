import streamlit as st

# --- Page Setup --- #
about_page = st.Page(
    page='views/about_me.py',
    title='About me',
    icon=':material/account_circle:',
    default=True
)
projects_page = st.Page(
    page='views/projects.py',
    title='Projects',
    icon=':material/work:'
)

# --- Navigation Setup --- #
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [projects_page]
    }
)

# --- Run Navigation --- #
pg.run()