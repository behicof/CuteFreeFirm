
import streamlit as st
from src.pages import home, chat, about

PAGES = {
    "Home": home,
    "Chat": chat,
    "About": about
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
