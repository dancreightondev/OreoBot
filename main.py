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
    n_layers = random.randint(1,max_layers) # Assign a random number of layers, up to the maximum count of `max_layers`
    generated_layers = [] # Initialise an array to store each layer in
    for n in range(n_layers): # And for each layer...
        generated_layers.append(random.choice(oreo_type.get_original_layers()).get_name()) # ...choose a random one
    
    return Oreo( # Finally, return an `Oreo` object
        name = oreo_type.get_name(),
        generated_layers = generated_layers
    )

# Function to create the output that will eventually get posted
def create_output(output_oreo: Oreo):
    output = Image.open("img/background.png") # Start creating the output image by opening the background layer
    output_w, output_h = output.size # Get the background's dimensions
    canvas = ImageDraw.Draw(output) # Draw the background

    font_size = 1 # Base (minimum) font size
    max_font_size = 144 # Maximum font size
    font = ImageFont.truetype("fnt/MatSaleh.ttf", font_size) # Set the font

    text = "".join(output_oreo.get_generated_layers()) # Set the text
    text_width_fraction = 0.70 # Fraction of the image width the text should be
    
    while (font.getsize(text)[0] < text_width_fraction*output.size[0]) & (font.getsize(text)[1] < max_font_size): # Iterate until the text size is just larger than the criteria
        font_size += 1
        font = ImageFont.truetype("fnt/MatSaleh.ttf", font_size)
    font_size -= 1 # Decrement font size by 1 to ensure it fits within the fraction specified
    font = ImageFont.truetype("fnt/MatSaleh.ttf", font_size) # Set the font
    
    text_w, text_h = canvas.textsize(text, font=font) # Get the text size in the specified font
    canvas.text(((output_w-text_w)/2, output_h-(text_h/0.75)), text, (0,0,0), font=font) # Draw the text centred on the canvas
    
    out_file_path = "img/out/out.png" # Set the output file path
    output.save(out_file_path, "PNG") # Save the output to the aforementioned file path
    print(f"{output_oreo.get_name()} has the following layers:\n{output_oreo.get_generated_layers()}")
    
    return out_file_path # Return the output file path

# Main function
def main ():
    oreos = define_oreos() # Define the possible base oreos used for generation
    oreo_type = random.choice(list(oreos.values())) # Choose a random oreo
    max_layers = 8 # Set the maximum layer count
    new_oreo = generate_oreo(oreo_type, max_layers) # Generate an oreo using these parameters
    create_output(new_oreo) # Create the output that will eventually get posted

main()
