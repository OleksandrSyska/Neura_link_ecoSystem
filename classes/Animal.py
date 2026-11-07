class Animal():
    def __init__(self,image,starting_destination,NS):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = starting_destination

        self.state = {
            "health":0, # 0-100
            "hunger":0, # 0-100
            "thirst":0, # 0-100
            "age":0, # 0-100; <25:baby ; >25: adult, can breed
            "fitness":0, # to detemine how well it was in generation
            "parent":0, # 0/1; determine if this specie has bred
            "energy":0 # 0-100; movement -E, food/water +E
        }

        self.NS = NS


    def draw(self,sc):
        sc.blit(self.image,self.rect)

    def move(self,dx,dy):
        self.rect.centerx += dx
        self.rect.centery += dy

    def breed(self):
        pass
    
    def eat(self):
        pass

    def get_pos(self):
        return self.rect