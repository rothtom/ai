import os, sys, pygame

pygame.init()
ttf_path = os.path.join(sys.path[0], "OpenSans-Regular.ttf")
pygame.font.Font(ttf_path, 28)