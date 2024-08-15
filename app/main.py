import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import numpy as np



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

# Scaled data

def get_scaled_data(input_dict):
    data = get_clean_data()

    X = data.drop(['diagnosis'], axis=1)

    scaled_dict = {}

    for key,value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val)/(max_val - min_val)
        scaled_dict[key] = scaled_value

    return scaled_dict


# radar_chart_visualization col 1
def get_radar_chart(input_data):
    input_data = get_scaled_data(input_data)

    categories = ['Radius','Texture','Perimeter','Area','Smoothness',
                 'Compactness','Concavity','Concave points','Symmetry','Fractal dimension' ]
    
    # Create the radar chart
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
        range=[0, 1]
        )),
    showlegend=True
    )

    return fig

# add predictions col 2
def add_predictions(input_data):
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    input_array = np.array(list(input_data.values())).reshape(1,-1)
    input_array_scaled = scaler.transform(input_array)
    
    # Making real predictions using the model
    prediction =  model.predict(input_array_scaled)
    
    st.subheader("Cell Cluster Prediction")
    st.write("The cell cluster is:")

    if prediction[0] == 0:
        st.write('Begnin')
    else:
        st.write('Malicious')
    

    st.write("The probability of being Benign: ",model.predict_proba(input_array_scaled)[0][0])
    st.write("The probability of being Malicious: ",model.predict_proba(input_array_scaled)[0][1])
    st.write("This app can aassist medical professionals in making a diagnosis.")


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
        add_predictions(input_data) 


if __name__ == '__main__':
    main()