from PIL import Image, ImageTk
import names


class Entity:
    x = 0
    y = 0
    name = str
    sprite_path = str
    sprite = object
    sprite_scale = tuple
    sprite_flip = False
    nametag = str  # "Basic" or "Boss"
    nametag_offset_x = 0
    nametag_offset_x = 0
    colour = str  # "#ffffff"

    def __init__(self, window):
        self.window = window
        if self.sprite_path:
            self.sprite = self.create_sprite(self.sprite_path)
        if self.nametag:
            self.nametag = self.create_nametag(self.name)

    def create_sprite(self, path, x=0, y=0, anchor="center"):
        img = Image.open(path)
        if self.sprite_scale:
            img = img.resize(self.sprite_scale, 0)
        if self.sprite_flip:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img = ImageTk.PhotoImage(img)
        self.window.image_refs.append(img)
        return self.window.canvas.create_image(x, y, anchor=anchor, image=img)

    def create_nametag(self, text):
        if self.nametag == "Basic":
            return self.window.canvas.create_text(self.x + self.nametag_offset_x, self.y + self.nametag_offset_y,
                                                  text=text, anchor="center", font=self.window.font_basic,
                                                  fill=self.colour)
        if self.nametag == "Boss":
            return self.window.canvas.create_text(self.x + self.nametag_offset_x, self.y + self.nametag_offset_y,
                                                  text=text, anchor="center", font=self.window.font_bigger,
                                                  fill=self.colour)

    def set_position(self, x, y):
        self.window.canvas.move(self.sprite, -self.x + x, -self.y + y)
        self.window.canvas.move(self.nametag, -self.x + x, -self.y + y)
        self.x = x
        self.y = y

    def move(self, x, y):
        self.window.canvas.move(self.sprite, x, y)
        self.window.canvas.move(self.nametag, x, y)
        self.x = x
        self.y = y


class Fry(Entity):
    name = "French Fry"
    sprite_path = "Assets/Sprites/Fry.png"
    sprite_scale = (128, 128)
    sprite_flip = True
    nametag = "Basic"
    colour = "#7030ab"
    nametag_offset_x = 0
    nametag_offset_y = 70
    combat_class = object
    Damage = 1
    Health = 5
    Saves = 8

    def __init__(self, window):
        self.name = names.get_first_name()
        super().__init__(window)


class WarriorFry(Fry):
    name = "Warrior"
    Damage = 5
    Health = 20
    Saves = 5
    sprite_path = "Assets/Sprites/Warrior.png"


class ArcherFry(Fry):
    name = "Archer"
    Damage = 15
    Health = 10
    Saves = 3
    sprite_path = "Assets/Sprites/Archer.png"


class RogueFry(Fry):
    name = "Rogue"
    Damage = 20
    Health = 5
    Saves = 2
    sprite_path = "Assets/Sprites/Rogue.png"


class NecromancerFry(Fry):
    name = "Necromancer"
    Damage = 0
    Health = 15
    Saves = 3
    sprite_path = "Assets/Sprites/Rogue.png"
    Revives = 4


class Mod(Entity):
    name = "ModCorp Intern"
    sprite_path = "Assets/Sprites/ModCorp.png"
    sprite_scale = (256, 256)
    nametag = "Boss"
    colour = "#ffffff"
    nametag_offset_x = 0
    nametag_offset_y = -200