import fitz

def extract_pdf_content(file_path):
    try:
        pdf_document = fitz.open(file_path)
        extracted_text = ""
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            extracted_text += page.get_text()
        pdf_document.close()

        return extracted_text
    except Exception as e:
        print(f"Error occurred while extracting PDF content: {e}")
        return None


# file_path = "src/utils/apoorv_garg.pdf"
# extracted_text = extract_pdf_content(file_path)
# if extracted_text:
#     print(extracted_text)
# else:
#     print("Failed to extract PDF content.")
