from pygame import Surface as SURF
from random import randint as rint
from classes.colors import WHITE
class BG():
    def __init__(self,tiles,objects,SCW,SCH):
        self.tiles = tiles
        self.background = SURF((SCW, SCH))
        for row in range(SCW//16):
            for col in range(SCH//16):
                self.background.blit(
                    self.tiles[rint(0,len(self.tiles)-1)],
                    (row*16,col*16)
                )


        lake_count = 10
        for _ in range(lake_count):
            Wx = rint(0,SCW//16)
            Wy = rint(0,SCH//16)
            max_water_size = 10
            for row in range(SCW//16):
                for col in range(SCH//16):
                    dx = abs(row - Wx)
                    dy = abs(col - Wy)
                    d = dx + dy
                    chance = 100*(max_water_size-d)/max_water_size

                    if chance > 0 and rint(1,100) <= chance:
                        self.background.blit(
                            objects[1][rint(0,len(objects)-1)],
                            (row*16,col*16)
                        )

        for row in range(SCW//16):
            for col in range(SCH//16):
                if rint(1,20) == 10:
                    image = objects[0][rint(0,len(objects[0])-1)]
                    image.set_colorkey(WHITE)
                    self.background.blit(
                        image,
                        (row*16,col*16)
                    )
        

    def draw(self,sc):
        sc.blit(self.background,(0,0))