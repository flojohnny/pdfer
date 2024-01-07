import os
import PyPDF2


def extract_pages(source_writer, source_path, destination_path, pages):
    with open(source_path, "rb") as source_file:
        source_reader = PyPDF2.PdfReader(source_file)

        with open(destination_path, "ab") as destination_file:
            for page_number in pages:
                source_page = source_reader.pages[int(page_number) - 1]
                source_writer.add_page(source_page)

            source_writer.write(destination_file)


def save_temp_results_to_pdf(matches, folder_path_results):
    output_pdf_name = f"temp.pdf"
    source_writer = PyPDF2.PdfWriter()
    for match in matches:
        source_pdf_path = match["pdf"]
        print(source_pdf_path)
        destination_pdf_path = os.path.join(folder_path_results, output_pdf_name)
        extract_pages(
            source_writer, source_pdf_path, destination_pdf_path, [match["page"]]
        )
    print(f"Top results saved to {output_pdf_name}")
