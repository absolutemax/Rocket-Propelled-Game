from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrian_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrian_map.append(list(row))
        return terrian_map

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path):
        sorted_files = sorted(img_files)
        for image in sorted_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list