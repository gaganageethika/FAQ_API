from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except:
        return text  # Fallback to original text if translation fails