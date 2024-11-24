import streamlit as st
import pandas as pd
import numpy as np

# Title of the dashboard
st.title('Basic Streamlit Dashboard')

# Sidebar for user input
st.sidebar.header('User Input')
option = st.sidebar.selectbox('Select a number:', range(1, 11))

# Generate some data
data = pd.DataFrame({
    'Column 1': np.random.randn(100),
    'Column 2': np.random.randn(100) * option
})

# Display the data
st.write('## Data')
st.write(data)

# Display a line chart
st.write('## Line Chart')
st.line_chart(data)

# Display a bar chart
st.write('## Bar Chart')
st.bar_chart(data)

# Display a map
st.write('## Map')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)