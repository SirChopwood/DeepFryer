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
    nametag = str  # Basic, Boss, Healthbar
    nametag_offset_x = 0
    nametag_offset_y = 0
    colour = str  # "#ffffff"
    damage = 1
    health = 5
    saves = 8
    current_health = health

    def __init__(self, window):
        self.window = window
        if self.sprite_path:
            self.sprite = self.create_sprite(self.sprite_path)
        if self.nametag:
            self.set_nametag(self.name, self.nametag)

    def create_sprite(self, path, x=0, y=0, anchor="center"):
        img = Image.open(path)
        if self.sprite_scale:
            img = img.resize(self.sprite_scale, 0)
        if self.sprite_flip:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img = ImageTk.PhotoImage(img)
        self.window.image_refs.append(img)
        return self.window.canvas.create_image(x, y, anchor=anchor, image=img)

    def set_nametag(self, text, type="Basic"):
        if isinstance(self.nametag, list):
            for nametag in self.nametag:
                self.window.canvas.delete(nametag)
        elif isinstance(self.nametag, int):
            self.window.canvas.delete(self.nametag)

        if type == "Basic":
            self.nametag = self.window.canvas.create_text(self.x + self.nametag_offset_x,
                                                          self.y + self.nametag_offset_y,
                                                          text=text, anchor="center",
                                                          font=self.window.font_basic,
                                                          fill=self.colour)
        elif type == "Boss":
            self.nametag = self.window.canvas.create_text(self.x + self.nametag_offset_x,
                                                          self.y + self.nametag_offset_y,
                                                          text=text, anchor="center",
                                                          font=self.window.font_bigger,
                                                          fill=self.colour)
        elif type == "Healthbar":
            self.nametag = []
            self.nametag.append(self.window.canvas.create_rectangle(self.x + self.nametag_offset_x - 60,
                                                                 self.y + self.nametag_offset_y - 15,
                                                                 self.x + self.nametag_offset_x + 60,
                                                                 self.y + self.nametag_offset_y + 10,
                                                                 fill="#000000"))
            self.nametag.append(self.window.canvas.create_rectangle(self.x + self.nametag_offset_x - 59,
                                                                 self.y + self.nametag_offset_y - 14,
                                                                 self.x + self.nametag_offset_x + (((self.current_health / self.health) * 118) - 59),
                                                                 self.y + self.nametag_offset_y + 9,
                                                                 fill=self.colour))

            self.nametag.append(self.window.canvas.create_text(self.x + self.nametag_offset_x,
                                                            self.y + self.nametag_offset_y,
                                                            text=text, anchor="center",
                                                            font=self.window.font_basic,
                                                            fill="#ffffff"))
        elif type == "Bossbar":
            self.nametag = []
            self.nametag.append(self.window.canvas.create_rectangle(self.x + self.nametag_offset_x - 401,
                                                                 self.y + self.nametag_offset_y - 30,
                                                                 self.x + self.nametag_offset_x + 401,
                                                                 self.y + self.nametag_offset_y + 25,
                                                                 fill="#000000"))
            self.nametag.append(self.window.canvas.create_rectangle(self.x + self.nametag_offset_x - 40,
                                                                 self.y + self.nametag_offset_y - 14,
                                                                 self.x + self.nametag_offset_x + (((self.current_health / self.health) * 80) - 40),
                                                                 self.y + self.nametag_offset_y + 9,
                                                                 fill=self.colour))

            self.nametag.append(self.window.canvas.create_text(self.x + self.nametag_offset_x,
                                                            self.y + self.nametag_offset_y,
                                                            text=text, anchor="center",
                                                            font=self.window.font_bigger,
                                                            fill="#ffffff"))

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
    damage = 1
    health = 5
    saves = 8

    def __init__(self, window):
        self.name = names.get_first_name()
        super().__init__(window)


class WarriorFry(Fry):
    name = "Warrior"
    damage = 5
    health = 20
    saves = 5
    sprite_path = "Assets/Sprites/Warrior.png"


class ArcherFry(Fry):
    name = "Archer"
    damage = 15
    health = 10
    saves = 3
    sprite_path = "Assets/Sprites/Archer.png"


class RogueFry(Fry):
    name = "Rogue"
    damage = 20
    health = 5
    saves = 2
    sprite_path = "Assets/Sprites/Rogue.png"


class NecromancerFry(Fry):
    name = "Necromancer"
    damage = 0
    health = 15
    saves = 3
    revives = 4


class Mod(Entity):
    name = "ModCorp Intern"
    sprite_path = "Assets/Sprites/ModCorp.png"
    sprite_scale = (256, 256)
    nametag = "Boss"
    colour = "#ffffff"
    nametag_offset_x = 0
    nametag_offset_y = -200
    health = 500