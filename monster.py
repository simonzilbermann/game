import  pygame
import  random
import  animation

#class monstre
class Monster(animation.AnimateSprite):

    def __init__(self,game,name,size,offset=0):
        super().__init__(name,size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        #self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000+random.randint(0,300)
        self.rect.y = 540 - offset
        self.loop_amount = 10
        self.start_animation()

    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

        #renplace la valeure
    def set_loop_amount(self,amount):
        self.loop_amount = amount

    def damage(self,amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de points de vie est inferieur ou egal a 0
        if self.health <= 0:
            #Reaparaitre comme un nouveau monstre
            self.rect.x = 1000+random.randint(0,300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            #ajouter le nombre de points
            self.game.add_score(self.loop_amount)

            #si la barre d evenement est charge a son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer de jeu
                self.game.all_monsters.remove(self)

                # appel dela methode pour essayer de declencher la pluie de comet
                self.game.comet_event.attempt_fall()
    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self,surface):
        #definir unr couleur pour la jauge de vie (vert)
        bar_color = (111,210,46)
        # definir unr couleur pour la jauge de vie de la arriere plan (grie)
        back_bar_color = (60, 63, 60)

        #definir la position de la jauge de vie ainsi que sa largeur et epaisseur
        bar_position = [self.rect.x+10,self.rect.y-20,self.health ,5]
        # definir la position de la jauge de vie en arriere plan ainsi que sa largeur et epaisseur
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #dessiner la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)



    def forward(self):#avance de droite a gauche
        #le deplacement ne se fait que si il ny a pas de collision avec un goup de joueur
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -=self.velocity
        #si le monstre est en collisuon avec le joueur
        else:
            #infliger des degats
            self.game.player.damage(self.attack)

   #class mummy
class Mummy(Monster):

    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
        self.set_speed(3)
        self.set_loop_amount(20)

   #class Alien
class Alien(Monster):

    def __init__(self,game):
        super().__init__(game,"alien",(300,300),130)
        self.health = 250
        self.max_health = 250
        self.attack= 0.8
        self.set_speed(1)
        self.set_loop_amount(80)