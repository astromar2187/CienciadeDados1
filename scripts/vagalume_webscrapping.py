import requests
import bs4
import re
import pandas as pd
import unidecode

# puxa os nomes dos artistas do arquivo
artistas = [linha.strip() for linha in open('novo_artistas.txt', encoding='utf-8')]

# Lista para armazenar todas as linhas do DataFrame
data = []

# Função para gerar slug da música (o Vagalume usa nomes em minúsculo e sem acento)
def slugify(nome):
    nome = unidecode.unidecode(nome.lower())  # tira acento e põe minúsculo
    nome = re.sub(r'[^\w\s-]', '', nome)  # remove tudo que não é letra, número, espaço ou hífen
    nome = nome.replace(' ', '-')  # troca espaços por hífen
    nome = re.sub(r'-+', '-', nome)  # evita múltiplos hífens
    return nome.strip('-')  # tira hífens sobrando nas pontas

for artista in artistas:
    # Monta a url
    url = 'https://www.vagalume.com.br/' + artista + "/discografia/"

    # Faz a requisição
    req = requests.get(url)

    # puxa o html -> usa req.content e não req.text por erros de encoding detectados em testes
    soup = bs4.BeautifulSoup(req.content, "html.parser")

    #nome do artista
    artist_name = soup.find("h1", "darkBG long")
    if artist_name == None:
        artist_name = soup.find("h1", "darkBG")
    artist_name = artist_name.get_text().strip()

    # tags associadas ao artista
    artist_tags_list = soup.find("ul", "subHeaderTags h14")
    artist_tags = []

    if artist_tags_list:
        tag_items = artist_tags_list.find_all("a")
        for tag in tag_items:
            tag_text = tag.get_text().strip()
            artist_tags.append(tag_text)

    # Lista que vai guardar os álbuns
    discografia = []

    # recupera os álbuns
    albuns = soup.find_all("div", "topLetrasWrapper")

    for album_div in albuns:
        album = {}

        album["artist_name"] = artist_name
        album["artist_tags"] = artist_tags

        album_title_elem = album_div.find("h1", "albumTitle")
        if album_title_elem:
            album["album_title"] = album_title_elem.get_text().strip()
        else:
            album["album_title"] = None

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

        track_list = album_div.find("ol", id="topMusicList")
        tracks = []
        if track_list:
            track_items = track_list.find_all("li")
            for track in track_items:
                track_name_elem = track.find("a", "nameMusic")
                if track_name_elem:
                    track_name = track_name_elem.get_text().strip()
                    tracks.append(track_name)
        album["tracks"] = tracks

        # Adiciona esse álbum na lista de discografia
        discografia.append(album)

        '''for album in discografia:
            print(album)'''
        

    for album in discografia:
        artist = album['artist_name']
        for track in album['tracks']:
            track_slug = slugify(track)
            url = f"https://www.vagalume.com.br/{slugify(artist)}/{track_slug}.html"
            
            req = requests.get(url)
            soup = bs4.BeautifulSoup(req.content, 'html.parser')
            lyric_div = soup.find('div', id='lyrics')
            if lyric_div:
                lyrics = lyric_div.get_text(separator=' ').strip()
            else:
                lyrics = None
            
            data.append({
                'artist_name': artist,
                'artist_tags': album['artist_tags'],
                'album_title': album['album_title'],
                'year': album['year'],
                'track_name': track,
                'lyrics': lyrics
            })

# Criar DataFrame
df = pd.DataFrame(data)

# salvar o csv
df.to_csv('discografia_letras.csv', index=False)
