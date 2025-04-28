import json
import csv
import os
import pandas as pd

class DataStorage:
    """Componente para armazenar dados em diferentes formatos"""
    
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        # Cria diretório de saída se não existir
        os.makedirs(output_dir, exist_ok=True)
        
    def save_to_json(self, data, filename):
        """Salva dados em formato JSON"""
        filepath = os.path.join(self.output_dir, f"{filename}.json")
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Dados salvos em {filepath}")
            return True
        except Exception as e:
            print(f"Erro ao salvar JSON: {e}")
            return False
            
    def save_to_csv(self, data, filename):
        """Salva dados em formato CSV"""
        filepath = os.path.join(self.output_dir, f"{filename}.csv")
        try:
            # Converte para DataFrame se for uma lista de dicionários
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                df = pd.DataFrame(data)
                df.to_csv(filepath, index=False, encoding='utf-8')
            elif isinstance(data, pd.DataFrame):
                data.to_csv(filepath, index=False, encoding='utf-8')
            else:
                raise ValueError("Formato de dados não suportado para CSV")
                
            print(f"Dados salvos em {filepath}")
            return True
        except Exception as e:
            print(f"Erro ao salvar CSV: {e}")
            return False