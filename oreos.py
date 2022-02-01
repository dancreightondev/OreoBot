class Oreo:
    def __init__(self, name, original_layers=None, generated_layers=None):
        self.name = name
        self.original_layers = original_layers
        self.generated_layers = generated_layers

    def get_name(self):
        return self.name
    
    def get_original_layers(self):
        if self.original_layers is not None:
            return self.original_layers
        else:
            return f"{self.name} has no original layers. Did you mean to return the generated layers?"
    
    def get_generated_layers(self):
        if self.generated_layers is not None:
            return self.generated_layers
        else:
            return f"{self.name} has no generated layers. Did you mean to return the original layers?"
