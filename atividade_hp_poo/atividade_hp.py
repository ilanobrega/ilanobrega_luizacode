class HogwartsHouse:
    def __init__(self, name, color, founder):
        self.name = name
        self.color = color
        self.founder = founder
        
    def get_points_house(self):
        return f"A casa {self.name} possui a pontuação total \
                 de 50 pontos"
            
    def play_quidditch(self):
        return f"A pontuação de quadribol foi de 10 pontos"
    
hufflepuff = HogwartsHouse('Lufa-lufa',
                            'Amarelo e Preto',
                            'Helga Lufa-Lufa')
    
points_house = hufflepuff.get_points_house()
print('Pontuação ->', points_house)