import os
from moviepy import VideoFileClip, AudioFileClip
import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS



def extract_audio_from_video(video_path, audio_output_path):
    """Extracts audio from an MP4 video file."""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output_path)
    print(f"Audio extracted and saved to {audio_output_path}")


def transcribe_audio(audio_path, model_type="base"):
    """Transcribes audio to text using Whisper."""
    model = whisper.load_model(model_type)
    result = model.transcribe(audio_path)
    print("Transcription completed.")
    return result["text"]


def translate_text(text, target_language="hi"):
    """Translates text to the target language using Google Translate."""
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    print("Translation completed.")
    return translated


def text_to_speech(text, output_audio_path, language="hi"):
    """Converts translated text to speech."""
    tts = gTTS(text=text, lang=language)
    tts.save(output_audio_path)
    print(f"Hindi audio saved to {output_audio_path}")


def add_audio_to_video(video_path, audio_path, output_video_path):
    """Adds audio to the video file."""
    # Set the FFmpeg binary path
    os.environ["FFMPEG_BINARY"] = r"C:\ffmpeg\ffmpeg.exe"  # Update this with your actual FFmpeg path

    # Load the video file
    video = VideoFileClip(video_path)

    # Load the audio file
    audio = AudioFileClip(audio_path)

    # Set the audio to the video using 'with_audio'
    video_with_audio = video.with_audio(audio)

    # Write the final video with the new audio
    video_with_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    print(f"Video with new audio saved at {output_video_path}")


def translate_and_replace_video_audio(video_path, output_video_path, target_language="hi"):
    """Main function to extract audio, transcribe, translate, and replace audio in the video."""
    audio_path = "temp_audio.mp3"
    hindi_audio_path = "hindi_audio.mp3"

    try:
        # Step 1: Extract audio from video
        print("Extracting audio from video...")
        extract_audio_from_video(video_path, audio_path)

        # Step 2: Transcribe audio to text
        transcription = transcribe_audio(audio_path)

        # Step 3: Translate transcribed text to Hindi
        translated_text = translate_text(transcription, target_language)

        # Step 4: Convert translated text to Hindi speech
        text_to_speech(translated_text, hindi_audio_path, language=target_language)

        # Step 5: Replace original audio in video with Hindi audio
        add_audio_to_video(video_path, hindi_audio_path, output_video_path)

    finally:
        # Cleanup temporary files
        for temp_file in [audio_path, hindi_audio_path]:
            if os.path.exists(temp_file):
                os.remove(temp_file)


# Example Usage
if __name__ == "__main__":
    # Taking input from the user for the video path
    video_path = input("Enter the full path of the video (e.g., C:/path/to/video.mp4): ").strip()

    # Ensure that the file exists
    if not os.path.exists(video_path):
        print(f"Error: The video file at {video_path} does not exist.")
    else:
        # Generating the output file path with a custom name
        base_name = os.path.splitext(os.path.basename(video_path))[0]  # Extract the base name without extension
        output_video_path = os.path.join(os.path.dirname(video_path), f"{base_name}_translated.mp4")  # Custom name

        # Running the translation and audio replacement process
        translate_and_replace_video_audio(video_path, output_video_path, target_language="hi")
C:\Users\sagar\OneDrive\Desktop\videoplayback.mp4
