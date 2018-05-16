# instalar ví PIP
# pip install python-docx

# instalar vía anaconda
# conda install -c conda-forge python-docx
import docx

doc = docx.Document("demo.docx")
print(len(doc.paragraphs),"\n")

print(doc.paragraphs[0].text,"\n")

print(doc.paragraphs[1].text,"\n")

print(len(doc.paragraphs[1].runs),"\n")

print(doc.paragraphs[1].runs[0].text,"\n")

print(doc.paragraphs[1].runs[1].text,"\n")

print(doc.paragraphs[1].runs[2].text,"\n")

print(doc.paragraphs[1].runs[3].text,"\n")

print(doc.paragraphs[1].runs[4].text,"\n")

# documentación
# https://python-docx.readthedocs.io/en/latest/
