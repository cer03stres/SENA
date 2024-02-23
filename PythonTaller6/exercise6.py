import xlrd
import docx
from PIL import Image
import PyPDF2
import csv 


class Elementodocumento:
    def __init__(self, contenido):
        self.contenido = contenido
    
    def __str__(self):
        return self.contenido
    

class Texto (Elementodocumento):
    def __init__(self, contenido):
        super().__init__(contenido)


class Imagen(Elementodocumento):
    def __init__(self, contenido, formato):
        super().__init__(contenido)
        self.Formato = formato

class Documento:
    def __init__(self):
        self.elementos = []

    def agregar_elemento (self, elemento):
        self.elementos.append(elemento)

    def importar_xls(self,archivo):
        worbook = xlrd.open_workbook(archivo)
        for sheet  in worbook.sheets():
            for row in range(sheet.nrows):
                for col in range (sheet.ncols):
                    self.agregar_elemento(Texto(str(sheet.cell_value(row,col))))

        
    

    def importar_doc(self,archivo):
        doc = docx.Document(archivo)
        for paragraph in doc.paragraphs:
            self.agregar_elemento(Texto(paragraph.text))

    def importar_imagen(self, archivo):
        self.agregar_elemento(Imagen(archivo, 'JPG'))
            
    
    def importar_pdf(self, archivo):
        with open(archivo, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            for page_num in range (reader.numPages):
                page = reader.getPage(page_num)
                text = page.extractText()
                self.agregar_elemento(Texto(text))

    def importar_csv(self, archivo):
        with open (archivo, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                for col in row:
                    self.agregar_elemento(Texto(col))

#uso

documento = Documento()
documento.importar_xls('excel.xlsx')
documento.importar_doc('documento.docx')
documento.importar_imagen('imagen.jpg')
documento.importar_pdf('documento.pdf')
documento.importar_csv('documento.csv')

print("Contenido del documento: ")
for elemento in documento.elementos:
    print(elemento)