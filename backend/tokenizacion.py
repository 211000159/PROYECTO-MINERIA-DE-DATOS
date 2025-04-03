import fitz
import re
import pandas

with fitz.open(r"C:\Users\ChenC\OneDrive\Documentos\Analisis FODA.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()
nuevo_text = text.lower() 
nuevo_text = re.sub(r'http\\S+', '', nuevo_text)

# Eliminación de signos de puntuación
regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
nuevo_text = re.sub(regex , ' ', nuevo_text)
# Eliminación de números
nuevo_text = re.sub(r"\d+", ' ', nuevo_text)
# Eliminación de espacios en blanco múltiples
nuevo_text = re.sub("\\s+", ' ', nuevo_text)
# Tokenización por palabras individuales
nuevo_text = nuevo_text.split(sep = ' ')
# Eliminación de tokens con una longitud < 2
nuevo_text = [token for token in nuevo_text if len(token) > 1]
print(nuevo_text)