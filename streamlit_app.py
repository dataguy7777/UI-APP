import streamlit as st

# Function to generate download links with icons
def create_sidebar_link(label, url, icon):
    st.sidebar.markdown(
        f"""
        <div style="display: flex; align-items: center;">
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
        <a href="{info['url']}" target="_blank">
            <img src="{info['icon']}" alt="{label}" style="width:50px; vertical-align: middle;">
            <span style="font-size:18px; color:#1E90FF;">Download {label.split()[1]}</span>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top:50px;">
        <p>© 2024 Your Company Name. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
