from modules.services.voice_service import VoiceService

voice = VoiceService()

print("=== Normal Voice ===")
voice.speak("This is the default voice.")

voice.settings.set_rate(250)

print("=== Fast Voice ===")
voice.speak("Now I am speaking much faster.")

voice.settings.set_volume(0.3)

print("=== Low Volume ===")
voice.speak("My volume has been reduced.")

voice.settings.disable()

print("=== Muted ===")
voice.speak("You should not hear this sentence.")

voice.settings.enable()

print("=== Enabled Again ===")
voice.speak("Voice has been enabled again.")