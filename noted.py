import streamlit as st
from fpdf import FPDF
import base64

def create_download_link(pdf, filename):
    """Generates a link to download the PDF."""
    b64 = base64.b64encode(pdf.output(dest="S").encode()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF</a>'
    return href

def main():
    st.title("Simple Note-Taking App with PDF Export")

    note = st.text_area("Enter your notes here:")

    if st.button("Export to PDF"):
        if note:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=note)

            pdf_bytes = pdf.output(dest="S").encode('latin-1')

            st.markdown(create_download_link(pdf, "my_notes.pdf"), unsafe_allow_html=True)
            st.success("PDF generated successfully! Click the link below to download.")
        else:
            st.warning("Please enter some notes before exporting.")

if __name__ == "__main__":
    main()
