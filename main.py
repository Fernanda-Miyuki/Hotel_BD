import streamlit as st
import sys
from pathlib import Path
import importlib

# Configuração da interface
st.set_page_config(
    page_title="Hotel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Adiciona a raiz do projeto ao sys.path
sys.path.append(str(Path(__file__).parent))

# Dicionário de páginas disponíveis (nome amigável → módulo)
PAGES = {
    "Funcionário": "Views.PageFuncionario",
    "Serviço": "Views.PageServico",
}

# Sidebar com menu de navegação
st.sidebar.title("Menu de Navegação")
selected_page = st.sidebar.radio("Escolha a página:", list(PAGES.keys()))

# Função para carregar dinamicamente a função da página
def load_page(page_label):
    """Carrega o módulo da página e executa sua função principal"""
    try:
        module_path = PAGES[page_label]
        module = importlib.import_module(module_path)

        # Deriva o nome da função principal da página
        function_name = f"show_{page_label.lower().replace('á','a').replace('ç','c').replace('é','e')}_page"
        page_function = getattr(module, function_name)

        # Executa a função da página
        page_function()

    except (ImportError, AttributeError) as e:
        st.error(f"Erro ao carregar a página '{page_label}': {e}")
        st.stop()

# Carrega a página selecionada
load_page(selected_page)
