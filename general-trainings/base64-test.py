import base64

# Decode the Base64 string
decoded_string = base64.b64decode("Rml4c2t5YWxpdHRsZTE3IyM=").decode("utf-8")
print(decoded_string)

encoded_string = base64.b64encode('Fixskyalittle17####'.encode()).decode("utf-8")
print(encoded_string)