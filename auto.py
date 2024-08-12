import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Set the path to the ImageMagick binary
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

def split_video_with_text(video_path, segment_duration):
    video = VideoFileClip(video_path)
    video_duration = video.duration
    segments = []
    for i, start in enumerate(range(0, int(video_duration), segment_duration)):
        end = start + segment_duration
        if end > video_duration:
            end = video_duration
        segment = video.subclip(start, end)
        
        # Create a text clip
        text = f"Part {i + 1}"
        txt_clip = TextClip(text, fontsize=70, color='white', bg_color='black')
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(segment.duration)

        # Overlay text on video segment
        segment_with_text = CompositeVideoClip([segment, txt_clip])
        segment_path = f"segment_{i + 1}.mp4"
        segment_with_text.write_videofile(segment_path, codec="libx264")
        segments.append(segment_path)
        
    return segments

video_path = "movie.mkv"
segment_duration = 60  # 60 seconds
segments = split_video_with_text(video_path, segment_duration)
print("Created segments:", segments)
