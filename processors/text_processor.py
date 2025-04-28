import re
import unicodedata

class TextProcessor:
    """Componente para processar e normalizar textos"""
    
    def normalize(self, text):
        """Normaliza o texto removendo caracteres especiais, ajustando espaços, etc."""
        if not text:
            return ""
            
        # Remove espaços extras
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Normaliza caracteres Unicode
        text = unicodedata.normalize('NFKC', text)
        
        return text
        
    def tokenize(self, text):
        """Tokeniza o texto em palavras"""
        if not text:
            return []
            
        # Normaliza primeiro
        text = self.normalize(text)
        
        # Divide em tokens (palavras)
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        return tokens