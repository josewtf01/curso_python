import docx

doc  = docx.Document()

doc.add_paragraph('hello world')

doc.add_paragraph('Python Rules')

doc.save('hello_world.docx')
