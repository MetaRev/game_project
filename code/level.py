import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import IU
from enemy import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_spirtes = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.current_attack = None
        
        self.create_map()
        
        self.ui = IU()
        
    def create_map(self):
        layout = {
            'boundary': import_csv_layout('map\\map_FloorBlocks.csv'),
            'grass': import_csv_layout('map\\map_Grass.csv'),
            'object': import_csv_layout('map\\map_Objects.csv'),
            'entities': import_csv_layout('map\\map_Entities.csv')
        }
        
        graphics = {
            'grass': import_folder('graphics\\grass'),
            'object': import_folder('graphics\\objects')
        }
        print(graphics)
        
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y), [self.visible_spirtes, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['object'][int(col)]
                            Tile((x,y), [self.visible_spirtes, self.obstacle_sprites], 'object', surf)
                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                (x,y), 
                                [self.visible_spirtes], 
                                self.obstacle_sprites, 
                                self.create_attack, 
                                self.destroy_attack,
                                self.create_magic)
                            else:
                                if col == '390': monster_name = 'bamboo'
                                elif col == '391': monster_name = 'spirit'
                                elif col == '392': monster_name = 'raccoon'
                                else: monster_name = 'squid'
                                
                                Enemy(monster_name, (x,y), [self.visible_spirtes], self.obstacle_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_spirtes])
        
    def create_magic(self, style, strength, cost):
        print(style, strength, cost)
        
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        self.visible_spirtes.custom_draw(self.player)
        self.visible_spirtes.update()
        debug(self.player.direction)
        debug(self.player.status)
        self.ui.display(self.player)
        self.visible_spirtes.enemy_update(self.player)
    
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)
        
        self.floor_surface = pygame.image.load('graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0, 0))
        
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
                
    def enemy_update(self, player):
        enemies_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemies_sprites:
            enemy.enemy_update(player)
            
            
        