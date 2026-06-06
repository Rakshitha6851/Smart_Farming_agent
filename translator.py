from deep_translator import GoogleTranslator

def translate_to_english(text):
    """
    Translate any language text to English
    """

    try:
        translated = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        return translated

    except Exception as e:
        print("Translation Error:", e)
        return text