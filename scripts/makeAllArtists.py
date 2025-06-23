import os
import pandas as pd

# Caminho para a pasta com os CSVs
csvs_dir = os.path.join(os.path.dirname(__file__), '..', 'output')

# Lista todos os arquivos .csv na pasta output
csv_files = [os.path.join(csvs_dir, f) for f in os.listdir(csvs_dir) if f.endswith('.csv')]

# Lê e concatena todos os CSVs
df_list = []
for f in csv_files:
	try:
		df = pd.read_csv(f)
		df_list.append(df)
	except Exception as e:
		print(f"Erro ao ler {f}: {e}")
df_all = pd.concat(df_list, ignore_index=True)

# Salva o resultado em um novo arquivo
output_path = os.path.join(os.path.dirname(__file__), '..', 'all_artists.csv')
df_all.to_csv(output_path, index=False)

print(f'Arquivo salvo em: {output_path}')