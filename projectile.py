import  pygame

#class projectile
class Projectile(pygame.sprite.Sprite):
    #constructeur
    def __init__(self,player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))#size
        #deplasmen et position
        self.rect = self.image.get_rect()#position
        self.rect.x = player.rect.x +120
        self.rect.y = player.rect.y +80
        self.origin_image = self.image # pour garder l image originelle
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 8
        #(rotozoom) pour faire tourner
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)#maitre en centre

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):#fait avence le projectile
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile entre en conlision avec un monster
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #delete le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #verifier si notre projectile nes plus present sur le screen
        if self.rect.x > 1080:
            #delete le projectile
            self.remove()
            print("Projectile delete !")