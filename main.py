import random
from oreos import Oreo

# Function to define the base oreos used to generate a post
def define_oreos():
    oreos = {
        0: Oreo("Original") # Original
    }
    
    return oreos

# Function to actually generate an oreo
def generate_oreo(oreo_type: Oreo, max_layers: int):
    match oreo_type.get_name(): # Get the name of the oreo and match it with the following cases
        case "Original":
            possible_layers = ["o", "re"] # Get layers for this oreo
            n_layers = random.randint(1,max_layers) # Assign a random number of layers, up to the maximum of `layer_count`
            for n in range(n_layers): # For each layer...
                print(random.choice(possible_layers)) # ...print the value
        case _:
            print("unknown oreo type")

# Main function
def main ():
    oreos = define_oreos() # Define the possible base oreos used for generation
    oreo_type = random.choice(list(oreos.values())) # Choose a random oreo
    max_layers = 10 # Set the maximum layer count
    generate_oreo(oreo_type, max_layers) # Generate an oreo using these parameters

main()
