import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Header
st.header("Cars analysis in US")

# Read CSV
car_data = pd.read_csv('vehicles_us.csv')

# --- Options Buttons ---
st.subheader("Clickable Buttons")

# Button for histogram
if st.button('Build a histogram'):
    st.write('Distribution of car odometers')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Odometer Histogram')
    st.plotly_chart(fig_hist, use_container_width=True)

# Scatter plot button
if st.button('Build a scatter plot'):
    st.write('Relationship between price and odometer reading')
    fig_scatter = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                             y=car_data['price'],
                                             mode='markers')])
    fig_scatter.update_layout(title_text='Price vs. Odometer',
                              xaxis_title='Odometer',
                              yaxis_title='Price')
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- Checkbox ---
st.subheader("Checkboxes")

# Checkbox for histogram
if st.checkbox('Show odometer histogram'):
    st.write('Distribution of car odometers')
    fig_hist_cb = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist_cb.update_layout(title_text='Odometer Histogram')
    st.plotly_chart(fig_hist_cb, use_container_width=True)

# Checkbox for scatter plot
if st.checkbox('Show scatter plot'):
    st.write('Relationship between price and odometer reading')
    fig_scatter_cb = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                                y=car_data['price'],
                                                mode='markers')])
    fig_scatter_cb.update_layout(title_text='Price vs Odometer',
                                 xaxis_title='Odometer',
                                 yaxis_title='Price')
    st.plotly_chart(fig_scatter_cb, use_container_width=True)