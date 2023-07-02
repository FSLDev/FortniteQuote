# FortniteQuote
FortniteQuote is a Python project that overlays a list of Fortnite quotes onto a video background. 

## Prerequisites
Before running this script, you need to have the following libraries installed:

- PIL (Pillow)
- moviepy
- progressbar
- textwrap
- numpy

You can install these libraries using pip:

```bash
pip install pillow moviepy progressbar2 textwrap3 numpy
```

#How to Use
Clone this repository to your local machine.

Update the `quotes` list in the Python script with your desired quotes.

Make sure to have a video file in the `input` directory. This will be used as the background for the quotes.

Run the Python script:
```bash
python fortnitequote.py
```
The videos with the overlaid quotes will be saved in the `output` directory.

#Code Example
Here is a snippet of the code in this project:

```bash
# Load the input video
input_video = VideoFileClip("input/Fortnite-Quote-Background.mp4")

max_chars = 30  # Maximum number of characters per line

font = ImageFont.truetype(font_path, font_size)

for i, quote in enumerate(quotes):
    # Remove quote marks and split into lines of maximum length
    quote_lines = wrap(quote.replace('\"', ''), max_chars)
    
    # Join lines with newline character
    formatted_quote = '\n'.join(quote_lines)

    # Create a new image with transparent background
    text_image = Image.new('RGBA', input_video.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(text_image)

    # Draw the text with stroke
    w, h = d.textsize(formatted_quote, font=font)
    x, y = (input_video.size[0] - w) / 2, (input_video.size[1] - h) / 2
    d.text((x, y), formatted_quote, fill='white', stroke_width=stroke_width, stroke_fill='black', font=font)

    # Create a clip from the image
    text_clip = ImageClip(np.array(text_image)).set_duration(input_video.duration)

    # Create a composite video with text and input video
    final_clip = CompositeVideoClip([input_video, text_clip])

    # Sanitize the quote to use it as a filename
    sanitized_quote = quote.replace('\"', '').replace(' ', '_').replace('\n', '_').replace(',', '').replace('.', '')

    # Export the final video
    final_clip.write_videofile(os.path.join("output", f"{sanitized_quote}.mp4"), codec='libx264')
```
