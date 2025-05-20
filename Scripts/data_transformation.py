
import re
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup

def remove_html_and_script(text):
    soup = BeautifulSoup(text, "html.parser")

    # Remove script and style tags completely
    for tag in soup(["script", "style"]):
        tag.decompose()


    return soup.get_text(strip=False)

def unicode_handling(text):
    # Dictionary of unicode escape sequences mapped to their actual characters
    unicode_map = {
        r'\u2018': '‘',  # Left single quote
        r'\u2019': '’',  # Right single quote
        r'\u201c': '“',  # Left double quote
        r'\u201d': '”',  # Right double quote
        r'\u2013': '–',  # En dash
        r'\u2014': '—',  # Em dash
        r'\u2022': '•',  # Bullet
        r'\u2026': '…',  # Ellipsis
        r'\u00a0': ' ',  # Non-breaking space
        r'\u00b7': '·',  # Middle dot
        r'\u00e9': 'é',  # e acute
        r'\u00e2': 'â',  # a circumflex
        r'\u00e0': 'à',  # a grave
        r'\u00e8': 'è',  # e grave
        r'\u00e7': 'ç',  # c cedilla
        r'\u00f4': 'ô',  # o circumflex
        r'\u00fb': 'û',  # u circumflex
        r'\u00ee': 'î',  # i circumflex
        r'\u00ef': 'ï',  # i diaeresis
        r'\u00e4': 'ä',  # a umlaut
        r'\u00f6': 'ö',  # o umlaut
        r'\u00fc': 'ü',  # u umlaut
        r'\u00df': 'ß',  # sharp s
        r'\u2082': '₂',  # subscript 2
        r'\u2083': '₃',  # subscript 3
        r'\u267b': '',         # Recycling symbol
        r'\ufe0f': '',         # Variation selector
        # r'\ud83d\udd25': '',   # Fire emoji
        # r'\ud83c\udf1f': '', 
        # r'\u2744\ufe0f': '',
        r'\u2744': '',
        r'\u2122': '™',
        r'\u27a1': '',
        r'\u20ac': '€',
        r'\u201': '',
        r'\u2013': '–',
        r'\u2014': '—',
        #r'\ud83d\udccd': '',
        #r'\ud83c\udf89': '',
        #r'\ud83d\udd17': '',
        #r'\ud83d\udd0e': '',
        #r'\ud83d\udcf8': '',
        #r'\ud83d\udc49': '',
        #r'\ud83c\udfa7': '',
        #r'\ud83e\udd1d': '',
        #r'\u2714': '',
        #r'\ud83d\udca1': '',
        r'\u23f0': '',
        # r'\ud83c\udf88': '',
        r'\u2': '',
        r'\u201e': '',
        r'\u26a1': '',
        # r'\ud83d\udd12': '',
        # r'\ud83d\ude80': '',  # Unicode for "ROCKET" emoji (🚀).
        # r'\ud83c\u': '',  # Represents other emojis or special characters.
        r'\u25b6': '',  # Unicode for "BLACK RIGHT-POINTING TRIANGLE" (▶), used for video/play buttons.
        r'\u2b05': '',
        r'\u0130': '',
        # r'\ud83c\udf2c': '',  # Unicode for "TROPICAL STORM" emoji (🌀)
        # r'\ud83c\uud83c': '',  # Represents other emojis or special characters.

    }

    for code, char in unicode_map.items():
        text = text.replace(code, char)

    return text




def remove_matches(text):
    # Regular expression to match Unicode escape sequences
    unicode_pattern = r'\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}'

    # Replace all matches with an empty string
    updated_string = re.sub(unicode_pattern, '', text)

    return updated_string




def extract_date_ddmmyyyy(iso_datetime: str) -> str:
    """
    Extracts and formats the date portion from an ISO 8601 datetime string
    into 'dd-mm-yyyy' format.

    Parameters:
        iso_datetime (str): An ISO 8601 datetime string (e.g., '2025-04-16T04:31:13Z').

    Returns:
        str: The date in 'dd-mm-yyyy' format.
    """
    dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d")



def data_transformations(all_articles):
    print("Starting data transformations")
    df = pd.DataFrame(all_articles)
    df['Title'] = df['Title'].apply(remove_html_and_script)
    df['Title'] = df['Title'].apply(unicode_handling)
    df['Title'] = df['Title'].apply(remove_matches)
    df['Summary'] = df['Summary'].apply(remove_html_and_script)
    df['Summary'] = df['Summary'].apply(unicode_handling)
    df['Summary'] = df['Summary'].apply(remove_matches)
    df['Date'] = df['Date'].apply(extract_date_ddmmyyyy)

    print("Data transformations completed")

    return df
