import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a CVS file", type="cvs")
if uploaded_file is not None:

    st.write("File uploaded...")
    df = pd.read_cvs(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe ())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_column = df[selected_columns].unique()
    selected_vlaue = st.selectbox("Select value", unique_value ) # type: ignore

    filtered_df = df[df[selected_columns] == selected_vlaue]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x_axis column",columns)
    y_column = st.selectbox("Select y_axis column",columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
      st.write("Waiting on file upload.......")  



