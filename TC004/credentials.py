import base64

tokenb64 = "TOKEN_EM_BASE64_AQUI"

# Decodifica de bytes base64 para bytes string
token = base64.b64decode(tokenb64)
# Decodifica bytes string para seu equivalente em UTF-8
token = token.decode("utf-8")