#!/usr/bin/env python3
"""
Generate simple PNG icons for the Dark Space Theme extension.
Creates icons in sizes 16x16, 48x48, and 128x128.
"""

import random

try:
    from PIL import Image, ImageDraw
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL/Pillow not available. Installing...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'pillow'])
    from PIL import Image, ImageDraw

def create_icon(size):
    """Create a simple dark space themed icon."""
    # Create image with dark background
    img = Image.new('RGB', (size, size), color='#121212')
    draw = ImageDraw.Draw(img)
    
    # Draw purple circle in center
    center = size // 2
    radius = size // 3
    draw.ellipse(
        [center - radius, center - radius, center + radius, center + radius],
        fill='#9400ff'
    )
    
    # Draw small white stars
    star_positions = [
        (size // 4, size // 4),
        (size * 3 // 4, size // 4),
        (size // 4, size * 3 // 4),
        (size * 3 // 4, size * 3 // 4),
    ]
    
    for x, y in star_positions:
        star_size = max(1, size // 16)
        draw.ellipse([x - star_size, y - star_size, x + star_size, y + star_size], fill='white')
    
    return img

def create_theme_image(width, height, seed=None):
    """Create a dark space themed background image."""
    import random
    if seed is not None:
        random.seed(seed)
    
    img = Image.new('RGB', (width, height), color='#000000')
    draw = ImageDraw.Draw(img)
    
    # Draw random stars
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        color = (brightness, brightness, brightness)
        draw.ellipse([x, y, x + size, y + size], fill=color)
    
    return img

def create_animated_gif(width, height, filename, frames=10, duration=200):
    """Create an animated GIF with twinkling stars."""
    import random
    random.seed(42)  # Consistent star positions
    
    # Generate star positions once
    star_positions = []
    for _ in range(150):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        size = random.randint(1, 3)
        star_positions.append((x, y, size))
    
    frames_list = []
    for frame in range(frames):
        img = Image.new('RGB', (width, height), color='#000000')
        draw = ImageDraw.Draw(img)
        
        for x, y, size in star_positions:
            # Vary brightness for twinkling effect
            brightness_offset = random.randint(0, 100)
            brightness = 155 + brightness_offset
            color = (brightness, brightness, brightness)
            draw.ellipse([x, y, x + size, y + size], fill=color)
        
        frames_list.append(img)
    
    # Save as animated GIF
    frames_list[0].save(
        filename,
        save_all=True,
        append_images=frames_list[1:],
        duration=duration,
        loop=0,
        optimize=True
    )
    print(f'Created {filename}')

def main():
    # Generate icons
    sizes = [16, 48, 128]
    
    for size in sizes:
        icon = create_icon(size)
        filename = f'img/icon{size}.png'
        icon.save(filename)
        print(f'Created {filename}')
    
    # Generate theme images
    # Background for NTP and frame (animated GIF)
    create_animated_gif(1920, 1080, 'img/background.gif', frames=10, duration=200)
    
    # Also generate static PNG version
    background_static = create_theme_image(1920, 1080, seed=42)
    background_static.save('img/background.png')
    print('Created img/background.png')
    
    # Toolbar background - simple 1x1 pixel for Brave
    toolbar = Image.new('RGB', (1, 1), color='#121212')
    toolbar.save('img/toolbar.png')
    print('Created img/toolbar.png')
    
    # Tab background - simple 1x1 pixel for Brave
    tab_bg = Image.new('RGB', (1, 1), color='#1a1a1a')
    tab_bg.save('img/tab_background.png')
    print('Created img/tab_background.png')
    
    print('All icons and theme images generated successfully!')

if __name__ == '__main__':
    main()
