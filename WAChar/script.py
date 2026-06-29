import os
import sys
import numpy as np
import soundfile as sf
import webrtcvad
from moviepy import AudioFileClip, VideoClip, ImageClip

# ==========================================
# CONFIGURATION
# ==========================================
RECORDINGS_DIR = "recordings"  # Folder where your MP3 files are stored
IMAGE_SILENT = "silent.png"
IMAGE_TALKING = "talking.png"
OUTPUT_FILE = "output_video.mp4"

# Speech detection aggressiveness: 0 (lax) to 3 (very strict filter for noise)
VAD_AGGRESSIVENESS = 2 

FPS = 5 
# ==========================================

def select_audio_file():
    """Prompts the user to select an MP3 file from the recordings directory."""
    # Create the directory if it doesn't exist yet
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)
        print(f"Created folder '{RECORDINGS_DIR}'. Please place your MP3 files there and run the script again.")
        sys.exit(0)

    # List all .mp3 files in the folder
    mp3_files = [f for f in os.listdir(RECORDINGS_DIR) if f.lower().endswith('.mp3')]

    if not mp3_files:
        print(f"No MP3 files found in the '{RECORDINGS_DIR}' folder. Please add some and retry.")
        sys.exit(0)

    print("\nAvailable Audio Files:")
    for idx, filename in enumerate(mp3_files, start=1):
        print(f"[{idx}] {filename}")

    # Prompt user for choice
    while True:
        try:
            choice = input(f"\nSelect a file (1-{len(mp3_files)}): ").strip()
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(mp3_files):
                return os.path.join(RECORDINGS_DIR, mp3_files[choice_idx])
            else:
                print(f"Please enter a number between 1 and {len(mp3_files)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Dynamically select the audio file
    audio_file_path = select_audio_file()
    print(f"\nSelected: {audio_file_path}")

    print("Loading audio for video generation...")
    audio_clip = AudioFileClip(audio_file_path)
    duration = audio_clip.duration

    print("Loading character images...")
    clip_silent = ImageClip(IMAGE_SILENT).get_frame(0)
    clip_talking = ImageClip(IMAGE_TALKING).get_frame(0)

    print("Analyzing track specifically for human speech...")
    # Read audio file into a raw format for the Voice Activity Detector
    data, sample_rate = sf.read(audio_file_path)
    
    # If stereo, convert to mono for processing
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
        
    # Standardize sample rate to 16000Hz (highly recommended for WebRTCVAD)
    if sample_rate != 16000:
        import scipy.signal
        num_samples = int(len(data) * 16000 / sample_rate)
        data = scipy.signal.resample(data, num_samples)
        sample_rate = 16000

    # Convert float audio array to 16-bit PCM integers (required by VAD)
    pcm_data = (data * 32767).astype(np.int16).tobytes()

    # Initialize the Voice Activity Detector
    vad = webrtcvad.Vad(VAD_AGGRESSIVENESS)

    # Calculate frame sizes (30ms chunks are optimal for speech detection)
    frame_duration_ms = 30
    bytes_per_sample = 2
    frame_size = int(sample_rate * frame_duration_ms / 1000) * bytes_per_sample

    # Pre-map timestamps to speech status
    speech_timeline = []
    for i in range(0, len(pcm_data) - frame_size, frame_size):
        chunk = pcm_data[i:i + frame_size]
        timestamp = (i / frame_size) * (frame_duration_ms / 1000.0)
        
        # Check if this specific chunk contains actual speech
        is_speech = vad.is_speech(chunk, sample_rate)
        speech_timeline.append((timestamp, is_speech))

    print("Generating video frames based on speech patterns...")
    
    def make_frame(t):
        # Find the closest analyzed speech chunk for the current timestamp 't'
        is_talking = False
        for timestamp, speech_detected in speech_timeline:
            if timestamp <= t < timestamp + (frame_duration_ms / 1000.0):
                is_talking = speech_detected
                break
                
        if is_talking:
            return clip_talking
        else:
            return clip_silent

    # Build and render the video file
    video = VideoClip(make_frame, duration=duration)
    video = video.with_audio(audio_clip)

    print("Rendering final video asset...")
    video.write_videofile(
        OUTPUT_FILE, 
        fps=FPS, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    audio_clip.close()
    video.close()
    print(f"Success! Speech-tracked video saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
