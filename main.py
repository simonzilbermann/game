import pygame
import  math
from game import Game

pygame.init()

#definir unr clock
clock = pygame.time.Clock()#rapiditer de l afichage du screen
FPS = 80

#generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")#titre
screen = pygame.display.set_mode((1080,720))#size

#importer de charget larriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer la banniere(page home)
banner = pygame.image.load('assets/banner.png')
banner =pygame.transform.scale(banner,(500,500))#size
banner_rect = banner.get_rect()#recupere le placement du banner
banner_rect.x = math.ceil(screen.get_width()/4)#larjeure de l ecran

#button pour lancer
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()#recupere le placement du button
play_button_rect.x = math.ceil(screen.get_width()/3.33)#larjeure de l ecran
play_button_rect.y = math.ceil(screen.get_height()/2)


#charger le jeu
game = Game()

running = True

#boucle tant que cette condition vrai
while running:

    #appliquer l arriere plan de notre jeu
    screen.blit(background,(0,-200))#largeur,auteur

    #verifier si le jeu a commence ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si le jeu na pas commence
    else:
        #ajouter mon cecran de bienvenue
        screen.blit(play_button,(play_button_rect))
        screen.blit(banner, (banner_rect))

    #mettre a jour l ecran
    pygame.display.flip()

    #si le jouur ferme cette fenetre
    for event in pygame.event.get():
        #que l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu !")
        # detecter si le joueur lache une touche
        elif event.type == pygame.KEYDOWN:
          game.pressed[event.key] = True

          #detecter si la touche espace est enclenchee pour lancer notre projectile
          if event.key == pygame.K_SPACE:
              if game.is_playing:
                game.player.launch_projectile()
              else:
                  # mettre le jeu en mode lance
                  game.start()
                  # jouer le son
                  game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:#pas utilise
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:#touche de la souris
            #verification pour savoir si la souris est en collosion avec le boutton jouer
            if play_button_rect.collidepoint(event.pos):#position du boutton play
                #mettre le jeu en mode lance
                game.start()
                #jouer le son
                game.sound_manager.play('click')
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)

            #touche sacader
            # qelle touch a ete utilisee
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()
            #     print("Deplacement vers la droite")
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()
            #     print("Deplacement vers la gauche")

