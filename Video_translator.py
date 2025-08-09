from moviepy import VideoFileClip

video_translator.py
auto_video_dubber.py
translate_video_audio.py
def extract_audio_from_video(video_path, audio_output_path):
    """Extracts audio from an MP4 video file."""
    try:
        video = VideoFileClip(video_path)  # Load video
        audio = video.audio  # Get audio from the video
        audio.write_audiofile(audio_output_path)  # Save the audio to an output file
        print(f"Audio extracted and saved to {audio_output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_path = r"C:\Users\sagar\Downloads\videoplayback.mp4"  # Path to your video file
audio_output_path = r"C:\Users\sagar\PycharmProjects\audioconvert\extracted_audio.mp3"  # Path to save the extracted audio

extract_audio_from_video(video_path, audio_output_path)
