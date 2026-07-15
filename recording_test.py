import sounddevice as sd
import whisper

# sounddevice doc: https://python-sounddevice.readthedocs.io/en/0.5.3/usage.html
# useful: https://python-sounddevice.readthedocs.io/en/0.5.3/examples.html#recording-with-arbitrary-duration

print(
    f"Devices: {sd.query_devices()}\nDefault input device: {sd.default.device[0]}"
)


# Whisper expectes the numpy array audio to have a 16k samplerate, so for now we just record it like that. We could instead resample it to 16k but idk, yk.
fs = 16000  # Sample rate
sd.default.samplerate = fs  # Sample rate
seconds = 30  # Duration of recording
dtype = "float32"  # Data type of the recording
channels = 1  # Number of channels (1 for mono, 2 for stereo)


print("Recording...")

# sd.RawInputStream()
myrecording = sd.rec(
    int(seconds * fs),
    channels=channels,
    dtype=dtype,
    blocking=True
)
sd.wait()  # Wait until the recording is finished
print("Recording finished.")


myrecording = myrecording.flatten()  # Flatten the array to 1D

sd.play(myrecording, fs)
print("Playing flattened recording.")

print(myrecording.shape)
print(myrecording.min(), myrecording.max())


model = whisper.load_model("turbo")
print("Starting transcription...")
# whisper.DecodingOptions(sample_len=len(myrecording), language="pt")
result = model.transcribe(audio=myrecording, verbose=True, language="pt")


print(result["text"])
