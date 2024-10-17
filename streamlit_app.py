import streamlit as st
from pathlib import Path
import base64

# Function to generate download links
def get_download_link(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        file_ext = file_path.suffix.lower()
        if file_ext == ".pdf":
            mime = "application/pdf"
        elif file_ext in [".docx", ".doc"]:
            mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        elif file_ext in [".xlsx", ".xls"]:
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        elif file_ext in [".pptx", ".ppt"]:
            mime = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        else:
            mime = "application/octet-stream"
        
        href = f'<a href="data:{mime};base64,{encoded}" download="{file_path.name}">{file_label}</a>'
        return href

# Set page configuration
st.set_page_config(
    page_title="File Download App",
    page_icon="📂",
    layout="wide",
)

# Sidebar
st.sidebar.title("📁 Available Files")
files_dir = Path(__file__).parent / "files"

# List of files with labels
files = {
    "Download PDF": files_dir / "sample.pdf",
    "Download Word Document": files_dir / "sample.docx",
    "Download Excel Spreadsheet": files_dir / "sample.xlsx",
    "Download PowerPoint Presentation": files_dir / "sample.pptx",
}

# Display download links in the sidebar
for label, path in files.items():
    if path.exists():
        st.sidebar.markdown(get_download_link(path, label), unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f"**{label}** - File not found.")

# Main Content
st.title("Welcome to the File Download App 📂")
st.write("Use the sidebar to download the files you need.")

# Optionally, display the files in the main area
for label, path in files.items():
    if path.exists():
        with open(path, "rb") as f:
            file_data = f.read()
            file_ext = path.suffix.lower()
            if file_ext == ".pdf":
                st.subheader(label)
                st.download_button(
                    label="Download PDF",
                    data=file_data,
                    file_name=path.name,
                    mime="application/pdf"
                )
            elif file_ext in [".docx", ".doc"]:
                st.subheader(label)
                st.download_button(
                    label="Download Word Document",
                    data=file_data,
                    file_name=path.name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            elif file_ext in [".xlsx", ".xls"]:
                st.subheader(label)
                st.download_button(
                    label="Download Excel Spreadsheet",
                    data=file_data,
                    file_name=path.name,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            elif file_ext in [".pptx", ".ppt"]:
                st.subheader(label)
                st.download_button(
                    label="Download PowerPoint Presentation",
                    data=file_data,
                    file_name=path.name,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
    else:
        st.warning(f"{label} - File not found.")

# Footer
st.markdown("---")
st.markdown("© 2024 Your Company Name. All rights reserved.")
