# Dashboard de Vendas de Supermercado

Um dashboard interativo em Python com **Streamlit** para análise de vendas de supermercado.

## Funcionalidades

- Visualização do faturamento diário
- Faturamento por produto, filial e forma de pagamento
- Avaliação média das filiais
- Filtros dinâmicos por mês

## Como rodar

1. Crie um ambiente virtual:
python -m venv .venv
.venv\Scripts\activate


2. Instale as dependências:
pip install streamlit pandas plotly


3. Rode o dashboard:
streamlit run dashboard.py


O arquivo `supermarket_sales.csv` já está incluído para testes.

---

## Estrutura

- `dashboard.py` — código principal do dashboard
- `supermarket_sales.csv` — base de dados usada
- `testes.ipynb` — anotações e testes exploratórios


