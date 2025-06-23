import pandas as pd

class Orchestrator:
    """Componente orquestrador que coordena o fluxo de trabalho"""
    
    def __init__(self, artist_extractor, discography_extractor, 
                 lyrics_extractor, text_processor, data_storage):
        self.artist_extractor = artist_extractor
        self.discography_extractor = discography_extractor
        self.lyrics_extractor = lyrics_extractor
        self.text_processor = text_processor
        self.data_storage = data_storage
        
    def process_all_artists(self):
        """Processa todos os artistas disponíveis"""
        artists = self.artist_extractor.get_artists()
        
        for artist in artists:
            print(f"Processando artista: {artist}")
            self.process_artist(artist)
            
    def process_artist(self, artist):
        """Processa um artista específico"""
        # Extrai discografia
        discography, artist_name, artist_tags = self.discography_extractor.extract_discography(artist)
        
        if not discography:
            print(f"Nenhum álbum encontrado para {artist}")
            return
            
        # Salva discografia em JSON
        self.data_storage.save_to_json(discography, f"{artist}_discografia")
        
        # Prepara dados para CSV e processamento de letras
        all_songs = []
        
        for album in discography:
            for track in album["tracks"]:
                # Extrai letra se tiver URL
                lyrics = None
                if "url" in track and track["url"]:
                    lyrics = self.lyrics_extractor.extract_lyrics(track["url"])
                    
                    # Processa a letra se encontrada
                    if lyrics:
                        lyrics = self.text_processor.normalize(lyrics)
                        lyrics = self.text_processor.tokenize(lyrics)
                
                # Cria registro da música
                song_data = {
                    "artist": artist_name,
                    "tags": artist_tags,
                    "album": album["album_title"],
                    "year": album["year"],
                    "record_label": album["album_record"],
                    "title": track["name"],
                    "lyrics": lyrics if lyrics else ""
                }
                
                all_songs.append(song_data)
        
        # Salva todas as músicas em CSV
        if all_songs:
            df = pd.DataFrame(all_songs)
            self.data_storage.save_to_csv(df, f"{artist}_musicas")
            
        print(f"Processamento de {artist} concluído. {len(all_songs)} músicas encontradas.")