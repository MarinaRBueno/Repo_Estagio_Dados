import hashlib

while True:
    string = input("Digite uma string para gerar o hash: ")
    hash_string = hashlib.sha1(string.encode())
    hex_dig_string = hash_string.hexdigest()
    print(f"{hex_dig_string}\n")
