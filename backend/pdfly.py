import os
from backend.utils import read_write_index
from backend.utils import create_index
from backend.utils import search_index
from backend.utils import read_write_pdf


class Pdfly:
    def __init__(self):
        # define the paths to the pdfs and results directories
        self.dirpath_pdfs: str = os.path.join(os.getcwd(), "pdfs")
        self.dirpath_results: str = os.path.join(os.getcwd(), "./src/assets")
        self.filepath_index: str = os.path.join(os.getcwd(), "./src/assets/index.json")
        self.index: dict = read_write_index.load_index(self.filepath_index)
        self.query: str = ""

        # handle any changes in the index
        self.update_index()

    def update_query(self, query: str):
        self.query = query
        matches = search_index.search(self.query, self.index)
        return matches

    def update_index(self):
        # search the pdfs directory for any new pdfs, referring to full filepaths
        for filename in os.listdir(self.dirpath_pdfs):
            pdf_path = os.path.join(self.dirpath_pdfs, filename)
            if filename.endswith(".pdf") and pdf_path not in self.index:
                self.index = create_index.add_pdf_to_index(pdf_path, self.index)
        # search the index for any pdfs that have been deleted
        for pdf_path in list(self.index.keys()):
            if not os.path.exists(pdf_path):
                del self.index[pdf_path]

        # apply stemming and remove stop words to the index
        self.index = create_index.remove_stop_words(self.index)
        self.index = create_index.apply_stemming(self.index)

        # save the updated index to the index.json file
        read_write_index.save_index(self.index, self.filepath_index)

    def update_pdf(self, active_results: dict):
        read_write_pdf.save_selected_pages_to_temp_pdf(active_results)
        return True
