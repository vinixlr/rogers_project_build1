from gettext import install

from extracao_dados import ExtrairDados
import pandas as pd 
from openpyxl import Workbook, load_workbook

from tkinter import messagebox

class GravarDados:

    def test(self):
    #Atribuindo uma váriavel a Database 

    # dbExcel = pd.read_excel('C:\\Users\marchrom\Documents\PDF_Extract-main\excel_sample\GSD_Alignment_TT.xlsx')
    # dbExcel.head()

    # #Atribuindo uma váriavel a coluna de Códigos
    # dbCod = dbExcel.iloc[:,0]
    # #Atribuindo uma váriavel a coluna de Descrições
    # dbDesc = dbExcel.iloc[:,1]
    # #Atribuindo uma váriavel a coluna de SMVs
    # dbSmv = dbExcel.iloc[:,2]




    #lista de dados extraidos
    # lista_dados_extraidos = ExtrairDados().extrair_dados()

    #lista de códigos extraidos
    # lista_de_codigos = ExtrairDados().extrar_lista_codigos(lista_dados_extraidos)

    #lista de descricoes do PDF
    # lista_descricoes = ExtrairDados().extrair_descricao(lista_dados_extraidos, lista_de_codigos)

    #extracao de SMV
    # lista_de_smv = ExtrairDados().extrair_smv(lista_dados_extraidos, lista_de_codigos)


    #Usando openpyplx para gravar os dados na planilha selecionada

    #Definindo uma variavel como excel
    # plan = load_workbook('C:\\Users\marchrom\Documents\PDF_Extract-main\excel_sample\GSD_Alignment_TT.xlsx')

    #Definindo que a aba ativa do Excel DB será o local de gravação dos dados
    # aba_ativa = plan.active

    #Definindo váriaveis Source das listas geradas do PDF
    #Atribuindo uma váriavel a coluna de Códigos
    # srcCod = lista_de_codigos
    #Atribuindo uma váriavel a coluna de Descrições
    # srcDesc = lista_descricoes
    #Atribuindo uma váriavel a coluna de SMVs
    # srcSmv = lista_de_smv


    #Criando ponteiros para rodar os loopings
    # celulaA = 0
    # celulaB = 0
    # celulaC = 0
    # a = 0
    # b = 0
    # c = 0



    #Atribuindo uma váriavel a quantidade de linhas da Código (Usando como ponteiro nos for)
    # pCod = len(dbExcel.iloc[:,0]) 

    #Escreve na próxima célula em branco da coluna A(apontada por pCod) até o tamanho de srcCod

    # for celulaA in srcCod:
    #     aba_ativa[f"A{pCod}"] = srcCod[a]
    #     pCod = pCod + 1
    #     a = a + 1

    
    #Atribuindo uma váriavel a quantidade de linhas da Descrição (Usando como ponteiro nos for)
    # pDesc = len(dbExcel.iloc[:,0]) 

    #Escreve na próxima célula em branco da coluna A(apontada por pDesc) até o tamanho de srcCod

    # for celulaB in srcDesc:
    #     aba_ativa[f"B{pDesc}"] = srcDesc[b]
    #     pDesc = pDesc + 1
    #     b = b + 1

    #Atribuindo uma váriavel a quantidade de linhas da SMV (Usando como ponteiro nos for)
    # pSmv = len(dbExcel.iloc[:,1])


    #Escreve na próxima célula em branco da coluna A(apontada por pDesc) até o tamanho de srcCod

    # for celulaC in srcSmv:
    #     aba_ativa[f"C{pSmv}"] = srcSmv[c]
    #     pSmv = pSmv + 1
    #     c = c + 1


    #Grava e substitui o arquivo selecionado como DB.
    # plan.save('teste3.xlsx')

    # print(srcCod)
    # print(srcDesc)
    # print(srcSmv)
    # print(pCod)

        pass
#messagebox.showinfo(tittle=None, message= 'Conversão realizada!')