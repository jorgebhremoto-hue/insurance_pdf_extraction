# 📄 Insurance PDF Extraction Tool
**Repo:** `jorgebhremoto-hue/insurance_pdf_extraction`

This specialized tool extracts key information from insurance payment receipts (specifically optimized for **Quálitas Seguros**). It transforms static PDF data into structured, readable information using a clean Streamlit interface.

## 🚀 Key Features
- **Automated Extraction:** Parses PDF files to retrieve Policy Number, Amount Due, Vehicle Details, and Due Dates.
- **Validation Engine:** Uses a dual-check system (`extract_insurance_info_2`) to verify the document type before processing.
- **User-Friendly UI:** Built with Streamlit for a fast, responsive web experience.
- **Data Export:** Generates a clean code block with extracted data for easy "copy-paste" into other systems.

## 📁 Repository Structure
To ensure successful deployment on **Streamlit Cloud**, the files are organized as follows:
- `app.py`: The main entry point for the Streamlit interface.
- `extraction_logic.py`: (Or your specific .py files) Backend functions for PDF parsing.
- `requirements.txt`: Python dependencies (e.g., streamlit, pdfplumber).
- `README.md`: Project documentation.

## 🛠️ Installation & Deployment

### Local Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/jorgebhremoto-hue/insurance_pdf_extraction.git](https://github.com/jorgebhremoto-hue/insurance_pdf_extraction.git)
   cd insurance_pdf_extraction
