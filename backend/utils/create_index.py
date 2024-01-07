import os
import PyPDF2
from PyPDF2 import PageObject

import re
from nltk.stem import PorterStemmer


def apply_stemming(index):
    stemmer = PorterStemmer()
    stemmed_index = {}
    for pdf, page_index in index.items():
        for page, words in page_index.items():
            for word, count in words.items():
                stemmed_word = stemmer.stem(word)
                if stemmed_word in stemmed_index:
                    stemmed_index[stemmed_word] += count
                else:
                    stemmed_index[stemmed_word] = count
            
            page_index[page] = stemmed_index
            stemmed_index = {}

        index[pdf] = page_index

    return index


def remove_stop_words(index):
    stop_words = {"a", "an", "the", "and", "or", "in", "on", "at"}
    for stop_word in stop_words:
        if stop_word in index:
            del index[stop_word]
    return index


def index_words(page: PageObject):
    index = {}
    words = re.findall(r"\w+", page.extract_text().lower())
    for word in words:
        word = word.lower()
        if word in index:
            index[word] += 1
        else:
            index[word] = 1

    return index


def index_pdf(pdf_path):
    print(f"Indexing {pdf_path}")
    index = {}

    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for page_number in range(len(reader.pages)):
            index[page_number] = index_words(reader.pages[page_number])

    return index


def build_index(folder_path_pdfs):
    index = {}
    for filename in os.listdir(folder_path_pdfs):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path_pdfs, filename)
            index[pdf_path] = index_pdf(pdf_path)

    index = remove_stop_words(index)
    index = apply_stemming(index)

    return index
