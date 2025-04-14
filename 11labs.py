from elevenlabs.client import ElevenLabs
import elevenlabs
client = ElevenLabs(
  api_key="sk_aa769546ed738d59fcbac85656c3c826920404ccbb432ece",
)

# response = client.voices.get_all()
# print(response.voices)

from elevenlabs import play


audio = client.text_to_speech.convert(
    text="helooooo",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

elevenlabs.save(audio,"yashuu.mp3")