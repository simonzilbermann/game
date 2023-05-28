import pygame

#class pour animation
class AnimateSprite(pygame.sprite.Sprite):

    #definir les chose a faire a la creation de l entite
    def __init__(self,sprite_name,size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0 #commencer l animation a l image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #definir une method pour demarrer l animation
    def start_animation(self):
        self.animation = True

    #definir une method pour animer le sprite
    def animate(self,loop=False):

        #verifier si l animation est active
        if self.animation:

            #passer a l image suivante
            self.current_image += 1

            #verifier si on a atteint la fin de l animation
            if self.current_image >= len(self.images):
                #remettre l animation a 0
                self.current_image = 0

                #verifier si l animation n est pas en mode boucle
                if loop is False:
                    # desactivation de l animation
                    self.animation = False

            #modifier l image precedant par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#definir une function pour charger les image d un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images =[]
    #recuperer le chemin du dossier pour ce sprite
    path=f'assets/{sprite_name}/{sprite_name}'

    #boucler sur chaque image dans ce dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        #return list d images
    return images


#definir un dictionnaire qui va contenir les images chargees de chaque sprite
animations = {
    'mummy':load_animation_images('mummy'),
    'player':load_animation_images('player'),
    'alien':load_animation_images('alien')
}