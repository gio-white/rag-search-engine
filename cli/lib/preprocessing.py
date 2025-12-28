import string

def preprocessing(text:str) -> str:
    res = text.lower()
    translation_map = str.maketrans({k: None for k in string.punctuation})
    res = res.translate(translation_map)
    return res