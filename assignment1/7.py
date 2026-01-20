def custom_encoder(text):
    text_position = []
    for ch in text:
        ch = ch.lower()
        if "a" <= ch <="z":
            text_position.append(ord(ch) - ord("a"))
        else:
            text_position.append(-1)
    return text_position