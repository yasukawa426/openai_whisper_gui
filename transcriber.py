import whisper  # type: ignore[import-untyped]


def transcribe_audio(audio_file: str, timestamp: bool = False, language: str | None = None, testing: bool = False) -> str:
    """Transcribe the `audio_file` and saves the result to file.

    Args:
        audio_file (str): The path to the audio file to be transcribed.
        language (str, optional): The language to use for transcription. Defaults to None resulting in auto-detection. 
        timestamp (bool, optional): Whether to include timestamps in the transcription. Defaults to False - WIP.
        testing (bool, optional): Whether to run in testing mode, returning Lorem Ipsum. Defaults to False.

    Returns:
        str: The transcribed text.
    """

    # print(torch.cuda.is_available())

    if testing:
        return "Excepteur Lorem officia enim aliquip sit pariatur dolor irure pariatur reprehenderit. Quis amet quis ullamco incididunt proident nisi sint. Nostrud pariatur duis ea irure veniam laborum veniam consequat sunt dolor nulla enim ullamco fugiat. Consectetur mollit sunt sint laborum voluptate occaecat commodo do elit deserunt adipisicing sint et voluptate. Irure id excepteur nostrud laboris labore sunt dolore elit Lorem quis cillum commodo nostrud ipsum." \
        "" \
        "Mollit reprehenderit deserunt tempor incididunt veniam sunt eu culpa irure. Occaecat excepteur reprehenderit ipsum sit et dolore enim veniam voluptate enim in laboris. Aliqua aute dolor id deserunt esse. Sit ut ut nisi ex fugiat laboris deserunt consequat laborum officia eiusmod."\
        "" \
        "Mollit reprehenderit deserunt tempor incididunt veniam sunt eu culpa irure. Occaecat excepteur reprehenderit ipsum sit et dolore enim veniam voluptate enim in laboris. Aliqua aute dolor id deserunt esse. Sit ut ut nisi ex fugiat laboris deserunt consequat laborum officia eiusmod."\
        "" \
        "Mollit reprehenderit deserunt tempor incididunt veniam sunt eu culpa irure. Occaecat excepteur reprehenderit ipsum sit et dolore enim veniam voluptate enim in laboris. Aliqua aute dolor id deserunt esse. Sit ut ut nisi ex fugiat laboris deserunt consequat laborum officia eiusmod."
    

    model = whisper.load_model("turbo")

    # audio = "audio.mp3"
    result = model.transcribe(audio_file, verbose=True,
                              word_timestamps=timestamp, language=language,)


    # print(result["text"])
    return result["text"]


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
