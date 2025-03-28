from googletrans import Translator, LANGUAGES

def translate_text(text, target_language='sw'):
    """
    Translate text to the target language using Google Translate API.
    
    Args:
        text (str): Input text to translate.
        target_language (str): Language code (e.g., 'sw' for Swahili, 'en' for English).
    
    Returns:
        str: Translated text.
    """
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def main():
    print("Available languages:", LANGUAGES)
    
    examples = [
        ("Hello, how are you?", "en", "English to Swahili"),
        ("Kesho twaenda shule", "sw", "Swahili to English"),
        ("Machine translation is fascinating.", "sw", "English to Swahili"),
        ("Tutie bidii masomoni", "en", "Swahili to English"),
        ("Huu ni muhula wetu wa mwisho", "en", "Swahili to English")
    ]
    
    for text, target_lang, description in examples:
        translated = translate_text(text, target_lang)
        print(f"\n{description}:")
        print(f"Original: {text}")
        print(f"Translated: {translated}")

if __name__ == "__main__":
    main()


# OUTPUT
# Available languages: {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# English to Swahili:
# Original: Hello, how are you?
# Translated: Hello, how are you?
# Translated: Hello, how are you?
# Translated: Hello, how are you?

# Swahili to English:
# Translated: Hello, how are you?

# Translated: Hello, how are you?

# Swahili to English:
# Original: Kesho twaenda shule
# Translated: Kesho twaenda shule


# English to Swahili:
# Original: Machine translation is fascinating.
# Translated: Tafsiri ya mashine inavutia.

# Swahili to English:
# Original: Tutie bidii masomoni
# Translated: Let's work hard

# Swahili to English:
# Original: Huu ni muhula wetu wa mwisho
# Translated: This is our last semester