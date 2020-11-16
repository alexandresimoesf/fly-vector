import pygame
import pygame.font

class Rotation():
    
    def __init__(self,x):
        self.vista = pygame.image.load(x)
        self.w, self.h = self.vista.get_size()
    #self.vista = pygame.transform.scale(self.vista, (self.w//2, self.h//2))
    
    def Rotate(self, surf, pos, angle):
        
        # calcaulate the axis aligned bounding box of the rotated image
        w, h       = self.w, self.h
        originPos  = (w//2, h//2)
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        
        # calculate the translation of the pivot
        pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot
        
        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])
        
        # get a rotated image
        rotated_image = pygame.transform.rotate(self.vista, angle)
        
        # rotate and blit the image
        surf.blit(pygame.image.load('unifei.png'), (5,5))
        surf.blit(rotated_image, origin)





