import random
from oreos import Oreo

def define_oreos():
    oreos = {
        "default": Oreo("Original")
    }
    
    return oreos

def generate_oreo(oreo_type: Oreo):
    match oreo_type.get_name():
        case "Original":
            possible_layers = ["o", "re"]
            n_layers = random.randint(1,10)
            for n in range(n_layers):
                print(random.choice(possible_layers))
        case _:
            print("unknown oreo type")

def main ():
    oreos = define_oreos()
    generate_oreo(random.choice(list(oreos.values())))

main()
