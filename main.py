from extractors.vagalume.artist_extractor import ArtistExtractor
from extractors.vagalume.discography_extractor import DiscographyExtractor
from extractors.vagalume.lyrics_extractor import LyricsExtractor
from processors.text_processor import TextProcessor
from storage.data_storage import DataStorage
from utils.encoding_manager import EncodingManager
from orchestrator import Orchestrator

def main():
    # Inicializa componentes
    encoding_manager = EncodingManager()
    artist_extractor = ArtistExtractor('novo_artistas.txt')
    discography_extractor = DiscographyExtractor(encoding_manager)
    lyrics_extractor = LyricsExtractor(encoding_manager)
    text_processor = TextProcessor()
    data_storage = DataStorage()
    
    # Inicializa orquestrador
    orchestrator = Orchestrator(
        artist_extractor,
        discography_extractor,
        lyrics_extractor,
        text_processor,
        data_storage
    )
    
    # Executa o processamento
    orchestrator.process_all_artists()
    
if __name__ == "__main__":
    main()