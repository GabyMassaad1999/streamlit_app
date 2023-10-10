import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px

url="https://github.com/GabyMassaad1999/streamlit_app/blob/main/heart_failure_clinical_records_dataset.csv"

# Load the dataset
data = pd.read_csv(url)

# Sidebar with navigation options
navigation = st.sidebar.radio("Navigation", ("Introduction", "First visualization", "Second visualization"))

# Add an interactive feature to filter data
st.sidebar.header("Data Filtering")
age_range = st.sidebar.slider("Filter by Age Range", min(data['age']), max(data['age']), (min(data['age']), max(data['age'])))

# Filter data based on user input
filtered_data = data[(data['age'] >= age_range[0]) & (data['age'] <= age_range[1])]

# Page content based on navigation
if navigation == "Introduction":
    st.title('Streamlit Assignment')
    st.title('Explanation')
    st.write("Welcome to the streamlit assignment. That is the first Web Application that I have developed for the Data Visualization course.I have extracted two visuals from the previous Plotly assignment and used them inside this application as instructed while adding two interactive features to them ('the sidebar filter and the tooltips').")
elif navigation == "First visualization":
    st.title('First Visualization')
    hist_data = [filtered_data["age"].values]
    group_labels = ['age']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title_text='Age Distribution plot')

    # Add tooltips to the plot
    fig.update_traces(hoverinfo='x+y')
    
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")
    st.write("The first interactive feature is the sidebar that does the filtering on the variable age. The second interactive feature is the tooltips. When you hover over a data point on the plot, it will display information about the age value on the x-axis and the density (y-value) at that point on the y-axis. ")
elif navigation == "Second visualization":
    st.title('Second Visualization')
    # BoxPlot
    fig = px.box(filtered_data, x='sex', y='age', points="all")
    fig.update_layout(
        title_text="Gender-wise Age Spread, Male = 1 Female = 0")
    
    # Add tooltips to the plot
    fig.update_traces(hoverinfo='x+y')
    
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")
    st.write("The first interactive feature is the sidebar that does the filtering on the variable age.The second interactive feature is the tooltips. When you hover over a box in the box plot, it will display information about the age values within that box. It typically shows the minimum, maximum, median, and quartile values for the age distribution within the selected box.")
