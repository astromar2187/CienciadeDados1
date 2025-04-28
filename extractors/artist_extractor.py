class ArtistExtractor:
    """Componente para extrair informações de artistas de arquivos ou outras fontes"""
    
    def __init__(self, file_path='artistas.txt'):
        self.file_path = file_path
        
    def get_artists(self):
        """Lê artistas de um arquivo de texto"""
        try:
            return [linha.strip() for linha in open(self.file_path, encoding='utf-8')]
        except Exception as e:
            print(f"Erro ao carregar artistas: {e}")
            return []