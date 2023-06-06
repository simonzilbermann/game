import pygame
from  player import  Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


#class representer notre jeu
class Game:
    def __init__(self):
        #definir si le jeu a commence
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l evenement
        self.comet_event = CometFallEvent(self)
        #group de monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        #gerer le son
        self.sound_manager = SoundManager()
        #mettre le score a 0
        self.font = pygame.font.Font("assets/my_custom_font.ttf",25)
        self.score = 0


        #self.spawn_monster()#premier monster
        #self.spawn_monster()#deuxier monster

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)  # premier monster
        self.spawn_monster(Mummy)  # deuxier monster
        self.spawn_monster(Alien)

    def add_score(self,points=10):
        self.score += points


    def game_over(self):
        #remettre le jeu a neuf retirer les monster,remettre le joueur a 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()#group son monster
        self.score_max()
        self.comet_event.all_comets = pygame.sprite.Group() #maitre a 0
        self.player.health = self.player.max_health
        self.comet_event.reset_percent() #maitre a 0 la jauge
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')



    def update(self,screen):#le jeu
        #afficher le score sur screen

        score_text = self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text,(20,20))

        with open("score", "r") as f:
            Line = f.readlines()
            first_line = Line[0].strip()
            score_text_max = self.font.render(f" Max Score : {first_line}",1,(0,0,0))
            screen.blit(score_text_max, (800, 20))

        # appliquer l image de joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d evenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monster du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les comets du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l ensemble des image de mon group de projectiles
        self.player.all_projectiles.draw(screen)  # dessine tout les projectiles du group

        # appliquer l ensemble des image de mon group de monsters
        self.all_monsters.draw(screen)

        # appliquer l ensemble des image de mon group de comettes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller a gauche ou adroite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

            print(self.player.rect.x)

    def check_collision(self,sprite,group):#function de conlision
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def spawn_monster(self,monster_class_name):
        monster = Mummy(self)
        self.all_monsters.add(monster_class_name.__call__(self))

    def score_max(self):
        with open("score", "r") as f:
            Line = f.readlines()
            if self.score > int(Line[0]):
                with open("score", "w") as f:
                    f.write(f"{self.score}\n")





