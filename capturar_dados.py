from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class CapturarDados:

    def pdfFiles():
        filenamePDF = filedialog.askopenfilename(initialdir="/",
                                                      title="Selecionar o Arquivo",
                                                      filetypes=(('Adobe Acrobat Document', '*.pdf'),
                                                                 ("all files", "*.*")))

        lbl_PDF.configure(text=filenamePDF)
        print(filenamePDF)
        return filenamePDF

    def exlFiles():
        filenameEXL = filedialog.askopenfilename(initialdir="/",
                                                 title="Selecionar o Arquivo",
                                                 filetypes=(('Microsoft Excel Worksheet', '*.xlsx'),
                                                            ("all files", "*.*")))
        lbl_EXL.configure(text=filenameEXL)




window = Tk()

window.title('File Explorer')

window.geometry("720x500")

window.config(background="white")

lbl_PDF = Label(window,
                text="Selecionar o arquivo PDF",
                width=100, height=4,
                fg="blue", background='white')

btn_PDF = Button(window,
                 text="Selecione o arquivo PDF",
                 command=CapturarDados.pdfFiles)

lbl_EXL = Label(window,
                text="Selecionar o arquivo em Excel",
                width=100, height=4,
                fg="blue", background='white')

btn_EXL = Button(window,
                 text="Selecione o arquivo em Excel",
                 command=CapturarDados.exlFiles)

btn_Confirmar = Button(window,
                       text="Confirmar",
                       command=window.destroy)

btn_Cancelar = Button(window,
                      text="Cancelar",
                      command=window.destroy)

lbl_PDF.grid(column=1, row=1)

btn_PDF.grid(column=1, row=2)

lbl_EXL.grid(column=1, row=3)

btn_EXL.grid(column=1, row=4)

btn_Confirmar.grid(column=1, row=5)

btn_Cancelar.grid(column=1, row=6)




window.mainloop()

