import hashlib

filepath = "wordlists/word1.txt"
hashWord = "helo" # this is supposed to be secret


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

hash = (hash_string(hashWord, "sha1"))
print("hash input is", hash)

def  crack_hash(hash: str, filepath: str = "wordlists/word1.txt"):
    with open(filepath, 'r') as file:
        for line in file:
            words = [line.strip() for line in file]

            for word in words:
                cracked = hash_string(word, "sha1")

                if cracked == hash:
                    print("Cracked!", cracked, "password is", word)
                else:
                    continue

print(crack_hash(hash, "wordlists/word1.txt"))

