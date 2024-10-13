import os
import zipfile

import pytest

from constants import FILES_DIR


@pytest.fixture(scope="session", autouse=True)
def create_archive():
    with zipfile.ZipFile(f"{FILES_DIR}/archive.zip", "w") as zf:
        for file in ["file_csv.csv", "file_pdf.pdf", "file_xlsx.xlsx"]:
            add_file = os.path.join(FILES_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    os.remove(f"{FILES_DIR}/archive.zip")

