import fitz
import xlsxwriter


class Util():

    def identificar_idioma_e_selecionar_palavra_chave(self, pdf_file):
        """
        função para identificar o idioma da pagina e selecionar a palavra chave de acordo
        """
        palavra_chave = ""
        with fitz.open(pdf_file) as doc:
            for page in doc:
                areas = page.search_for('Operador/Balanço de Local de Trabalho')
                if len(areas) > 0:
                    palavra_chave = 'Operador/Balanço de Local de Trabalho'
                else:
                    palavra_chave = 'Operator/Work Place Balance'
 
        return palavra_chave

    def indetificar_código_cabecalho(self, lista_de_dados):
        """
        função para identificar o código do cabecalho do PDF
        """
        codigo_cabecalho = lista_de_dados[1]

        return codigo_cabecalho

    def escrever_dados_planilha(self, lista_de_codigos, lista_de_descricoes, lista_de_smv):
        quantidade_de_linhas = len(lista_de_codigos)
        linha = 1
        coluna_codigo = 0
        coluna_descricao = 1
        coluna_de_smv = 2
        workbook = xlsxwriter.Workbook('dados_extraidos.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write("A1", "Códigos")
        worksheet.write("B1", "Descricao")
        worksheet.write("C1", "SMV")
        index = 0

        for _ in range(quantidade_de_linhas):
            worksheet.write(linha, coluna_codigo, lista_de_codigos[index])
            worksheet.write(linha, coluna_descricao, lista_de_descricoes[index])
            worksheet.write(linha, coluna_de_smv, lista_de_smv[index])

            index += 1
            linha += 1

        workbook.close() 

   

    

        return

    '''Abre uma janela para o usuário selecionar qual o arquivo, 
        a função pdfFiles filtra só por pdf e exlFiles filtra só por xlxs'''
'''
def pdfFiles(filenamePDF):
    filenamePDF = Util.filedialog.askopenfilename(initialdir="/",
        title="Select a File",
        filetypes=(('Adobe Acrobat Document', '*.pdf'),
                   ("all files", "*.*")))

    capturar_dados.lbl_PDF.configure(text=filenamePDF)


def exlFiles(filenameEXL):
    filenameEXL = Util.filedialog.askopenfilename(initialdir="/",
                  title="Select a File",
                  filetypes=(('Microsoft Excel Worksheet', '*.xlsx'),
                  ("all files","*.*")))


    capturar_dados.lbl_EXL.configure(text=filenameEXL)

'''
