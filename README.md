## Descrição do Projeto

Este projeto consiste em um sistema automatizado para raspagem, processamento e armazenamento de letras de músicas de rap, criando um conjunto de dados estruturado para análises linguísticas e culturais. O sistema extrai dados do site Vagalume, navegando pela hierarquia de discografia a partir do nome do artista.

O projeto foi concebido para a primeira avaliação da disciplina de Ciência de Dados ofertada pelo Departamento de Computação da UFPI no período 2025.1. O objetivo é aplicar técnicas de raspagem web para desenvolver um dataset específico sobre artistas brasileiros e suas letras de rap, permitindo análises posteriores sobre vocabulário, temas, evolução temporal e características regionais das produções.

## Estrutura do Projeto

```
├── main.py                    # Ponto de entrada da aplicação
├── config/
│   ├── __init__.py
│   └── settings.py            # Configurações gerais
├── extractors/
│   ├── __init__.py
│   ├── artist_extractor.py    # Extrator de artistas
│   ├── discography_extractor.py # Extrator de discografia
│   └── lyrics_extractor.py    # Extrator de letras
├── processors/
│   ├── __init__.py
│   └── text_processor.py      # Processador de texto
├── storage/
│   ├── __init__.py
│   └── data_storage.py        # Sistema de armazenamento
├── utils/
│   ├── __init__.py
│   └── encoding_manager.py    # Gerenciador de encoding
└── orchestrator.py            # Orquestrador principal
```

## Componentes

### Orquestrador

O Orchestrator coordena o fluxo de trabalho entre os diferentes componentes.

Principais métodos:
- `process_all_artists`: Processa todos os artistas da lista
- `process_artist`: Processa um artista específico, extraindo sua discografia e letras

### Extratores

Componentes responsáveis por extrair dados de diferentes fontes:

- **ArtistExtractor**: Extrai nomes de artistas de um arquivo texto
  - `get_artists`: Lê a lista de artistas do arquivo

- **DiscographyExtractor**: Extrai informações da discografia de um artista
  - `extract_discography`: Extrai a discografia completa
  - `_extract_album_info`: Extrai informações de um álbum específico
  - `_extract_tracks`: Extrai a lista de músicas de um álbum

- **LyricsExtractor**: Extrai letras de músicas
  - `extract_lyrics`: Extrai a letra de uma música específica

### Processadores

- **TextProcessor**: Normaliza e processa textos extraídos
  - `normalize`: Normaliza o texto da letra de música

### Armazenamento

- **DataStorage**: Gerencia o armazenamento dos dados extraídos
  - `save_to_json`: Salva dados em formato JSON
  - `save_to_csv`: Salva dados em formato CSV

### Utilitários

- **EncodingManager**: Gerencia problemas de codificação de caracteres
  - `detect_encoding`: Detecta a codificação de um conteúdo binário
  - `process_content`: Processa o conteúdo binário tratando problemas de encoding

## Dados Extraídos

Os dados são armazenados em dois formatos principais:

1. **Discografias (JSON)**:
   - Estrutura hierárquica contendo álbuns e faixas
   - Exemplo: emicida_discografia.json

2. **Músicas (CSV)**:
   - Dados tabulares com informações sobre cada música e letra
   - Exemplo: emicida_musicas.csv

## Como Usar

1. Configure a lista de artistas em artistas.txt
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```
   python main.py
   ```

O sistema irá:
1. Ler a lista de artistas
2. Extrair a discografia de cada artista
3. Extrair as letras de cada música
4. Processar os textos
5. Salvar os dados em formato JSON e CSV no diretório output

## Dependências

O projeto utiliza as seguintes bibliotecas principais:
- beautifulsoup4: Para análise de HTML
- requests: Para requisições HTTP
- pandas: Para manipulação de dados tabulares
- chardet: Para detecção de codificação

## Exemplos

Um exemplo de dados extraídos é a discografia do artista Emicida, que inclui álbuns como:
- "AmarElo" (2019)
- "Sobre Crianças, Quadris, Pesadelos e Lições de Casa..." (2015)
- "O Glorioso Retorno de Quem Nunca Esteve Aqui" (2013)