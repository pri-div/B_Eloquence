from flask import Flask, request, jsonify
from flask_cors import CORS
from whisper_service import transcribe_audio
from translator_service import translate_text
from tts_service import text_to_speech
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Welcome to EloquenceAI Backend!"

@app.route('/process', methods=['POST'])
def process_audio():
    print("Request received!")
    file = request.files['audio']
    target_lang = request.form['target_lang']

     # Make sure the folder exists
    os.makedirs('test_audio', exist_ok=True)

    filepath = 'test_audio/input.wav'
    file.save(filepath)

    text = transcribe_audio(filepath)
    translated = translate_text(text, target_lang)
    output_path = text_to_speech(translated, speaker_wav=filepath, language=target_lang)

    return jsonify({
        'original_text': text,
        'translated_text': translated,
        'audio_file_path': output_path
    })

if __name__ == '__main__':
    app.run(debug=True)