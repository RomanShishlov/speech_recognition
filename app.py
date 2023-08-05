from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():
    transcript = ""
    if request.method =="POST":
        print("form data received")

#ifno file found it will be redirected to the home page

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

#taking audio file, analyzing it with the speech rocognition
# module and got a transcript of that audio using google API
#using Wav files

        if file:
            recornizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recornizer.record(source)
            transcript = recornizer.recognize_google(data, key=None)




    return render_template('index.html', transcript = transcript)
if __name__ == "__main__":
    app.run(debug = True, threaded = True)