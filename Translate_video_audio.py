import moviepy as mp
import os

def add_audio_to_video(video_path, audio_path, output_video_path):
    """Adds audio to the video file."""
    # Set the FFmpeg binary path
    os.environ["FFMPEG_BINARY"] = r"C:\ffmpeg\ffmpeg.exe"  # Update this with your actual FFmpeg path

    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Load the audio file
    audio = mp.AudioFileClip(audio_path)

    # Set the audio to the video using 'with_audio'
    video_with_audio = video.with_audio(audio)

    # Write the final video with the new audio
    video_with_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")


# Example usage
if __name__ == "__main__":
    video_path = r"C:\Users\sagar\PycharmProjects\audioconvert\audio.mp4"  # Path to your video file
    audio_path = r"C:\Users\sagar\PycharmProjects\audioconvert\hindi_audio.mp3"  # Path to your audio file
    output_video_path = r"C:\Users\sagar\PycharmProjects\audioconvert\output_video.mp4"  # Path to save the new video

    add_audio_to_video(video_path, audio_path, output_video_path)
