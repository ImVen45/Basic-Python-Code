import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))  # select your pdf file in place of file.pdf

import pyttsx3
# Initialize the speaker.
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   
print(rate)
speaker.setProperty('rate', 200)    # 200 means 2x Speed

voices = speaker.getProperty('voices')
print(voices)

#changing index, changes voices, 0 for male.
#speaker.setProperty('voice', voices[0].id)

#changing index, changes voices, 1 for female.
speaker.setProperty('voice', voices[1].id)

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()


engine = pyttsx3.init()

# volume ranges from 0 to 1, where 0 is the min volume and 1 being the max volume.
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
