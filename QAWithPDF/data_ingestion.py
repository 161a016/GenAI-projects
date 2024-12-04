from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):
    """
    Load PDF documents from specfic directory.
    parameters:
    data(str):The path to directory containing PDF Files.
    return :
    -Alist of loaded pdf documents.The specific type of  document may vary.
    """
    try:
        logging.info("data loaded started...")
        loader=SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("datal loading started")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)
