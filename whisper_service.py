import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect language first
    _, probs = model.detect_language(mel)
    detected_lang = max(probs, key=probs.get)
    print(f"Detected language: {detected_lang}")

    # Now transcribe using the detected language
    result = model.transcribe(audio_path, language=detected_lang)
    return result['text']