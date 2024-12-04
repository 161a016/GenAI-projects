import os
from pathlib import Path
import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
list_of_files=[
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiements/experiement.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "expection.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory; {filedir} for filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already created")
