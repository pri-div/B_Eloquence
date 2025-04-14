from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
from torch.serialization import safe_globals

# ✅ Trust all required classes now
with safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs]):
    tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

def text_to_speech(text, speaker_wav, language="en"):  # default language
    output_path = "output.wav"
    tts_model.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        file_path=output_path,
        language=language  # ✅ Fix: Add this!
    )
    return output_path