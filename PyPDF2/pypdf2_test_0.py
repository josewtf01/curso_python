# instalar PyPDF2

# vía PIP
# pip install PyPDF2

# Vía ANACONDA
# conda install -c conda-forge pypdf2
# ó
# conda install -c conda-forge/label/broken pypdf2

# esta librería es muy básica , permitiendo
# solo extraer texto de la mayoría de pdfs
# otro inconveniente es que puede fallar en algunos pdfs
import PyPDF2

pdf_file = open('meetingminutes.pdf',"rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

print(pdf_reader.numPages,"\n")

page_info = pdf_reader.getPage(0)

print(page_info.extractText())

pdf_file.close()

# documentación
# https://pythonhosted.org/PyPDF2/
