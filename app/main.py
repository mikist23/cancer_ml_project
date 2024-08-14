import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go



# cleaned data

def get_clean_data():
    data = pd.read_csv('data.csv')
    data = data.drop(['Unnamed: 32', 'id'], axis = 1)
    data['diagnosis'] = data['diagnosis'].map({'M':1,"B":0})
    return data

# Scaled data

def get_scaled_data(input_dict):
    data = get_clean_data()

    X = data.drop(columns = 'diagnosis')
    













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
# radar_chart_visualization
def get_radar_chart(input_data):
    categories = ['Radius','Texture','Perimeter','Area','Smoothness',
                 'Compactness','Concavity','Concave points','Symmetry','Fractal dimension' ]
    

    fig = go.Figure()

    # Add the traces
    fig.add_trace(
        go.Scatterpolar(
            r=[input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
                input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
                input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
                input_data['fractal_dimension_mean']],
            theta=categories,
            fill='toself',
            name='Mean'
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
                input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
                input_data['concave points_se'], input_data['symmetry_se'], input_data['fractal_dimension_se']],
            theta=categories,
            fill='toself',
            name='Standard Error'
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
                input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
                input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
                input_data['fractal_dimension_worst']],
            theta=categories,
            fill='toself',
            name='Worst value'
        )
    )
    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=True
    )

    return fig





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
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        st.write('This is col 2')  


if __name__ == '__main__':
    main()