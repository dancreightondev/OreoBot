import random
from oreos import Oreo, Layer

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
        )
    }
    
    return oreos

# Function to actually generate an oreo
def generate_oreo(oreo_type: Oreo, max_layers: int):
    match oreo_type.get_name(): # Get the name of the oreo and match it with the following cases
        case "Original":
            n_layers = random.randint(1,max_layers) # Assign a random number of layers, up to the maximum of `layer_count`
            generated_layers = [] # Initialise an array to store each layer in
            for n in range(n_layers): # And for each layer...
                generated_layers.append(random.choice(oreo_type.get_original_layers()).get_name()) # ...choose a random one
            
            return Oreo( # Finally, return an `Oreo` object
                name = "Original",
                generated_layers = generated_layers
            )
        case _:
            print("unknown oreo type")

# Main function
def main ():
    oreos = define_oreos() # Define the possible base oreos used for generation
    oreo_type = random.choice(list(oreos.values())) # Choose a random oreo
    max_layers = 10 # Set the maximum layer count
    new_oreo = generate_oreo(oreo_type, max_layers) # Generate an oreo using these parameters
    print(f"{new_oreo.get_name()} has the following layers:\n{new_oreo.get_generated_layers()}")

main()
