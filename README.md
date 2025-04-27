# Projeto de Ciência de Dados: Base de Letras de Rap Brasileiro

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema automatizado para raspagem, processamento e armazenamento de letras de músicas de rap, com o objetivo de criar um conjunto de dados estruturado para análises linguísticas e culturais. O sistema parte apenas do nome do artista e navega automaticamente através da hierarquia de discografia, extraindo e processando letras completas de cada música por álbum.

O projeto foi concebido para a primeira avaliação da disciplina de Ciência de Dados ofertada pelo Departamento de Computação da UFPI no período 2025.1. O objetivo é aplicar técnicas de raspagem web para desenvolver um dataset específico sobre artistas brasileiros e suas letras de rap, permitindo análises posteriores sobre vocabulário, temas, evolução temporal e características regionais das produções.

## Características Principais

O sistema é projetado com uma arquitetura modular que permite:

1. **Entrada Simplificada**: A partir apenas do nome do artista, o sistema localiza automaticamente sua discografia online.
2. **Navegação Hierárquica**: O sistema navega pela estrutura artista → discografia → álbum → música, extraindo metadados importantes como ano de lançamento e título do álbum.
3. **Adaptabilidade HTML**: Utilizando um sistema de templates configuráveis, o software se adapta às diferentes estruturas HTML de diversos sites de letras musicais.
4. **Tratamento de Encoding**: Implementação de mecanismos robustos para lidar com diferentes codificações de caracteres encontradas nos sites, garantindo a correta extração do texto.
5. **Processamento Linguístico**: As letras extraídas são tokenizadas e processadas seguindo um formato padronizado, preservando suas características linguísticas para análise futura.
6. **Armazenamento Estruturado**: Os dados são armazenados em formato consistente, mantendo a relação entre artista, álbum, música e metadados geográficos.

## Arquitetura do Sistema

O sistema foi estruturado em componentes independentes que podem ser desenvolvidos por diferentes membros da equipe:

1. **Orquestrador**: Coordena o fluxo de trabalho e a integração entre os módulos.
2. **Extratores**: Componentes especializados para busca de artistas, extração de discografia e coleta de letras.
3. **Processador de Texto**: Responsável pela normalização, tokenização e preparação dos dados textuais.
4. **Sistema de Armazenamento**: Gerencia a persistência dos dados em formato estruturado.
5. **Gerenciador de Encoding**: Componente dedicado à detecção e tratamento de diferentes codificações.