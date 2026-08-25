import pandas as pd
 
### extração
 
def carregar_dados(caminho):
 
    df = pd.read_csv(caminho)
 
    return df
 
### transformação
 
def transformar_dados(df):
 
    df = df.copy()
 
    df = df.dropna(
        subset=["id_cliente"]
    )
 
    df = df[
        df["quantidade"] > 0
    ]
 
    df = df[
        df["valor_unitario"] > 0
    ]
 
    #calcular o faturamento
    df["faturamento"] = (
        df["quantidade"] + df["valor_unitario"]
    )
 
    return df
 
### agregação
def gerar_resumo(df):
    resumo = (
        df
        .groupby("produto")["faturamento"]
        .sum()
        .reset_index()
    )
 
    return resumo
 
### execução do pipeline
 
if __name__ == "__main__":
    df = carregar_dados(
        "data/vendas.csv"
    )
   
    df = transformar_dados(df)
   
    resumo = gerar_resumo(df)
 
    print(resumo)
 
    resumo.to_csv(
        "data/resultado.csv",
        index=False
    )