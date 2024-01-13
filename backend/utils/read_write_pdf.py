import os
import PyPDF2
from PyPDF2.generic import AnnotationBuilder


def extract_page(source_writer: PyPDF2.PdfWriter, page: dict):
    """
    Extracts a specific page from a PDF file and adds it to the source writer object.

    Args:
        source_writer (PyPDF2.PdfWriter): The PDF writer object for the source PDF file.
        source_path (str): The path to the source PDF file.
        page (dict): A dictionary containing the page number to extract.
            page = { "pdf": "pdf_filepath.pdf",
                    "page": page_number (int),
                    "keywords": ["keyword1", "keyword2"],
                    "average_score": 0.0 }

    Returns:
        None
    """
    source_path = str(page.get("pdf"))

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"{source_path} does not exist")

    with open(source_path, "rb") as source_file:
        source_reader = PyPDF2.PdfReader(source_file)
        page_number = page.get("page")
        if page_number is not None:
            source_page = source_reader.pages[int(page_number)]
            source_writer.add_page(source_page)



def save_selected_pages_to_temp_pdf(
    active_results: dict, folder_path_results="./src/assets"
):
    """
    Saves the selected pages from multiple PDF files to a temporary PDF file.

    Args:
        active_results (dict): A dictionary containing the selected pages from multiple PDF files.
        folder_path_results (str, optional): The folder path where the temporary PDF file will be saved. Defaults to "./src/assets".

    Returns:
        None
    """

    temp_pdf_name = f"temp.pdf"
    source_writer = PyPDF2.PdfWriter()
    destination_path = os.path.join(folder_path_results, temp_pdf_name)

    with open(destination_path, "wb") as destination_file:
        pass

    for pdf in active_results:
        for page in active_results[pdf]:
            # extract_page(source_writer, page)
            extract_page(source_writer, page)

    with open(destination_path, "wb") as destination_file:
        source_writer.write(destination_file)

    # remove output.pdf and rename temp.pdf to output.pdf
    os.remove(os.path.join(folder_path_results, "output.pdf"))
    os.rename(destination_path, os.path.join(folder_path_results, "output.pdf"))
