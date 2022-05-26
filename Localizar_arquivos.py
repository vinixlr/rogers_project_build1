from tkinter import filedialog
from tkinter import messagebox


class LocalizarArquivos:

    def buscar_pdf(self, label_pdf):
        """
        solicita ao usuario localizar o pdf através do explorer
        """
        caminho_do_arquvio = filedialog.askopenfilename(initialdir="/",
                                                      title="Selecionar o Arquivo",
                                                      filetypes=(('Adobe Acrobat Document', '*.pdf'),
                                                                 ("all files", "*.*")))

        label_pdf.configure(text=caminho_do_arquvio)
        
        return caminho_do_arquvio

    def buscar_excel(self, label_excel):
        """
        solicita ao usuario localizar o excel através do explorer
        """
        filenameEXL = filedialog.askopenfilename(initialdir="/",
                                                 title="Selecionar o Arquivo",
                                                 filetypes=(('Microsoft Excel Worksheet', '*.xlsx'),
                                                            ("all files", "*.*")))
        label_excel.configure(text=filenameEXL)
        return filenameEXL