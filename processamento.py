
from compilar_dados import GravarDados
from extracao_dados import ExtrairDados
from util import Util



class ProcessamentoDeDados:
    def processamento(self, pdf_path):
        
        #lista de dados extraidos
        lista_dados_extraidos = ExtrairDados().extrair_dados(pdf_path)

        #lista de códigos extraidos
        lista_de_codigos = ExtrairDados().extrair_lista_codigos(lista_dados_extraidos, pdf_path)

        #lista de descricoes do PDF
        lista_descricoes = ExtrairDados().extrair_descricao(lista_dados_extraidos, lista_de_codigos)

        #extracao de SMV
        lista_de_smv = ExtrairDados().extrair_smv(lista_dados_extraidos, lista_de_codigos)

        # Util().escrever_dados_planilha(lista_de_codigos, lista_descricoes, lista_de_smv)

        return






