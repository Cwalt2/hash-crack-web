import hashlib

f2 = "wordlists/word1.txt"

# --- Hashing Function ---
def hash_string(text: str, algorithm: str = "md5") -> str:
    byte_text = text.encode()

    if algorithm == "md5":
        return hashlib.md5(byte_text).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(byte_text).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(byte_text).hexdigest()
    else:
        return "Unsupported algorithm."

hashWord = "helo" # this is supposed to be secret
hash = (hash_string(hashWord, "sha1"))

print("hash input is", hash)

with open('wordlists/word1.txt', 'r') as file:
    for line in file:
        a = [line.strip() for line in file]

        for i in a:
            cracked = hash_string(i, "sha1")

            if cracked == hash:
                print("Cracked!", cracked, "password is", i)
            else:
                continue
            