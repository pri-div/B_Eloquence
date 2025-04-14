from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_aa769546ed738d59fcbac85656c3c826920404ccbb432ece",
)

response = client.voices.get_all()
print(response.voices)