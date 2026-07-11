import whisper
import torch
print(torch.cuda.is_available())

model = whisper.load_model("turbo")


audio = "sonho.m4a"
result = model.transcribe(audio, verbose=True)
print(result["text"])