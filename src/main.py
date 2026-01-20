import os
import time
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv



# ==========================================
#      CONFIGURAÇÕES INICIAIS DE API
# ==========================================



load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")



def configurar_ia():
    """Configura a conexão com a API do Google Gemini."""

    if not GOOGLE_API_KEY:
        raise ValueError("A chave de API não foi encontrada no arquivo .env")
    
    # Limpeza de possíveis resíduos na string da chave
    api_key = GOOGLE_API_KEY.strip().replace('"', '').replace("'", "")
    genai.configure(api_key=api_key)
    
    # Selecionamos o modelo Flash 
    return genai.GenerativeModel(model_name="gemini-2.5-flash")



def analisar_feedback(texto, model):
    """
    Envia o comentário para a IA e retorna Sentimento e Categoria.
    Inclui lógica de pausa para respeitar a cota gratuita.
    """
    prompt = (
        f"Analise o feedback: '{texto}'. "
        "Responda estritamente no formato: Sentimento;Categoria. "
        "Sentimentos: Positivo, Negativo, Neutro. "
        "Categorias: Logística, Produto, Tech, Atendimento."
    )
    
    try:
        response = model.generate_content(prompt)
        resultado = response.text.replace('\n', '').strip()
        
        # Pausa estratégica para evitar erro 429 (Cota Gratuita)
        # O modelo Flash na camada gratuita permite poucas requisições por minuto
        time.sleep(15) 
        return resultado
    
    except Exception as e:
        if "429" in str(e):
            print("⏳ Limite de cota atingido. Aguardando 30s...")
            time.sleep(30)
            return "Aguardando;Cota"
        return "Erro;Erro"



#==========================================
#              PIPELINE ETL 
# ==========================================



def executar_pipeline():
    print(" Iniciando Pipeline de Análise de Feedbacks...")
    
    try:
        # 1. SETUP
        ia_model = configurar_ia()
        
        # 2. EXTRACT (Extração)
        caminho_input = 'dados/feedbacks.csv'
        df = pd.read_csv(caminho_input)
        
        # Selecionamos uma amostra para o projeto (ajuste conforme necessário)
        df_processamento = df.copy()
        print(f"✅ {len(df_processamento)} registros carregados para análise.")

        # 3. TRANSFORM (Transformação com IA)
        print("Processando com IA... (Isso pode levar alguns minutos)")
        df_processamento['analise_bruta'] = df_processamento['comentario'].apply(
            lambda x: analisar_feedback(x, ia_model)
        )
        
        # Separando a resposta 'Sentimento;Categoria' em duas colunas
        df_processamento[['sentimento', 'categoria']] = df_processamento['analise_bruta'].str.split(';', n=1, expand=True)
        df_processamento.drop(columns=['analise_bruta'], inplace=True)

        # 4. LOAD (Carga)
        caminho_output = 'dados/Feedbacks_analisados.xlsx'
        df_processamento.to_excel(caminho_output, index=False)
        
        print(f"\nSucesso! O arquivo foi gerado: {caminho_output}")
        print(df_processamento[['comentario', 'sentimento', 'categoria']].head())

    except Exception as error:
        print(f"❌ Falha no pipeline: {error}")

if __name__ == "__main__":
    executar_pipeline()