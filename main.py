import tkinter
import transcriber
from tkinter import filedialog

audio: str = "None"


def choose_file():
    global audio
    file = filedialog.askopenfile(
        title="Select an audio file", filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")])

    if file:
        audio = file.name
        chosen_audio_label.config(text=f"Chosen file: {audio.split('/')[-1]}")
        print(f"Chosen file: {audio}")


window = tkinter.Tk()
window.title("Whisper GUI")
# window.geometry("1280x720")


# create the widget
frame = tkinter.Frame(window)
# pack the widget into the window
frame.pack()
frame.grid()

chosen_audio_label = tkinter.Label(frame, text=f"Chosen file: {audio}")
chosen_audio_label.grid(column=0, row=0)


btn_one = tkinter.Button(frame, text="Transcribe",
                         command=lambda: transcriber.transcribe_audio(audio))
btn_one.grid(column=0, row=1)

btn_two = tkinter.Button(frame, text="Choose file", command=lambda: choose_file())
btn_two.grid(column=1, row=1)

tkinter.Button(frame, text="Quit", command=window.destroy).grid(
    column=0, row=2)


window.mainloop()

