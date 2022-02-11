import random
from oreos import Oreo, Layer
from PIL import Image, ImageFont, ImageDraw

# Function to define the base oreos used to generate a post
def define_oreos():
    oreos = {

        # Original
        0: Oreo(
            name = "Original",
            original_layers = [
                Layer(
                    name = "o_top",
                    display_name = "O",
                    file_path = "original/o_top.png"
                ),
                Layer(
                    name = "re",
                    display_name = "RE",
                    file_path = "original/re.png"
                ),
                Layer (
                    name = "o_btm",
                    display_name = "O",
                    file_path = "original/o_btm.png"
                )
            ]
        ),

        # Golden
        1: Oreo(
            name = "Golden",
            original_layers = [
                Layer(
                    name = "golden_o_top",
                    display_name = "O",
                    file_path = "golden/golden_o_top.png"
                ),
                Layer(
                    name = "golden_re",
                    display_name = "RE",
                    file_path = "golden/golden_re.png"
                ),
                Layer(
                    name = "golden_o_btm",
                    display_name = "O",
                    file_path = "golden/golden_o_btm.png"
                )
            ]
        )
    }
    
    return oreos

# Function to actually generate an oreo
def generate_oreo(oreo_type: Oreo, max_layers: int):

    # Assign a random number of layers, up to the maximum count of `max_layers`
    n_layers = random.randint(1,max_layers)

    # Initialise an array to store each layer in
    generated_layers = []

    # And for each layer...
    for n in range(n_layers):
        generated_layers.append(random.choice(oreo_type.get_original_layers()).get_name()) # ...choose a random one
    
    # Finally, return an `Oreo` object
    return Oreo( 
        name = oreo_type.get_name(),
        generated_layers = generated_layers
    )

# Function to create the output that will eventually get posted
def create_output(output_oreo: Oreo):
    
    # Start creating the output image by opening the background layer
    output = Image.open("img/background.png")
    
    # Get the background's dimensions
    output_w, output_h = output.size

    # Draw the background
    canvas = ImageDraw.Draw(output)

    # Base (minimum) font size
    font_size = 1 

    # Maximum font size
    max_font_size = 144

    # Set the font
    font = ImageFont.truetype("fnt/MatSaleh.ttf", font_size)

    # Set the text
    text = "".join(output_oreo.get_generated_layers())

    # Set the fraction of the image width that the text should be
    text_width_fraction = 0.70
    
    # Increase the font size while the text width is less than the desired width and the text height is less than the maximum font size
    while (font.getsize(text)[0] < text_width_fraction*output.size[0]) & (font.getsize(text)[1] < max_font_size):
        font_size += 1
        font = ImageFont.truetype("fnt/MatSaleh.ttf", font_size)
    
    # Get the text size in the specified font
    text_w, text_h = canvas.textsize(text, font=font)
    
    # Draw the text horizontally centred at the bottom of the canvas
    canvas.text(((output_w-text_w)/2, output_h-(text_h/0.75)), text, (0,0,0), font=font)

    # Set the output file path
    out_file_path = "img/out/out.png"

    # Save the output to the aforementioned file path
    output.save(out_file_path, "PNG")
    print(f"{output_oreo.get_name()} has the following layers:\n{output_oreo.get_generated_layers()}\nSaved image to '{out_file_path}'")
    
    # Return the output file path
    return out_file_path 

# Main function
def main ():
    
    # Define the possible base oreos used for generation
    oreos = define_oreos()

    # Choose a random oreo type
    oreo_type = random.choice(list(oreos.values()))

    # Set the maximum layer count
    max_layers = 8

    # Generate an oreo using these parameters
    new_oreo = generate_oreo(oreo_type, max_layers)

    # Create the output that will eventually get posted
    create_output(new_oreo)

main()
