import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx.all import resize

# Set the path to the ImageMagick binary
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

def split_video_with_text(video_path, num_segments, segment_duration=60, distance_from_bottom=50):
    segments = []
    try:
        # Load the video file
        video = VideoFileClip(video_path)
    except Exception as e:
        print(f"Error loading video: {e}")
        return segments

    original_width, original_height = video.size
    target_width, target_height = 1080, 1920  # Instagram Reels dimensions

    # Calculate padding to maintain aspect ratio
    scale_factor = min(target_width / original_width, target_height / original_height)
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    padding_width = (target_width - new_width) // 2
    padding_height = (target_height - new_height) // 2

    # Resize video while maintaining aspect ratio and adding padding
    try:
        video = video.fx(resize, width=new_width, height=new_height)
        video = video.margin(left=padding_width, right=padding_width, top=padding_height, bottom=padding_height, color=(0, 0, 0))
    except Exception as e:
        print(f"Error processing video: {e}")
        video.close()
        return segments

    video_duration = video.duration
    total_segments = int(video_duration // segment_duration)
    if num_segments > total_segments:
        print(f"Requested {num_segments} segments, but video can only be split into {total_segments} segments of {segment_duration} seconds each.")
        num_segments = total_segments

    for i in range(num_segments):
        start = i * segment_duration
        end = min(start + segment_duration, video_duration)
        
        try:
            # Create a subclip
            segment = video.subclip(start, end)

            # Create a text clip
            text = f"Part {i + 1}"
            txt_clip = TextClip(text, fontsize=70, color='white', bg_color='black', size=(1080, 100))

            # Set text position a bit above the bottom
            text_width, text_height = txt_clip.size
            pos = (new_width / 2 - text_width / 2, new_height - text_height - distance_from_bottom)
            txt_clip = txt_clip.set_position(pos).set_duration(segment.duration)

            # Overlay text on video segment
            segment_with_text = CompositeVideoClip([segment, txt_clip])

            segment_path = f"segment_{i + 1}.mp4"
            try:
                segment_with_text.write_videofile(segment_path, codec="libx264", threads=4, preset='fast')
                segments.append(segment_path)
            except Exception as e:
                print(f"Error writing segment {i + 1} to file: {e}")

        except Exception as e:
            print(f"Error processing segment {i + 1}: {e}")

        finally:
            # Free memory
            segment_with_text.close()
            segment.close()

    video.close()
    return segments

if __name__ == "__main__":
    video_path = "movie.mp4"
    try:
        num_segments = int(input("Enter the number of 60-second segments you want: "))
        if num_segments <= 0:
            raise ValueError("Number of segments must be a positive integer.")
        distance_from_bottom = int(input("Enter the distance from the bottom in pixels (e.g., 50): "))
        if distance_from_bottom < 0:
            raise ValueError("Distance from the bottom must be a non-negative integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        segments = split_video_with_text(video_path, num_segments, distance_from_bottom=distance_from_bottom)
        print("Created segments:", segments)
