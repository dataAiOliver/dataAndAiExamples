"""
python -m streamlit run .\streamlitExampleRegression.py
"""

import streamlit as st
import pandas as pd
import pickle, os
from io import BytesIO

def process_data(df):
    y_pred = pipeline.predict(df)
    df["predicted"] = y_pred
    return df

def main():
    st.title('Excel File Processor')

    uploaded_file = st.file_uploader("Drag and drop or click to upload a file.", type=['xlsx', 'xls'])

    if uploaded_file is not None:
        # Read the uploaded Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        # Process the DataFrame using a custom function
        processed_df = process_data(df)

        # Show the processed DataFrame in the app (optional)
        st.write("Processed Data:", processed_df)

        # Use a BytesIO buffer as the Excel writer
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            processed_df.to_excel(writer, index=False)
        
        # Important: seek to the beginning of the stream
        output.seek(0)

        # Set up the download button
        st.download_button(label="Download Processed Excel File",
                        data=output,
                        file_name="processed_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# load pipeline
with open(os.path.join("out", "savedRegPipeline.pkl"), "rb") as f:
    j_pipeline = pickle.load(f)

pipeline = j_pipeline["pipeline"]

# python -m streamlit run .\streamlitExampleRegression.py
if __name__ == "__main__":
    main()
