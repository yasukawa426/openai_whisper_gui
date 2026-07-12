import whisper  # type: ignore[import-untyped]

def transcribe_audio(audio_file: str) -> None:
    """Transcribe the `audio_file` and saves the result to file.

    Args:
        audio_file (_type_): The path to the audio file to be transcribed.
    """

    # print(torch.cuda.is_available())

    model = whisper.load_model("turbo")


    # audio = "audio.mp3"
    result = model.transcribe(audio_file, verbose=True)
    # TODO: Save the result to a file? 
    print(result["text"])