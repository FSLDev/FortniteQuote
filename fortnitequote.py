import os
import glob
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, VideoFileClip, CompositeVideoClip
from progressbar import ProgressBar, Percentage, Bar
from textwrap import wrap
import numpy as np

# List of quotes
quotes = ["\"In Fortnite,\nsurvival is the only statistic that matters.\"",
          "\"You don't loot the victory,\nyou earn it.\"",
          "\"Every bullet tells a story,\nmake sure yours ends with a Victory Royale.\"",
          "\"The storm isn't your enemy,\nunpreparedness is.\"",
          "\"Your pickaxe strikes are your\nfirst steps towards victory.\"",
          "\"The best loot can't\nbuy skill.\"",
          "\"Even the rarest weapon is common\nin the hands of defeat.\"",
          "\"Victory is born from strategy,\nnot speed.\"",
          "\"A swift build wins the high ground,\nbut a strong build wins the game.\"",
          "\"The game isn't won in the sky,\nbut on the ground.\"",
          "\"Winning isn't about outgunning the enemy,\nit's about outlasting them.\"",
          "\"A Victory Royale isn't the end,\nit's the beginning of the next game.\"",
          "\"Victory isn't found in a chest,\nit's built with your hands.\"",
          "\"A true player doesn't fear the storm,\nthey outlive it.\"",
          "\"The storm takes everything,\nexcept your will to win.\"",
          "\"In Fortnite, it's not the weapon that matters,\nbut the hand that wields it.\"",
          "\"In the Battle Bus, everyone is equal.\nOn the ground, only the best survive.\"",
          "\"The last one standing\nis the first to victory.\"",
          "\"Every shot fired is a step\ncloser to victory or defeat.\"",
          "\"Victory isn't found at the end of the game,\nbut in every moment leading up to it.\"",
          "\"The storm doesn't claim the fastest,\nbut the unprepared.\"",
          "\"Every build is a\nmonument to survival.\"",
          "\"Even the longest sniper shot can't reach\nas far as a well-laid plan.\"",
          "\"Fortnite is not a game of chance,\nbut a game of choice.\"",
          "\"In the world of Fortnite,\nsurvival is the only currency that matters.\"",
          "\"The rarity of your weapon doesn't\ndetermine your chances of victory.\"",
          "\"In the storm,\nevery second counts.\"",
          "\"Every decision in Fortnite is a step\ntowards victory or defeat.\"",
          "\"A shield potion can't protect\nyou from poor tactics.\"",
          "\"Every build you make is a\nfortress in the storm.\"",
          "\"The sound of a Victory Royale is the\nsweetest melody.\"",
          "\"In the eye of the storm,\nonly skill can save you.\"",
          "\"A golden Scar is worthless in the\nhands of a bronze player.\"",
          "\"In Fortnite,\ntime is the most precious resource.\"",
          "\"Fortnite isn't just a game,\nit's a test of will.\"",
          "\"The game doesn't end with a Victory Royale,\nit begins with it.\"",
          "\"In the final circle,\neveryone's a target.\"",
          "\"A Victory Royale isn't given,\nit's earned.\"",
          "\"The high ground is worth more than\nall the loot in the game.\"",
          "\"Even the best player is just one\nshot away from defeat.\"",
          "\"Every supply drop is a gift,\nbut not every gift is for you.\"",
          "\"In Fortnite, every decision\ncould be your last.\"",
          "\"Victory is not found in the loot,\nbut in the player.\"",
          "\"The storm is relentless, so\nmust be your will to win.\"",
          "\"In Fortnite, the last man standing\nis the first to win.\"",
          "\"Victory doesn't come to the fastest builder,\nbut to the smartest player.\"",
          "\"Every match in Fortnite is a\nnew chance for victory.\"",
          "\"Your survival isn't determined by the weapon you hold,\nbut the strategy you follow.\"",
          "\"In Fortnite, you're only as good\nas your last game.\"",
          "\"In the end, only one name\nwill be remembered.\""]


font_path = "Montserrat-Bold.ttf"
font_size = 50
stroke_width = 5

# Create a progress bar
bar = ProgressBar(max_value=len(quotes), widgets=[Percentage(), Bar()])

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

    # Update the progress bar
    bar.update(i+1)