from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def translate(browser, language_r, language_d, text):
    browser.switch_to.window(browser.window_handles[1])
    browser.get(f'https://translate.google.com.br/?hl=pt-BR&sl={language_r}&tl={language_d}&text={text}&op=translate')
    while True:
        try:
            translated = browser.find_element(By.CSS_SELECTOR, "div.lRu31")
            break
        except NoSuchElementException:
            continue
    
    translated_text = translated.text if translated else ""
    browser.switch_to.window(browser.window_handles[0])
    
    return translated_text

idiomas = {'africaner': 'Africâner: af', 'albanes': 'Albanês: sq', 'amarico': 'Amárico: am', 'arabe': 'Árabe: ar', 'armenio': 'Armênio: hy', 'azerbaijano': 'Azerbaijano: az', 'basco': 'Basco: eu', 'bielorrusso': 'Bielorrusso: be', 'bengali': 'Bengali: bn', 'bosnio': 'Bósnio: bs', 'bulgaro': 'Búlgaro: bg', 'catalao': 'Catalão: ca', 'cebuano': 'Cebuano: ceb', 'chines (simplificado)': 'Chinês (simplificado): zh-CN', 'chines (tradicional)': 'Chinês (tradicional): zh-TW', 'corsico': 'Córsico: co', 'croata': 'Croata: hr', 'tcheco': 'Tcheco: cs', 'dinamarques': 'Dinamarquês: da', 'holandes': 'Holandês: nl', 'ingles': 'Inglês: en', 'esperanto': 'Esperanto: eo', 'estoniano': 'Estoniano: et', 'finlandes': 'Finlandês: fi', 'frances': 'Francês: fr', 'frisio': 'Frísio: fy', 'galego': 'Galego: gl', 'georgiano': 'Georgiano: ka', 'alemao': 'Alemão: de', 'grego': 'Grego: el', 'guzerate': 'Guzerate: gu', 'crioulo haitiano': 'Crioulo haitiano: ht', 'hausa': 'Hauçá: ha', 'havaiano': 'Havaiano: haw', 'hebraico': 'Hebraico: he ou iw', 'hindi': 'Hindi: hi', 'hmong': 'Hmong: hmn', 'hungaro': 'Húngaro: hu', 'islandes': 'Islandês: is', 'igbo': 'Igbo: ig', 'indonesio': 'Indonésio: id', 'irlandes': 'Irlandês: ga', 'italiano': 'Italiano: it', 'japones': 'Japonês: ja', 'javanes': 'Javanês: jv', 'canara': 'Canará: kn', 'cazaque': 'Cazaque: kk', 'cmer': 'Cmer: km', 'kinyarwanda': 'Kinyarwanda: rw', 'coreano': 'Coreano: ko', 'curdo': 'Curdo: ku', 'quirguiz': 'Quirguiz: ky', 'laosiano': 'Laosiano: lo', 'latim': 'Latim: la', 'leton': 'Letão: lv', 'lituano': 'Lituano: lt', 'luxemburgues': 'Luxemburguês: lb', 'macedonio': 'Macedônio: mk', 'malgaxe': 'Malgaxe: mg', 'malaio': 'Malaio: ms', 'malaiala': 'Malaiala: ml', 'maltes': 'Maltês: mt', 'maori': 'Maori: mi', 'marata': 'Marata: mr', 'mongol': 'Mongol: mn', 'myanmar (birmanes)': 'Myanmar (birmanês): my', 'nepales': 'Nepalês: ne', 'noruegues': 'Norueguês: no', 'nianja (chichewa)': 'Nianja (Chichewa): ny', 'oria': 'Oriá: or', 'pashto': 'Pashto: ps', 'persa': 'Persa: fa', 'polones': 'Polonês: pl', 'portugues (portugal, brasil)': 'Português (Portugal, Brasil): pt', 'punjabi': 'Punjabi: pa', 'romeno': 'Romeno: ro', 'russo': 'Russo: ru', 'samoano': 'Samoano: sm', 'gaelico escoces': 'Gaélico escocês: gd', 'servio': 'Sérvio: sr', 'sesoto': 'Sesoto: st', 'xona': 'Xona: sn', 'sindi': 'Sindi: sd', 'sinhala (cingales)': 'Sinhala (cingalês): si', 'eslovaco': 'Eslovaco: sk', 'esloveno': 'Esloveno: sl', 'somali': 'Somali: so', 'espanhol': 'Espanhol: es', 'sundanes': 'Sundanês: su', 'suaili': 'Suaíli: sw', 'sueco': 'Sueco: sv', 'tagalo (filipino)': 'Tagalo (filipino): tl', 'tajique': 'Tajique: tg', 'tamil': 'Tâmil: ta', 'tartaro': 'Tártaro: tt', 'telugu': 'Telugu: te', 'tailandes': 'Tailandês: th', 'turco': 'Turco: tr', 'turcomano': 'Turcomano: tk', 'ucraniano': 'Ucraniano: uk', 'urdu': 'Urdu: ur', 'uyghur': 'Uyghur: ug', 'usbeque': 'Usbeque: uz', 'vietnamita': 'Vietnamita: vi', 'gales': 'Galês: cy', 'xosa': 'Xosa: xh', 'idiche': 'Ídiche: yi', 'ioruba': 'Iorubá: yo', 'zulu': 'Zulu: zu'}

def find_language(palavra):
    resultado = {}
    for idioma, codigo in idiomas.items():
        if palavra in idioma:
            resultado[idioma] = codigo
    return resultado