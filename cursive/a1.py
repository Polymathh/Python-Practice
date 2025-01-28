import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (voice, rate, volume)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Get available voices and set a voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice available

# Text to be spoken
text = "Hey, Wambugu Moses! Isn't Python awesome? Let's build something cool together."

# Speak the text
engine.say(text)
engine.runAndWait()
