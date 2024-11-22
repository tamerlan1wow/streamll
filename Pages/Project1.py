import streamlit as st
import pandas as pd


class Project1:
    def __init__(self):
        pass

    def app(self):
        st.title('Creation of DataFrame')

        # File uploader
        upload = st.file_uploader("Choose CSV file", type="csv")

        # Check if file is uploaded
        if upload is not None:
            # Read CSV into DataFrame
            df = pd.read_csv(upload)

            # Select column for filtering
            column = st.selectbox("Choose column for filter", df.columns)

            if column:
                # Get unique values of the selected column
                unique_values = df[column].unique()

                # Select values for filtering using multiselect
                selected_values = st.multiselect(f"Select values for {column}", options=unique_values,
                                                 default=unique_values)

                # Filter DataFrame based on selected values
                filtered_df = df[df[column].isin(selected_values)]

                # Display filtered DataFrame
                st.dataframe(filtered_df, height=400, width=600)

        else:
            st.warning("Please upload a CSV file")

        # Custom styling
        st.markdown("""
            <style>
                h1 {
                    color: green;
                    font-size: 18px;
                    text-align: center;
                }
            </style>
        """, unsafe_allow_html=True)
