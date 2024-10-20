import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="SQL Table Schemas", layout="wide")

# Sample SQL table schemas
tables = {
    "Users": {
        "columns": ["UserID (INT)", "Username (VARCHAR)", "Email (VARCHAR)", "CreatedAt (DATETIME)"],
        "data": [
            {"UserID": 1, "Username": "john_doe", "Email": "john@example.com", "CreatedAt": "2024-01-01 10:00:00"},
            {"UserID": 2, "Username": "jane_smith", "Email": "jane@example.com", "CreatedAt": "2024-02-01 10:00:00"},
        ],
    },
    "Products": {
        "columns": ["ProductID (INT)", "ProductName (VARCHAR)", "Price (DECIMAL)", "Stock (INT)"],
        "data": [
            {"ProductID": 101, "ProductName": "Laptop", "Price": 999.99, "Stock": 50},
            {"ProductID": 102, "ProductName": "Smartphone", "Price": 499.99, "Stock": 150},
        ],
    },
    "Orders": {
        "columns": ["OrderID (INT)", "UserID (INT)", "ProductID (INT)", "OrderDate (DATETIME)"],
        "data": [
            {"OrderID": 1, "UserID": 1, "ProductID": 101, "OrderDate": "2024-01-15 12:30:00"},
            {"OrderID": 2, "UserID": 2, "ProductID": 102, "OrderDate": "2024-02-15 14:30:00"},
        ],
    },
}

# Function to create a beautiful UI for the SQL tables
def display_tables():
    st.title("Dummy SQL Tables Schema")
    st.write("Explore the schemas of our sample SQL tables below:")

    # Loop through the table schemas
    for table_name, table_info in tables.items():
        # Sidebar for each table
        with st.expander(table_name, expanded=True):
            st.markdown("### Columns:")
            columns = ", ".join(table_info["columns"])
            st.write(columns)

            # Display the sample data
            st.markdown("### Sample Data:")
            df = pd.DataFrame(table_info["data"])
            st.dataframe(df)

            # Adding a link to learn more about SQL
            st.markdown(f"[Learn more about {table_name}](https://www.w3schools.com/sql/sql_ref_table.asp)", unsafe_allow_html=True)

# Main entry point of the application
if __name__ == "__main__":
    display_tables()