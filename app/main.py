import streamlit as st
import pickle
import pandas as pd


# sidebar section

def add_sidebar():
    st.sidebar.header('Cell Nuclei Detals')

# main function
def main():
    st.set_page_config(
        page_title = 'Breast Cancer Predictor',
        page_icon= ':female_doctor:',
        layout= 'wide',
        initial_sidebar_state= 'expanded'
    )

    # sidebar

    add_sidebar()
    # container

    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Machine-learning dashboard to predict whether a cell cluster is benign or malignant using Python and Streamlit. machine-learning dashboard to predict whether a cell cluster is benign or malignant using Python and Streamlit.')

    col1, col2 = st.columns([4,1]) 

    with col1:
        st.write('This is col 1')  
    with col2:
        st.write('This is col 2')  


if __name__ == '__main__':
    main()