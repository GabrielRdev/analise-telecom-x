import requests
import pandas as pd
from pathlib import Path
import json

def extract_telecom_data(url: str) -> pd.DataFrame:
    """
    Extrai os dados da API e retorna um DataFrame.
    """
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    
    # Mostrar informações sobre o DataFrame
    print("\nInformações do DataFrame após extração:")
    print("\nColunas disponíveis:")
    print(df.columns.tolist())
    print("\nPrimeiras linhas:")
    print(df.head())
    print("\nEstrutura do DataFrame:")
    print(df.info())
    
    # Normaliza colunas aninhadas (ex: 'account')
    if 'account' in df.columns:
        print("\nNormalizando coluna 'account'...")
        account_df = pd.json_normalize(df['account'])
        df = pd.concat([df.drop('account', axis=1), account_df], axis=1)
        print("\nColunas após normalização:")
        print(df.columns.tolist())
    
    return df

def save_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Salva o DataFrame como arquivo JSON.
    """
    # Criar diretório se não existir
    output_dir = Path(file_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Converter DataFrame para JSON e salvar
    df.to_json(file_path, orient='records', indent=2)
    print(f"\nDados salvos em: {file_path}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/main/TelecomX_Data.json"
    df = extract_telecom_data(url)
    
    # Salvar dados
    data_path = "data/telecom_data.json"
    save_data(df, data_path)
    
    print("\nEstatísticas descritivas:")
    print(df.describe())