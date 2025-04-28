import requests
import bs4
import re
import time

class DiscographyExtractor:
    """Componente para extrair discografia de artistas de sites"""
    
    def __init__(self, encoding_manager=None):
        self.encoding_manager = encoding_manager
        self.base_url = 'https://www.vagalume.com.br/'
        
    def get_discography_url(self, artist):
        """Constrói a URL para a página de discografia do artista"""
        return f"{self.base_url}{artist}/discografia/"
        
    def extract_discography(self, artist):
        """Extrai a discografia completa de um artista"""
        url = self.get_discography_url(artist)
        
        try:
            # Faz a requisição
            req = requests.get(url)
            
            # Usa o gerenciador de encoding se disponível
            if self.encoding_manager:
                content = self.encoding_manager.process_content(req.content)
            else:
                content = req.content
                
            # Analisa o HTML
            soup = bs4.BeautifulSoup(content, "html.parser")
            
            # Lista para guardar os álbuns
            discografia = []
            
            # Recupera os álbuns
            albuns = soup.find_all("div", "topLetrasWrapper")
            
            for album_div in albuns:
                album = self._extract_album_info(album_div)
                discografia.append(album)
                
            # Adiciona delay para evitar sobrecarga do servidor
            time.sleep(1.5)
            
            return discografia
            
        except Exception as e:
            print(f"Erro ao extrair discografia de {artist}: {e}")
            return []
    
    def _extract_album_info(self, album_div):
        """Extrai informações de um álbum específico"""
        album = {}
        
        # Extrai título do álbum
        album_title_elem = album_div.find("h1", "albumTitle")
        if album_title_elem:
            album["album_title"] = album_title_elem.get_text().strip()
        else:
            album["album_title"] = None
            
        # Extrai ano e gravadora
        album_year_elem = album_div.find("p", "albumYear")
        album_record_elem = album_div.find("p", "albumRecord")
        
        if album_year_elem:
            year_text = album_year_elem.get_text().strip()
            # Separar o ano do resto usando regex
            match = re.match(r"(\d{4})(.*)", year_text)
            if match:
                album["year"] = match.group(1)
                # Se sobrou algo depois do ano, é a gravadora
                possible_label = match.group(2).strip()
                if possible_label and not album_record_elem:
                    album["album_record"] = possible_label
                else:
                    album["album_record"] = None
            else:
                album["year"] = year_text
                album["album_record"] = None
        else:
            album["year"] = None
            album["album_record"] = None
            
        # Se existir <p class="albumRecord"> de fato, usa ele como gravadora
        if album_record_elem:
            album["album_record"] = album_record_elem.get_text().strip()
            
        # Extrai lista de músicas
        album["tracks"] = self._extract_tracks(album_div)
        
        return album
        
    def _extract_tracks(self, album_div):
        """Extrai a lista de músicas de um álbum"""
        tracks = []
        track_list = album_div.find("ol", id="topMusicList")
        
        if track_list:
            track_items = track_list.find_all("li")
            for track in track_items:
                track_name_elem = track.find("a", "nameMusic")
                if track_name_elem:
                    track_name = track_name_elem.get_text().strip()
                    # Opcional: extrair URL da música para buscar letra depois
                    track_url = None
                    if track_name_elem.has_attr('href'):
                        track_url = self.base_url.rstrip('/') + track_name_elem['href']
                    
                    tracks.append({
                        "name": track_name,
                        "url": track_url
                    })
        
        return tracks