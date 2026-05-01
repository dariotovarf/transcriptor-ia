from deep_translator import GoogleTranslator

MAX_CHARS = 4000  # margen seguro debajo de 5000

def split_text(text, max_chars=MAX_CHARS):
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 <= max_chars:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def translate_text(text):
    chunks = split_text(text)
    translated_chunks = []

    for chunk in chunks:
        translated = GoogleTranslator(source='auto', target='es').translate(chunk)
        translated_chunks.append(translated)

    return " ".join(translated_chunks)