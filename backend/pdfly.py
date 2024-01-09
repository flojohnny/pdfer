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
        self.filepath_index: str = os.path.join(os.getcwd(), "index.json")
        self.index: dict = read_write_index.load_index(self.filepath_index)
        self.query: str = ""

        # handle any changes in the index
        self.update_index()

    def update_query(self, query: str):
        self.query = query
        matches = search_index.search(self.query, self.index)
        return matches

    def update_index(self):
        self.index = create_index.build_index(self.dirpath_pdfs)

    def update_pdf(self, active_results: dict):
        read_write_pdf.save_selected_pages_to_temp_pdf(active_results)
        return True
