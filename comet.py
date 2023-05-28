import  pygame
import  random

#class comete
class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        #definir l image associee a cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(10,800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event =comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #verifier si le nomre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("L evenement est finie")
            #remette la barre 0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monster
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
            #retirer la boule de feu
            self.remove()

        #si il ny a plus de meteor
        if len(self.comet_event.all_comets) == 0:
            print("L evenement est finie")
            #remettre la jauge au depart
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        #verivier si la metere touche le joueur
        if self.comet_event.game.check_collision(self,self.comet_event.game.all_players):
            print("Joueur touche !")
            #retirer la meteor
            self.remove()
            #subir 20 point de degats
            self.comet_event.game.player.damage(20)
