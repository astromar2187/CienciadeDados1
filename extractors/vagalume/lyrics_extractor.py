import requests
import bs4
import time

class LyricsExtractor:
    """Componente para extrair letras de músicas"""
    
    def __init__(self, encoding_manager=None):
        self.encoding_manager = encoding_manager
        
    def extract_lyrics(self, song_url):
        """Extrai a letra de uma música a partir da URL"""
        if not song_url:
            return None
            
        try:
            # Faz a requisição
            req = requests.get(song_url)
            
            # Usa o gerenciador de encoding se disponível
            if self.encoding_manager:
                #content = self.encoding_manager.process_content(req.content)
                content = req.content
            else:
                content = req.content
                
            # Analisa o HTML
            soup = bs4.BeautifulSoup(content, "html.parser")
            
            # No Vagalume, a letra geralmente fica em uma div com id 'lyrics'
            lyrics_div = soup.find("div", id="lyrics")
            if lyrics_div:
                lyrics = lyrics_div.get_text(separator=' ').strip()
                
                # Adiciona delay para evitar sobrecarga do servidor
                time.sleep(1.5)
                
                return lyrics
            return None
            
        except Exception as e:
            print(f"Erro ao extrair letra de {song_url}: {e}")
            return None