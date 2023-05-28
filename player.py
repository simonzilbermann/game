import pygame
from projectile import Projectile
import animation

#class Player
#ירושה animation pygame.sprite.Sprite (grafique)
class Player(animation.AnimateSprite):
    def __init__(self,game):
        self.game = game
        super().__init__('player')
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        #pluseure projectile
        self.all_projectiles = pygame.sprite.Group()
        #self.image = pygame.image.load('assets/player.png')
        #deplasmen
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        # infliger les degats
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur na plus de points de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # definir unr couleur pour la jauge de vie (vert)
        bar_color = (111, 210, 46)
        # definir unr couleur pour la jauge de vie de la arriere plan (grie)
        back_bar_color = (60, 63, 60)

        # definir la position de la jauge de vie ainsi que sa largeur et epaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        # definir la position de la jauge de vie en arriere plan ainsi que sa largeur et epaisseur
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]

        # dessiner la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        #creer une nouvelle instance de la class projectile
        self.all_projectiles.add(Projectile(self))
        #demarrer l animation du  lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur nes pas en collision avec un monster
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity