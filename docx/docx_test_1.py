import docx

def get_text(filename):
    doc = docx.Document(filename)
    fulltext = []
    for paragraph in doc.paragraphs:
        #fulltext.append(paragraph.text)
        fulltext.append(' ' + paragraph.text)
    #return '\n'.join(fulltext)
    return '\n\n'.join(fulltext)

print(get_text('demo.docx'))
