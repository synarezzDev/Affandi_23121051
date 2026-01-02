import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_KEY = "AIzaSyCSzmU2G-J4AdMx4QIdEDDms0NB6ApxOkY"
genai.configure(api_key=API_KEY)

model_name = "gemini-pro"
try:
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            model_name = m.name
            break
    model = genai.GenerativeModel(model_name)
    print(f"Menggunakan model: {model_name}")
except Exception:
    model = genai.GenerativeModel("gemini-pro")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text_input = data.get("text", "").strip()
    mode = data.get("mode", "").strip()

    if not text_input:
        return jsonify({"error": "Teks materi tidak boleh kosong"}), 400

    if mode == "summarize":
        prompt = (
            "Rangkum materi berikut dalam bahasa Indonesia yang profesional dan akademik. "
            "Gunakan poin-poin yang ringkas, jelas, dan terstruktur tanpa menghilangkan inti konsep. "
            f"Materi: {text_input}"
        )

    elif mode == "quiz":
        prompt = (
            "Buatlah 5 soal kuis pilihan ganda tingkat perguruan tinggi berdasarkan materi berikut. "
            "Setiap soal harus memiliki 4 opsi jawaban (A-D) dan sertakan kunci jawaban di akhir. "
            f"Materi: {text_input}"
        )

    elif mode == "mindmap":
        prompt = (
            "Tuliskan HANYA kode Mermaid.js untuk mindmap dari materi berikut. "
            "Jangan sertakan penjelasan, komentar, atau teks lain. "
            "Output HARUS diawali dengan kata 'mindmap'. "
            f"Materi: {text_input}"
        )

    else:
        return jsonify({"error": "Mode tidak valid"}), 400

    try:
        response = model.generate_content(prompt)
        result_text = response.text if response.text else "Tidak ada output dari AI."
        return jsonify({"result": result_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)