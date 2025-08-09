import os
from moviepy import VideoFileClip, AudioFileClip
import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS


def extract_audio_from_video(video_path, audio_output_path):
    """Extracts audio from an MP4 video file."""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output_path)


def transcribe_audio(audio_path, model_type="base"):
    """Transcribes audio to text using Whisper."""
    model = whisper.load_model(model_type)
    result = model.transcribe(audio_path)
    return result["text"]


def translate_text(text, target_language="hi"):
    """Translates text to the target language using Google Translate."""
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated


def text_to_speech(text, output_audio_path, language="hi"):
    """Converts translated text to speech."""
    tts = gTTS(text=text, lang=language)
    tts.save(output_audio_path)


def replace_audio_in_video(video_path, new_audio_path, output_video_path):
    """Replaces the audio track in the video with a new audio file."""
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(new_audio_path)
    video_with_new_audio = video.set_audio(new_audio)
    video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")


def translate_and_replace_video_audio(video_path, output_video_path, target_language="hi"):
    """Main function to translate video audio to Hindi and replace its audio."""
    audio_path = "temp_audio.mp3"
    hindi_audio_path = "hindi_audio.mp3"

    try:
        # Step 1: Extract audio from video
        print("Extracting audio from video...")
        extract_audio_from_video(video_path, audio_path)

        # Step 2: Transcribe audio to text
        print("Transcribing audio to text...")
        transcription = transcribe_audio(audio_path)
        print("Transcription completed.")

        # Step 3: Translate transcribed text to Hindi
        print("Translating text to Hindi...")
        translated_text = translate_text(transcription, target_language)
        print("Translation completed.")

        # Step 4: Convert translated text to Hindi speech
        print("Generating Hindi audio...")
        text_to_speech(translated_text, hindi_audio_path, language=target_language)
        print("Hindi audio generated.")

        # Step 5: Replace original audio in video with Hindi audio
        print("Replacing audio in video...")
        replace_audio_in_video(video_path, hindi_audio_path, output_video_path)
        print("Video with Hindi audio saved at:", output_video_path)

    finally:
        # Cleanup temporary files
        for temp_file in [audio_path, hindi_audio_path]:
            if os.path.exists(temp_file):
                os.remove(temp_file)


# Example Usage
if __name__ == "__main__":
    video_path = r"C:\Users\sagar\PycharmProjects\audioconvert\audio.mp4"  # Path to your video file
    output_video_path = r"C:\Users\sagar\PycharmProjects\audioconvert\video_with_hindi_audio.mp4"  # Path to save the new video

    translate_and_replace_video_audio(video_path, output_video_path, target_language="hi")
