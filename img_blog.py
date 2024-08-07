


import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import font_manager
import textwrap
import random
import pyperclip as p

from matplotlib import rcParams



designer_colors = [
    "#FFC5A6",  # Apricot
    "#FDAC98",  # Melon
    "#DC8E90",  # Light Coral
    "#A97882",  # Mountbatten Pink
    "#58545F",  # Davy's Gray
    "#BDE0FE",  # Uranian Blue
    "#FFC8DD",  # Fairy Tale
    "#FFAFCC",  # Carnation Pink
    "#D8F7F2",  # Mint Green
    "#CDB4DB",  # Thistle
    "#0033A0",  # Classic Blue
    "#FF6F61",  # Coral
    "#50C878",  # Emerald
    "#40E0D0",  # Turquoise
    "#36454F",  # Charcoal
    "#98FF98",  # Mint Green (already included)
    "#6A0D91",  # Royal Purple
    "#FFC0CB",  # Blush Pink
    "#708090"   # Slate Gray
]





def wrap_text(text, width):
    """
    Wrap text for Chinese characters and English words without breaking English words in half.
    Each Chinese character is considered twice the width of an English letter.
    """
    wrapped_lines = []
    paragraphs = text.split('\n')
    
    for paragraph in paragraphs:
        if paragraph == '':
            # Preserve empty lines
            wrapped_lines.append('')
            continue

        line = ""
        current_width = 0
        word = ""

        for char in paragraph:
            if '\u4e00' <= char <= '\u9fff':  # Chinese character
                char_width = 2
            else:
                char_width = 1

            if char.isspace():
                if current_width + len(word) > width:
                    wrapped_lines.append(line)
                    line = word + char
                    current_width = len(word) + char_width
                else:
                    line += word + char
                    current_width += len(word) + char_width
                word = ""
            elif char_width == 2:
                if current_width + char_width > width:
                    wrapped_lines.append(line)
                    line = char
                    current_width = char_width
                else:
                    line += word + char
                    current_width += len(word) + char_width
                word = ""
            else:
                if current_width + len(word) + char_width > width:
                    wrapped_lines.append(line)
                    line = word + char
                    current_width = len(word) + char_width
                    word = ""
                else:
                    word += char

        # Append any remaining text
        if current_width + len(word) > width:
            wrapped_lines.append(line)
            line = word
        else:
            line += word
        
        if line:
            wrapped_lines.append(line)

    return wrapped_lines


def add_text_to_image(background_color, output_path, rows, font_path, font_size=20, padding=10):
    """
    Adds formatted text to an image with a specified background color.

    Args:
        background_color (tuple): RGB values for the background color.
        output_path (str): Path to save the image with text.
        rows (list): List of text lines to add to the image.
        font_path (str): Path to the font file that supports Chinese characters.
        font_size (int): Font size of the text.
        padding (int): Padding from the edges.
    """
    # Load the font
    # font_prop = font_manager.FontProperties(fname=font_path, size=font_size)
    font_prop = font_manager.FontProperties(fname=font_path, size=font_size, weight='bold', style='italic')
    print("fff"*100, font_prop)  # Check the font properties
    

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 12))  # Adjust size as needed
    fig.patch.set_facecolor(background_color)
    ax.axis('off')

    # Define text height
    text_height = font_size * 1.2  # A rough estimate, adjust if needed

    # Calculate the maximum number of lines that fit in the image height
    fig_height_inches = fig.get_size_inches()[1]*0.6
    max_lines_per_image = int((fig_height_inches * fig.dpi - 2 * padding) / text_height)
    
    # Split rows into chunks that fit the image height
    for i in range(0, len(rows), max_lines_per_image):
        # chunk = rows[i:i + max_lines_per_image]
        chunk = [r.strip() for r in rows[i:i + max_lines_per_image]]
        text_chunk = '\n'.join(chunk)
        
        # Add text to the image
        ax.text(
            0.01, 0.99, text_chunk,
            fontsize=font_size,
            color='black',
            ha='left',
            va='top',
            bbox=dict(facecolor='none', edgecolor='none', pad=0),
            fontproperties=font_prop,
            transform=ax.transAxes
        )
        
        # Save the image
        fig.canvas.draw()
        img = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
        img.save(output_path.format(i // max_lines_per_image))
        print(f"Image saved to {output_path.format(i // max_lines_per_image)}")
        
        # Clear the figure for the next chunk
        ax.clear()
        # fig, ax = plt.subplots(figsize=(10, 12))
        fig, ax = plt.subplots(figsize=(int(12*3/4), 12))
        fig.patch.set_facecolor(background_color)
        ax.axis('off')



text = '''标题： 理解不同类型的人工智能

1, English: Each kind of AI has its own special function and way of working, just like tools in a toolbox.
Chinese: 每种人工智能都有其独特的功能和工作方式，就像工具箱中的工具一样。

2, English: In the following sections, we look at these different types of AI to understand what they’re like and how they work.
Chinese: 在接下来的部分，我们将探讨这些不同类型的人工智能，以了解它们的特点和工作原理。

3, English: We start with two main types:
Chinese: 我们从两种主要类型开始：

4, English: AI that learns from data, which we call machine learning (ML)
Chinese: 从数据中学习的人工智能，我们称之为机器学习（ML）

5, English: AI that follows specific rules
Chinese: 遵循特定规则的人工智能

6, English: Both types of AI have their own strengths, making them suitable for different kinds of tasks.
Chinese: 这两种类型的人工智能各有优点，使它们适用于不同类型的任务。

7, English: Understanding this will help you get a clear picture of how AI is changing our world, from health care to manufacturing and beyond.
Chinese: 理解这些将帮助你清楚地了解人工智能如何改变我们的世界，从医疗保健到制造业以及其他领域。

8, English: Each type of AI brings something valuable to the table, showing just how diverse and useful these technologies can be.
Chinese: 每种类型的人工智能都带来了一些有价值的东西，展示了这些技术的多样性和实用性。'''






def main():
    max_line_length = 50
    rows_ = wrap_text(p.paste(), max_line_length)

    # Example usage with multiple image files
    add_text_to_image(
        # background_color=(144/255, 238/255, 144/255),  # Light green background color
        background_color=random.choice(designer_colors),  # Light green background color
        output_path=r"C:\Users\34950\Desktop\temp_imgs\output_image_matplotlib_{:02d}.jpg",  # Use format string for multiple files
        # output_path=r"G:\main_work\learning_imgs\output_image_matplotlib_{:02d}.jpg",  # Use format string for multiple files
        rows=rows_,
        font_path=r"msyh.ttc"  # Replace with the path to your .ttc or .ttf font file
        # font_path= None  # Replace with the path to your .ttc or .ttf font file
    )


