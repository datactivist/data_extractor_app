import streamlit as st
import csv

# Function to calculate the CSV size
def calculate_csv_size(file_path):
    try:
        content = file_path.read().decode('utf-8')  # Read the file content as a string
        reader = csv.reader(content.splitlines())
        num_attributes = len(next(reader))
        num_entities = sum(1 for _ in reader)

        csv_size = num_attributes * num_entities
        return csv_size
    except IOError:
        st.error("Error: File not found or unable to open the file.")
        return 0


# Function to extract the number of relationships
def extract_relationships(file_path):
    try:
        content = file_path.read().decode('utf-8')  # Read the file content as a string
        reader = csv.reader(content.splitlines())

        # Read the CSV headers into a list of lists
        headers = []
        for _ in range(1):  # Assuming up to 1 row can contain column headers
            headers.append(next(reader))

        # Read the CSV data into a list of lists
        data = [row for row in reader]

        # Calculate the number of relationships

        # Count the number of rows in the data
        num_rows = len(data)

        # Count the number of columns by considering the first header row
        num_columns = len(headers[0])

        # Calculate the number of index combinations
        num_index_combinations = 1

        # Iterate over the first 1 column to extract index values
        for i in range(1):
            # Extract unique values for the current index column in the data rows
            # Only consider rows that have enough elements to access the index
            index_values = set(row[i] for row in data if len(row) > i)

            # Multiply the count of index combinations by the number of unique values
            num_index_combinations *= len(index_values)

        # Calculate the total number of relationships
        num_relationships = num_rows * num_columns * num_columns * num_index_combinations

        return num_relationships

    except IOError:
        st.error("Error: File not found or unable to open the file.")
        return 0


# Streamlit app
def main():
    st.title("Dataset Analysis")

    # File selection
    file_path = st.file_uploader("Upload CSV File", type=["csv"])
    
    if file_path is not None:
        # Calculate CSV size
        csv_size = calculate_csv_size(file_path)
        st.subheader("CSV Size")
        st.write(f"The size of the dataset is: {csv_size}")

        # Extract number of relationships
        num_relationships = extract_relationships(file_path)
        st.subheader("Number of Relationships")
        st.write(f"The number of relationships in the dataset is: {num_relationships}")


if __name__ == "__main__":
    main()
