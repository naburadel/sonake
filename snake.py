import pygame,random

pygame.init()
W = 400
screen = pygame.display.set_mode((W,W))
c = pygame.time.Clock()

sn = [(200,200)]
dir = (20,0)
ap = (random.randrange(0,W,20),random.randrange(0,W,20))

running = True
while running:
        c.tick(10)
        for event in pygame.event.get():
                if event.type == pygame.quit:
                        running = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:dir = (0,-20)
                        if event.key == pygame.K_DOWN:dir = (0,20)
                        if event.key == pygame.K_LEFT:dir = (-20,0)
                        if event.key == pygame.K_RIGHT:dir = (20,0)
        head = (sn[0][0] + dir[0] ,sn[0][1]+dir[1])
        sn.insert(0,head)

        if head == ap:
            ap = (random.randrange(0,W,20),random.randrange(0,W,20))
        else:
               sn.pop()
        if (head[0]<0 or head[0]>= W or
        head[1]< 0 or head[1]>=W or
        head in sn[1:]):
               running = False

        screen.fill((20,20,20))
        for s in sn:
               pygame.draw.rect(screen,(0,255,100),(*s,20,20))
        pygame.draw.rect(screen,(255,50,50),(*ap,20,20))

        pygame.display.flip()
pygame.quit()
               


