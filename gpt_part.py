#!/usr/bin/env python3

import sys
import openai
import warnings
import subprocess

warnings.filterwarnings("ignore", category=DeprecationWarning)



# transcription audio
audio_file = open("/var/lib/asterisk/sounds/gpt/gpt6_incoming.wav", "rb")
transcription = openai.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
print(transcription.text)
transcripted_text = transcription.text

# chat completion
completion = openai.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": """
      xxxxxxxx
    """},
    {"role": "user", "content": " xxxxxxxxx"}
  ]
)

completion_response= completion.choices[0].message.content
print(completion_response)

text to speech
alloy, echo, fable, onyx, nova, and shimmer
speech_file_path = "shimmer.mp3"#"/var/lib/asterisk/sounds/gpt/tts_mp3.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input="xxxxxxxxxxxxxxx"#completion_response
)
response_tts= response.stream_to_file(speech_file_path)
print (response_tts)

# convert tts_mp3.mp3 into wav
speech_file_wav = "/var/lib/asterisk/sounds/gpt/tts_wav.wav"
subprocess.run([
    "sox", speech_file_path, "-r", "8000", "-c", "1", "-b", "16", speech_file_wav
])
print("convert finished")



