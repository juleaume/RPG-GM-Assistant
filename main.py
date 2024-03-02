import time
import urandom
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK

from chaos import get_chaos, get_transform
from names import get_human, get_goblin, get_elfe, get_dwarf, get_orc, get_saurien
from descriptions import (
    get_physical_description,
    get_mental_description,
    get_accessories,
    get_f_weapons,
    get_fo_weapons,
    get_sw_weapons,
    get_trait,
)

display = PicoGraphics(display=DISPLAY_INKY_PACK)
WIDTH, HEIGHT = display.get_bounds()
# you can change the update speed here!
# it goes from 0 (slowest) to 3 (fastest)
display.set_update_speed(2)

display.set_font("sans")

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

WHITE = 0x0
BLACK = 0xFF

BG = BLACK
FG = WHITE

FONT_SIZE = 0.9


# a handy function we can call to clear the screen
def clear():
    display.set_pen(BG)
    display.clear()
    display.update()
    display.set_pen(FG)


# set up
clear()


def draw_arrows():
    display.polygon([(WIDTH - 15, 30), (WIDTH - 5, 30), (WIDTH - 10, 15)])
    display.circle(WIDTH - 10, HEIGHT // 2, 5)
    display.polygon([(WIDTH - 15, HEIGHT - 30), (WIDTH - 5, HEIGHT - 30), (WIDTH - 10, HEIGHT - 15)])


class App:
    def __init__(self) -> None:
        self.is_displayed = False

    def on_a(self):
        pass

    def on_b(self):
        pass

    def on_c(self):
        pass

    def on_default(self):
        pass


class Cursor:
    symbol = ">"

    def __init__(self, *apps: App) -> None:
        self.y_offset = 25
        self.pos = 0
        self.x = 0
        self.y = 10
        self.apps = apps
        self.show()

    def draw(self):
        display.text(self.symbol, self.x, self.y, WIDTH, FONT_SIZE)

    def up(self) -> None:
        self.pos -= 1
        if self.pos < 0:
            self.pos = len(self.apps) - 1
        self.show()

    def down(self) -> None:
        self.pos += 1
        if self.pos >= len(self.apps):
            self.pos = 0
        self.show()

    def show(self) -> None:
        clear()
        for i, _app in enumerate(self.apps):
            display.text(_app.name, 20, self.y_offset * (i + 1), WIDTH, FONT_SIZE)
        display.text(self.symbol, 0, self.y_offset * (self.pos + 1), WIDTH, FONT_SIZE)
        draw_arrows()
        display.update()

    def run(self) -> App:
        return self.apps[self.pos]


class NameApp(App):
    pages = {
        "Humains": get_human,
        "Elfes": get_elfe,
        "Nains": get_dwarf,
        "Gobelins": get_goblin,
        "Orcs": get_orc,
        "Sauriens": get_saurien,
    }
    name = "Noms"

    def __init__(self) -> None:
        super().__init__()
        self.cursor_pos = 0
        self.font_size = 0.7

    @property
    def pages_name(self) -> list[str]:
        names = list(self.pages.keys())
        names.sort()
        return names

    @property
    def pos(self) -> str:
        return self.pages_name[self.cursor_pos]

    def show_page(self, for_page):
        clear()
        name_set = set()
        while (i := len(name_set)) < 6:
            name = for_page(urandom.random() > 0.5)
            if name not in name_set:
                display.text(name, 0, 21 * i + 10, WIDTH, self.font_size)
                name_set.add(name)
        display.update()

    def on_a(self):
        self.cursor_pos -= 1
        if self.cursor_pos < 0:
            self.cursor_pos = len(self.pages) + 1
        self.is_displayed = False

    def on_b(self):
        self.show_page(self.pages[self.pos])

    def on_c(self):
        self.cursor_pos += 1
        if self.cursor_pos >= len(self.pages):
            self.cursor_pos = 0
        self.is_displayed = False

    def on_default(self):
        if not self.is_displayed:
            clear()
            for i, page in enumerate(self.pages_name):
                display.text(page, 20, 10 + 20 * i, WIDTH, self.font_size)
            display.text(">", 0, 10 + 20 * self.cursor_pos, WIDTH, self.font_size)
            draw_arrows()
            self.is_displayed = True
            display.update()
        else:
            time.sleep(0.1)


class ChaosApp(App):
    name = "Chaos"
    pages = ["Effets", "Transformations"]

    def on_a(self):
        clear()
        display.text(get_chaos())

    def on_b(self):
        clear()
        display.text(get_transform())

    def on_c(self):
        clear()

    def on_default(self):
        if not self.is_displayed:
            clear()
            for i, page in enumerate(self.pages):
                display.text(page, 10, 20 + 40 * i, WIDTH, FONT_SIZE)
            self.is_displayed = True
            display.update()
        else:
            time.sleep(0.1)


class DescriptionApp(App):
    pages = {
        "Physique": get_physical_description,
        "Mentale": get_mental_description,
        "Objets": get_accessories,
        "Armes Fantasy": get_f_weapons,
        "Armes Star Wars": get_sw_weapons,
        "Armes Fallout": get_fo_weapons,
    }
    name = "Descriptions"

    def __init__(self) -> None:
        self.cursor_pos = 0
        super().__init__()

    @property
    def pages_name(self) -> list[str]:
        names = list(self.pages.keys())
        names.sort()
        return names

    @property
    def pos(self) -> str:
        return self.pages_name[self.cursor_pos]

    def show_page(self, for_page):
        number_of_items = 6
        clear()
        name_set = set()
        while (i := len(name_set)) < number_of_items:
            name = for_page()
            if name not in name_set:
                display.text(
                    name,
                    0,
                    20 * i + 10,
                    WIDTH,
                    FONT_SIZE,
                )
                name_set.add(name)
        display.update()

    def on_a(self):
        self.cursor_pos -= 1
        if self.cursor_pos < 0:
            self.cursor_pos = len(self.pages) + 1
        self.is_displayed = False

    def on_b(self):
        self.show_page(self.pages[self.pos])

    def on_c(self):
        self.cursor_pos += 1
        if self.cursor_pos >= len(self.pages):
            self.cursor_pos = 0
        self.is_displayed = False

    def on_default(self):
        if not self.is_displayed:
            clear()
            for i, page in enumerate(self.pages_name):
                display.text(page, 20, 10 + 20 * i, WIDTH, FONT_SIZE)
            display.text(">", 0, 10 + 20 * self.cursor_pos, WIDTH, FONT_SIZE)
            draw_arrows()
            self.is_displayed = True
            display.update()
        else:
            time.sleep(0.1)


class QuickNPC(App):
    name = "Vite, un PNJ!"
    pages = ["Description", "Loot"]

    def __init__(self):
        super().__init__()
        self.history = {
            "name": list(),
            "physical": list(),
            "mental": list(),
            "trait": list(),
            "accessory": list(),
        }
        self.names = {
            "Humain": get_human,
            "Nain": get_dwarf,
            "Elfe": get_elfe,
            "Orc": get_orc,
            "Saurien": get_saurien,
            "Gobelin": get_goblin,
        }
        self.font_size = 0.7

    def show_page(self, for_page):
        def choose(hist, generator, is_fem):
            var = generator(is_fem)
            while var in self.history[hist]:
                var = generator(is_fem)
            self.history[hist].append(var)
            if len(self.history[hist]) > 10:
                self.history[hist].pop(0)
            return var

        clear()
        if for_page == "Description":
            specie = urandom.choice(list(self.names.keys()))
            gender = urandom.random() > 0.5
            display.text(choose("name", self.names[specie], gender), 0, 10, WIDTH, self.font_size)
            display.text(specie, 0, 30, WIDTH, self.font_size)
            display.text(choose("physical", get_physical_description, gender), 0, 50, WIDTH, self.font_size)
            display.text(choose("mental", get_mental_description, gender), 0, 70, WIDTH, self.font_size)
            display.text(choose("trait", get_trait, gender), 0, 90, WIDTH, self.font_size)
            display.text(choose("accessory", get_accessories, None), 0, 110, WIDTH, self.font_size)
        elif for_page == "Loot":
            display.text(get_accessories(), 0, 20, WIDTH, self.font_size)
            display.text(get_accessories(), 0, 50, WIDTH, self.font_size)
            display.text(get_f_weapons(), 0, 80, WIDTH, self.font_size)
            display.text(get_f_weapons(), 0, 110, WIDTH, self.font_size)

        display.update()

    def on_a(self):
        self.show_page(self.pages[0])

    def on_b(self):
        self.show_page(self.pages[1])

    def on_c(self):
        self.show_page(self.pages[2])

    def on_default(self):
        if not self.is_displayed:
            clear()
            for i, page in enumerate(self.pages):
                display.text(page, 10, 20 + 40 * i, WIDTH, FONT_SIZE)
            self.is_displayed = True
            display.update()
        else:
            time.sleep(0.1)


app = None
display.set_pen(FG)
cursor = Cursor(QuickNPC(), NameApp(), ChaosApp(), DescriptionApp())


while app is None:
    if button_a.read():
        cursor.up()
    elif button_b.read():
        app = cursor.run()
        break
    elif button_c.read():
        cursor.down()
    time.sleep(0.1)

clear()

while True:
    if button_a.read():
        app.on_a()
    elif button_b.read():
        app.on_b()
    elif button_c.read():
        app.on_c()
    else:
        app.on_default()
    time.sleep(0.1)
