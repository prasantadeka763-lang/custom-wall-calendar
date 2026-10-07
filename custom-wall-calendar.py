import calendar
from PIL import Image, ImageDraw, ImageFont

def generate_december_calendar(photo_path, output_path):
    # Set standard canvas width and section heights
    width = 800
    photo_height = 550
    cal_height = 550
    total_height = photo_height + cal_height

    # 1. Open and resize your uploaded profile photo
    try:
        photo = Image.open(photo_path)
        # Resize to fit the exact width of our template
        photo = photo.resize((width, photo_height))
    except FileNotFoundError:
        print(f"Error: Could not find image at {photo_path}")
        return

    # 2. Create base canvas and paste the photo at the top
    canvas = Image.new("RGB", (width, total_height), "white")
    canvas.paste(photo, (0, 0))
    
    draw = ImageDraw.Draw(canvas)
    
    # 3. Setup standard system typography fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 38)
        header_font = ImageFont.truetype("arial.ttf", 20)
        day_font = ImageFont.truetype("arial.ttf", 22)
    except IOError:
        # Fallback if specific TrueType system fonts are missing
        title_font = header_font = day_font = ImageFont.load_default()

    # 4. Write Month Title centered below the image
    y_offset = photo_height + 40
    draw.text((width // 2, y_offset), "DECEMBER 2026", fill="#1a1a1a", font=title_font, anchor="mm")
    
    # 5. Build Weekday Header labels (Mon - Sun)
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    col_width = width / 7
    y_offset += 50
    
    for i, day_name in enumerate(weekdays):
        x_pos = (i * col_width) + (col_width / 2)
        # Weekend headers colored red for visibility
        text_color = "#d9383a" if i >= 5 else "#555555"
        draw.text((x_pos, y_offset), day_name, fill=text_color, font=header_font, anchor="mm")

    # 6. Build the Numeric Date Grid
    y_offset += 45
    row_height = 60
    
    # Generates a matrix structure representing December 2026 dates
    december_matrix = calendar.monthcalendar(2026, 12)
    
    for row in december_matrix:
        for col, day in enumerate(row):
            if day != 0:  # Exclude padding empty days from adjacent months
                x_pos = (col * col_width) + (col_width / 2)
                # Sunday/Saturday dates highlighted red
                date_color = "#d9383a" if col >= 5 else "#222222"
                draw.text((x_pos, y_offset), str(day), fill=date_color, font=day_font, anchor="mm")
        y_offset += row_height

    # 7. Export file output
    canvas.save(output_path)
    print(f"Successfully generated calendar layout: {output_path}")

# --- execution ---
# 1. Save your uploaded image to your directory naming it "profile_photo.png"
# 2. Run the script function below:
generate_december_calendar(
    photo_path="profile_photo.png", 
    output_path="december_final_wallpaper.jpg"
)
