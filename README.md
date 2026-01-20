# 📊 Automação de Análise de Feedbacks com IA

Este projeto foi desenvolvido como parte do meu aprendizado em **Ciência de Dados**, com o objetivo de transformar feedbacks brutos de clientes em insights estratégicos para negócios.

## 📝 Cenário do Projeto
O desafio consistia em classificar manualmente 115 avaliações de clientes. Para tornar o processo eficiente e escalável, desenvolvi um pipeline em Python que utiliza Inteligência Artificial para realizar a categorização automática e análise de sentimento.

## 🚀 Tecnologias Utilizadas
* **Python**: Linguagem principal para o script de automação.
* **Pandas**: Biblioteca utilizada para leitura de CSV e geração de relatórios em Excel.
* **Google Gemini API**: Modelo de linguagem (IA) utilizado para processamento de texto.
* **Excel**: Ferramenta utilizada para a criação do Dashboard final.

## ⚙️ Funcionalidades
* **Processamento em Lote**: Leitura de base de dados em formato `.csv`.
---
<img width="689" height="418" alt="image" src="https://github.com/user-attachments/assets/4391ac05-4fda-4738-9abd-10f6d6368a5c" />
---
  
* **Classificação Inteligente**: Identificação de Sentimento (Positivo, Negativo, Neutro) e Categoria (Logística, Tech, Atendimento, Produto).
* **API**: Implementação de lógica de pausa (`time.sleep`) para respeitar os limites de cota da API gratuita em 2026.
* **Exportação Estruturada**: Geração de arquivo `.xlsx` pronto para Tabelas Dinâmicas.
---
<img width="988" height="577" alt="image" src="https://github.com/user-attachments/assets/cea74b4a-e705-4f40-b1d9-9fbe3f0aa396" />
---

## 📈 Dashboard e Resultados
O Dashboard foi construído no Excel para monitorar a **Taxa de Satisfação** e a **Evolução Mensal** dos feedbacks.
* **Métrica Master**: Termômetro de Satisfação Geral.
* **Submétricas**: Volume de reclamações por categoria para identificação de gargalos operacionais.

<img width="1685" height="882" alt="image" src="https://github.com/user-attachments/assets/d4c2f79f-bc94-418d-b49d-14fb71ccd8c6" />



## 🛠️ Como Executar
1. Clone o repositório.
2. Configure sua chave de API no arquivo `.env`.
3. Instale as dependências: `pip install pandas google-generativeai python-dotenv`.
4. Execute o script: `python main.py`.

---
**Desenvolvido por Elizeu Lucio** *Estudante de Ciência de Dados focado em transformar dados em decisões.*
