class Inventa:
    def __init__(self, items : list):
        self.items = items

    def __repr__(self):
        print("REPR")
        return "Inventa(list of items)"
    
    def __str__(self):
        print("STR")
        return ", ".join(self.items)
    
    # def __eq__(self, other):
    #     return self.items == other.items
    
    def __len__(self):
        return len(self.items)
    
    # def __hash__(self):
    #     return hash(self.items)
    

i = Inventa(["Magician Shield", "Sword of Disorder"])
j = Inventa(["Magician Shield", "Sword of Disorder"])
print(i == j)
print(len(i))
