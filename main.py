import tkinter
import transcriber
from datetime import datetime
from tkinter import ttk, filedialog

audio: str = None
testing: bool = False


def choose_file():
    global audio
    file = filedialog.askopenfile(
        title="Select an audio file", filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")])

    if file:
        audio = file.name
        chosen_audio_label.config(text=f"Audio file: {audio.split('/')[-1]}")
        print(f"Chosen file: {audio}")


def transcribe_audio(audio: str, language: str | None = None):
    result = transcriber.transcribe_audio(
        audio, language=language if language != "auto" else None, testing=testing)

    open_transcription_window(result)


def open_transcription_window(text: str):
    window = tkinter.Toplevel(root)
    window.title("Transcription")

    window.maxsize(800, 600)

    label = ttk.Label(window, text="Transcription Result:", wraplength=500)
    label.pack(pady=5, padx=10)

    txt_container = ttk.Frame(window)
    txt_container.pack(pady=5, padx=10)
    txt_box = tkinter.Text(txt_container,

                           #    wrap=tkinter.WORD, width=window.maxsize()[
                           #    1], height=window.maxsize()[0] - 100,
                           )
    txt_box.insert(tkinter.END, text)
    # txt_box.config(state=tkinter.DISABLED)  # make the text box read-only

    txt_box.pack(pady=5, padx=10)

    btns_frame = ttk.Frame(window)
    btns_frame.pack(pady=10, padx=10)

    save_btn = ttk.Button(btns_frame, text="Save", command=lambda: save_transcription(
        txt_box.get("1.0", tkinter.END), window))
    save_btn.pack(pady=5, padx=5, side=tkinter.LEFT)

    discard_btn = ttk.Button(
        btns_frame, text="Discard", command=window.destroy)
    discard_btn.pack(pady=5, padx=5, side=tkinter.LEFT)


def save_transcription(text: str, window):
    print(text)

    # ask the user to select a directory to save the transcription with the initial directory set to the audio file's directory
    path = filedialog.askdirectory(title="Select a directory to save the transcription",
                                   initialdir="./" if testing else audio.rsplit("/", 1)[0])

    with open("transcription_test.txt" if testing else f"{path}/{audio.split('/')[-1].rsplit('.', 1)[0]}_transcription_{datetime.now().strftime('%H-%M-%S')}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        tkinter.messagebox.showinfo(
            "Transcription Saved", f"Transcription saved with success to {f.name}")
        window.destroy()
    


root = tkinter.Tk()
root.title("Whisper GUI")
# window.geometry("800x600")


# create the widget
frame = tkinter.Frame(root)
# pack the widget into the window
frame.pack()
frame.grid()


chosen_audio_label = ttk.Label(frame, text=f"Chosen file: {audio}")
# chosen_audio_label.grid(column=0, row=0)


# btn_one.grid(column=0, row=1)

languages = list(transcriber.get_language_options().values())
language_combobox = ttk.Combobox(
    frame, state="readonly", values=languages, justify="center", width=4)
language_combobox.set("auto")

choose_btn = ttk.Button(frame, text="Choose file",
                        command=lambda: choose_file())
# choose_btn.grid(column=1, row=1)

quit_btn = ttk.Button(frame, text="Quit", command=root.destroy)
# .grid(column=0, row=2)

trans_btn = ttk.Button(frame, text="Transcribe",
                       command=lambda: transcribe_audio(audio, language=language_combobox.get()))

widgets = [
    chosen_audio_label,
    choose_btn,
    language_combobox,
    trans_btn,
    quit_btn
]

for widget in widgets:
    widget.pack(pady=5, padx=5)


root.mainloop()
