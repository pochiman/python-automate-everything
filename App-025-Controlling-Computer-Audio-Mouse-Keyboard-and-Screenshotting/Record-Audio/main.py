import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100

myrecording = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1)
# print(myrecording)
sounddevice.wait()
# print(myrecording)
write('output.mp3', fps, myrecording)
