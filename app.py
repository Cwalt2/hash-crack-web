from flask import Flask, request, render_template
import hashlib
import os

app = Flask(__name__)

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

# --- Hash Cracking Function ---
def crack_hash(target_hash: str, algorithm: str, filepath: str):
    if not os.path.exists(filepath):
        return "Wordlist file not found."

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            word = line.strip()
            if hash_string(word, algorithm) == target_hash:
                return f"✅ Cracked! The password is: {word}"
    return "❌ Password not found in wordlist."

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_hash = request.form["hash"]
        algorithm = request.form["algorithm"]
        wordlist = request.form["wordlist"]

        # For now, we only support files already in 'wordlists/' folder
        filepath = f"wordlists/{wordlist}"
        result = crack_hash(user_hash.strip(), algorithm, filepath)

    return render_template("index.html", result=result)
