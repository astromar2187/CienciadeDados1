import chardet

class EncodingManager:
    """Componente para gerenciar problemas de encoding"""
    
    def detect_encoding(self, content):
        """Detecta a codificação de um conteúdo binário"""
        result = chardet.detect(content)
        return result['encoding']
        
    def process_content(self, content):
        """Processa o conteúdo binário tratando problemas de encoding"""
        encoding = self.detect_encoding(content)
        
        # Se não detectar encoding ou for desconhecido, usa utf-8 com fallback para latin-1
        if not encoding or encoding.lower() == 'unknown':
            try:
                return content.decode('utf-8')
            except UnicodeDecodeError:
                return content.decode('latin-1')
        
        # Caso contrário, usa o encoding detectado
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            # Fallback para utf-8 ou latin-1
            try:
                return content.decode('utf-8')
            except UnicodeDecodeError:
                return content.decode('latin-1')