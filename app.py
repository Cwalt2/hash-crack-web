from flask import Flask, request, render_template
import hashlib

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

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    hashed = None
    if request.method == 'POST':
        user_input = request.form['plaintext']
        algorithm = request.form['algorithm']
        hashed = hash_string(user_input, algorithm)
    return render_template('index.html', hashed=hashed)
