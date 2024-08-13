import streamlit as st
import pickle
import pandas as pd


def main():
    st.set_page_config(
        page_title = 'Breast Cancer Predictor',
        page_icon= ':female_doctor:',
        layout= 'wide',
        initial_sidebar_state= 'expanded'
    )

    st.write('Hello woorlds')



if __name__ == '__main__':
    main()