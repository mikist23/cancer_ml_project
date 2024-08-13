import streamlit as st
import pickle
import pandas as pd

# cleaned data

def get_clean_data():
    data = pd.read_csv('data.csv')
    data = data.drop(['Unnamed: 32', 'id'], axis = 1)
    data['diagnosis'] = data['diagnosis'].map({'M':1,"B":0})
    return data


# sidebar section
def add_sidebar():
    st.sidebar.header('Cell Nuclei Detals')

    data = get_clean_data()

      # Define the labels
    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    # input data dictionary
    input_dict = {}
    

    # looping through all the key, values in the sidebar_labels
    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value = float(0),
            max_value = float(data[key].max()),
            value = float(data[key].mean())
        )

    return input_dict

# main function
def main():
    st.set_page_config(
        page_title = 'Breast Cancer Predictor',
        page_icon= ':female_doctor:',
        layout= 'wide',
        initial_sidebar_state= 'expanded'
    )

    # sidebar

    input_data = add_sidebar()
    # st.write(input_data)
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