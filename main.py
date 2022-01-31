import random

def generate_oreo(oreo_type: str):
    match oreo_type:
        case "regular":
            possible_layers = ["o", "re"]
            n_layers = random.randint(1,10)
            for n in range(n_layers):
                print(random.choice(possible_layers))
        case _:
            print("unknown oreo type")

def main ():
    generate_oreo("regular")

main()
