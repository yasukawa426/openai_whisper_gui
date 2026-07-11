import whisper
import torch
print(torch.cuda.is_available())

model = whisper.load_model("turbo")


audio = "audio.mp3"
result = model.transcribe(audio, verbose=True)
print(result["text"])