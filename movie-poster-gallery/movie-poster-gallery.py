import streamlit as st
import os
from PIL import Image, ImageDraw

# --- Set Page Config ---
st.set_page_config(page_title="Movie Poster Gallery", layout="wide")

safe_allow_html=True

# st.audio("background_music_legend.mp3", format="audio/mpeg", loop=True)

# Directory where your posters are stored
POSTER_DIR = "uploaded_posters"  # Make sure you put your posters here
os.makedirs(POSTER_DIR, exist_ok=True)
st.title("🎬 Movie Poster Gallery")

# Read posters
poster_files = [os.path.join(POSTER_DIR, f) for f in os.listdir(POSTER_DIR) if f.endswith(('png', 'jpg', 'jpeg'))]

if poster_files:
    cols = st.columns(4)  # 4 posters per row

    for idx, poster_file in enumerate(sorted(poster_files)):
        img = Image.open(poster_file)

        # Create rounded corner effect
        rounded_img = img.convert("RGBA")
        width, height = rounded_img.size

        radius = 30  # radius for rounded corners
        circle = Image.new('L', (radius * 2, radius * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

        alpha = Image.new('L', rounded_img.size, 255)
        alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
        alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (width - radius, 0))
        alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, height - radius))
        alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (width - radius, height - radius))

        rounded_img.putalpha(alpha)

        # Display image
        with cols[idx % 4]:
            st.image(rounded_img, use_column_width=True)
else:
    st.info("No posters found! Add them inside the 'uploaded_posters/' folder.")

# --- Background and Image Hover Effect ---
st.markdown(
    """
    <style>
    body {{
        background-color: #f5f5f5;
    }}
    .poster-container {{
        transition: transform 0.3s, box-shadow 0.3s;
        border-radius: 15px;
        overflow: hidden;
    }}
    .poster-container:hover {{
        transform: scale(1.05);
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
    }}
    img {{
        border-radius: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)