#import libraries
import streamlit as st
import pandas as pd

# Function to calculate the CSV size
def calculate_csv_size(file):
    """
    Calculates the size of the CSV dataset based on the number of attributes and entities.

    Parameters:
        file (BytesIO): The input CSV file as a BytesIO object.

    Returns:
        int: The size of the CSV dataset.
    """
    try:
        # Read the CSV file into a DataFrame
        dataframe = pd.read_csv(file)

        num_attributes = len(dataframe.columns)
        num_entities = len(dataframe)

        csv_size = num_attributes * num_entities
        return csv_size
    except Exception as e:
        st.error(f"Error: {e}")
        return 0

# Function to extract the number of relationships
def extract_relationships(file):
    """
    Extracts the number of relationships in the CSV dataset.

    Parameters:
        file (BytesIO): The input CSV file as a BytesIO object.

    Returns:
        int: The number of relationships in the dataset.
    """
    try:
        # Read the CSV file into a DataFrame
        dataframe = pd.read_csv(file)

        # Calculate the number of relationships
        num_rows = len(dataframe)
        num_columns = len(dataframe.columns)

        # Check if the dataset has multi-index
        if isinstance(dataframe.index, pd.MultiIndex):
            # Calculate the number of index combinations
            num_index_combinations = 1

            # Iterate over the index levels to extract unique values
            for i in range(dataframe.index.nlevels):
                index_values = dataframe.index.get_level_values(i)
                num_index_combinations *= len(index_values.unique())

            # Calculate the total number of relationships
            num_relationships = num_rows * num_columns * num_columns * num_index_combinations
        else:
            # Calculate the total number of relationships
            num_relationships = num_rows * num_columns * num_columns

        return num_relationships
    except Exception as e:
        st.error(f"Error: {e}")
        return 0


# Streamlit app
def main():
    st.title("Dataset Analysis")

    # File selection
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Convert CSV file to DataFrame
            dataframe = pd.read_csv(uploaded_file)
            
            # Calculate CSV size
            csv_size = calculate_csv_size(dataframe)
            st.subheader("CSV Size")
            st.write(f"The size of the dataset is: {csv_size}")

            # Extract number of relationships
            num_relationships = extract_relationships(dataframe)
            st.subheader("Number of Relationships")
            st.write(f"The number of relationships in the dataset is: {num_relationships}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
