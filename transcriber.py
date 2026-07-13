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
def get_language_options() -> dict[str, str]:
    """Get the available language options.

    Returns:
        dict[str, str]: A dictionary of available language options sorted in alphabetical order in the format {language: code}.
    """
    sorted_languages = dict(
        sorted(
            whisper.tokenizer.LANGUAGES.items(),
            key=lambda item: item[1])
    )

    #reverses the dictionary to have the language as the key and the code as the value
    reverse_sorted_languages = {
        str.capitalize(language): code for code, language in sorted_languages.items()
    }

    return {
        "Auto-detect": "auto",
        **reverse_sorted_languages
    }
