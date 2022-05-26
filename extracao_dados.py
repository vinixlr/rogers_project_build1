import fitz
from util import Util



#PDF_FILE = 'pdf_sample\S211CSIW127.pdf'
# PDF_FILE = 'pdf_sample\Cruzeiro.pdf'
#PDF_FILE = 'pdf_sample\Join Back Rises - Fechar gancho costas 45 cm.pdf'

class ExtrairDados():

    def extrair_dados(self, pdf_path):
        """
        função para extrair todos os dados do arquivo PDF que possuem lista de códigos

        """
        PDF_FILE = pdf_path
        palavra_chave = Util().identificar_idioma_e_selecionar_palavra_chave(PDF_FILE)

        with fitz.open(PDF_FILE) as doc:
            texto_lista = []
            for page in doc:                        
                areas = page.search_for(palavra_chave)
                if len(areas) > 0:
                    page_display = page.get_displaylist()
                    dictionary_elements = page_display.get_textpage().extractDICT()
                    for block in dictionary_elements['blocks']:
                            for line in block['lines']:
                                line_text = ''
                                for span in line['spans']:
                                    line_text += ''+ span['text']
                                    texto_lista.append(line_text)
        return texto_lista
        
    
    def extrair_lista_codigos(self, lista_de_dados, pdf_path):
        """
        função para extrair lista de códigos dos dados extraidos do PDF

        """
        PDF_FILE = pdf_path
        palavra_chave = Util().identificar_idioma_e_selecionar_palavra_chave(PDF_FILE)
        lista_de_codigos = []
        index = lista_de_dados.index(palavra_chave)
        lista_filtrada = lista_de_dados[index:]
        codigo_cabecalho = Util().indetificar_código_cabecalho(lista_de_dados)
        lista_caractere_de_codigos = [11, 12]
        filtro_pdf = ["Description", "TECNOTEXTIL", codigo_cabecalho]
        for codigo in lista_filtrada:
            if len(codigo) in lista_caractere_de_codigos and ' ' not in codigo and codigo not in filtro_pdf:
                lista_de_codigos.append(codigo)

        return lista_de_codigos


    def extrair_descricao(self, lista_dados_extraidos, lista_de_codigos):
        """
        função para extrair as descrições  e os códigos das descrições da lista de dados extraidos

        """
        lista_descricao = []
        for item in lista_dados_extraidos:
            if item in lista_de_codigos:
                index = lista_dados_extraidos.index(item)
                extracao_descricao_e_codigo = lista_dados_extraidos[index::]
                descricao = extracao_descricao_e_codigo[1]
                codigo = extracao_descricao_e_codigo[2]

                lista_descricao.append(f"{descricao} + {codigo}")
        
        return lista_descricao


    def extrair_smv(self, lista_dados_extraidos, lista_de_codigos):
        """
        função para extrair o SMV  da lista de dados extraidos
        """
        filtro_verificacao = ["acabamento embutido."]

        lista_smv = []
        for item in lista_dados_extraidos:
            if item in lista_de_codigos:
                index = lista_dados_extraidos.index(item)
                extracao_smv = lista_dados_extraidos[index::]

                if len(extracao_smv[4]) > 2 and '.' in extracao_smv[4] and extracao_smv[4] not in filtro_verificacao: 
                    lista_smv.append(extracao_smv[4])
                elif len(extracao_smv[5]) > 2 and '.' in extracao_smv[5] and extracao_smv[5] not in filtro_verificacao:
                    lista_smv.append(extracao_smv[5])
                elif len(extracao_smv[6]) > 2 and '.' in extracao_smv[6] and extracao_smv[6] not in filtro_verificacao:
                    lista_smv.append(extracao_smv[6])
                elif len(extracao_smv[7]) > 2 and '.' in extracao_smv[7] and extracao_smv[7] not in filtro_verificacao:
                    lista_smv.append(extracao_smv[7])

        return lista_smv
