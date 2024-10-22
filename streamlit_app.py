import streamlit as st
import os
import hashlib
import pandas as pd

# Optional: Load password from environment variable for better security
# Make sure to set the environment variable STREAMLIT_PASSWORD before running the app
# Example (Unix): export STREAMLIT_PASSWORD='your_secure_password'
PASSWORD = os.getenv("STREAMLIT_PASSWORD", "password")  # Replace with your desired password

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hashed password for verification
HASHED_PASSWORD = hash_password(PASSWORD)

# Function to generate download links with icons
def create_sidebar_link(label, url, icon):
    st.sidebar.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="{icon}" alt="{label}" style="width:24px; margin-right:10px;">
            <a href="{url}" target="_blank" style="text-decoration: none; color: #1E90FF;">{label}</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Set page configuration
st.set_page_config(
    page_title="Open Source File Links",
    page_icon="📁",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Center the password container */
    .password-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 150px;
    }
    /* Style the password input box */
    .password-input {
        width: 300px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    /* Style the submit button */
    .password-button {
        margin-top: 10px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #1E90FF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .password-button:hover {
        background-color: #0d6efd;
    }
    /* Style for the DataFrame header */
    .custom-header th:first-child {
        background-color: #FF5733 !important;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def authenticate_user():
    """Authenticate the user with a password."""
    with st.container():
        st.markdown('<div class="password-container">', unsafe_allow_html=True)
        password = st.text_input("🔒 Enter Password to Access the App:", type="password", key="password_input", help="Enter your secure password.")
        submit = st.button("Submit", key="submit_button")
        st.markdown('</div>', unsafe_allow_html=True)
        return password, submit

def main_app():
    # Sidebar
    st.sidebar.title("📂 Available Files")

    # Define icons (you can use any icon URLs or base64 encoded images)
    icons = {
        "PDF": "https://img.icons8.com/color/48/000000/pdf-2.png",
        "Word": "https://img.icons8.com/color/48/000000/microsoft-word-2019--v1.png",
        "Excel": "https://img.icons8.com/color/48/000000/microsoft-excel-2019--v1.png",
        "PowerPoint": "https://img.icons8.com/color/48/000000/microsoft-powerpoint-2019--v1.png",
    }

    # List of real open-source documents
    documents = {
        "Sample PDF Document": {
            "url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
            "icon": icons["PDF"],
        },
        "Sample Word Document": {
            "url": "https://file-examples-com.github.io/uploads/2017/02/file-sample_100kB.doc",
            "icon": icons["Word"],
        },
        "Sample Excel Spreadsheet": {
            "url": "https://file-examples-com.github.io/uploads/2017/02/file_example_XLS_10.xls",
            "icon": icons["Excel"],
        },
        "Sample PowerPoint Presentation": {
            "url": "https://file-examples-com.github.io/uploads/2017/08/file_example_PPT_500kB.ppt",
            "icon": icons["PowerPoint"],
        },
    }

    # Create links in the sidebar
    for label, info in documents.items():
        create_sidebar_link(label, info["url"], info["icon"])

    # Main Content
    st.title("Welcome to the Open Source File Download App 📂")
    st.write("Use the sidebar to access and download various open-source documents.")

    # Display information about the files
    for label, info in documents.items():
        st.subheader(label)
        st.markdown(
            f"""
            <a href="{info['url']}" target="_blank" style="text-decoration: none;">
                <div style="display: flex; align-items: center;">
                    <img src="{info['icon']}" alt="{label}" style="width:50px; margin-right: 10px;">
                    <span style="font-size:18px; color:#1E90FF;">Download {label.split()[1]}</span>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")

    # Add a small, styled DataFrame
    st.subheader("Sample DataFrame with Styled Header")

    # Create a sample DataFrame
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)

    # Apply styling to the first column header using Styler
    styled_df = df.style.set_table_styles({
        'Name': [{
            'selector': 'th',
            'props': [('background-color', '#FF5733'), ('color', 'white')]
        }]
    })

    # Display the styled DataFrame using Streamlit's native support
    st.write(styled_df)

    # Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top:50px;">
            <p>© 2024 Your Company Name. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    # Initialize session state for authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        password, submit = authenticate_user()
        if submit:
            if hash_password(password) == HASHED_PASSWORD:
                st.session_state.authenticated = True
                st.success("✅ Access Granted!")
                st.experimental_rerun()
            elif password:
                st.error("❌ Access Denied. Incorrect Password.")
    else:
        main_app()

if __name__ == "__main__":
    main()
