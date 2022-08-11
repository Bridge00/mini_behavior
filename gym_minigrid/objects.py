from .rendering import *
from .bddl import OBJECT_TO_IDX
from .utils.globals import COLOR_TO_IDX, COLORS
from .utils.objects_base import WorldObj, FurnitureObj


class Goal(WorldObj):
    def __init__(self, color='green', name='goal'):
        super().__init__('goal', color=color, name=name, can_overlap=True)

    def render(self, img):
        fill_coords(img, point_in_rect(0, 1, 0, 1), COLORS[self.color])


########################################################################################################################

class Apple(WorldObj):
    def __init__(self, color=None, name='apple'):
        super(Apple, self).__init__('apple', color, name)


class Ashcan(WorldObj):
    def __init__(self, color=None, name='ashcan'):
        super(Ashcan, self).__init__('ashcan', color, name, can_contain=True)


class Backpack(WorldObj):
    def __init__(self, color=None, name='backpack'):
        super(Backpack, self).__init__('backpack', color, name, can_contain=True)


class Ball(WorldObj):
    def __init__(self, color=None, name='ball'):
        super(Ball, self).__init__('ball', color, name)


class Banana(WorldObj):
    def __init__(self, color=None, name='banana'):
        super(Banana, self).__init__('banana', color, name)


class Basket(WorldObj):
    def __init__(self, color=None, name='basket'):
        super(Basket, self).__init__('basket', color, name, can_contain=True)


class Beef(WorldObj):
    def __init__(self, color=None, name='beef'):
        super(Beef, self).__init__('beef', color, name)


class Bin(WorldObj):
    def __init__(self, color=None, name='bin'):
        super(Bin, self).__init__('bin', color, name, can_contain=True)


class Blender(WorldObj):
    def __init__(self, color=None, name='blender'):
        super(Blender, self).__init__('blender', color, name)


class Book(WorldObj):
    def __init__(self, color=None, name='book'):
        super(Book, self).__init__('book', color, name)


class Bow(WorldObj):
    def __init__(self, color=None, name='bow'):
        super(Bow, self).__init__('bow', color, name)


class Bread(WorldObj):
    def __init__(self, color=None, name='bread'):
        super(Bread, self).__init__('bread', color, name)


class Broom(WorldObj):
    def __init__(self, color=None, name='broom'):
        super(Broom, self).__init__('broom', color, name)


class Bucket(WorldObj):
    def __init__(self, color=None, name='bucket'):
        super(Bucket, self).__init__('bucket', color, name, can_contain=True)


class Cake(WorldObj):
    def __init__(self, color=None, name='cake'):
        super(Cake, self).__init__('cake', color, name)


class Calculator(WorldObj):
    def __init__(self, color=None, name='calculator'):
        super(Calculator, self).__init__('calculator', color, name)


class Candy(WorldObj):
    def __init__(self, color=None, name='candy'):
        super(Candy, self).__init__('candy', color, name)


class Car(WorldObj):
    def __init__(self, color=None, name='car'):
        super(Car, self).__init__('car', color, name)


class Carton(WorldObj):
    def __init__(self, color=None, name='carton'):
        super(Carton, self).__init__('carton', color, name, can_contain=True)


class CarvingKnife(WorldObj):
    def __init__(self, color=None, name='carving_knife'):
        super(CarvingKnife, self).__init__('carving_knife', color, name)


class Casserole(WorldObj):
    def __init__(self, color=None, name='casserole'):
        super(Casserole, self).__init__('casserole', color, name)

class Chicken(WorldObj):
    def __init__(self, color=None, name='chicken'):
        super(Chicken, self).__init__('chicken', color, name)


class Chip(WorldObj):
    def __init__(self, color=None, name='chip'):
        super(Chip, self).__init__('chip', color, name)


class Cookie(WorldObj):
    def __init__(self, color=None, name='cookie'):
        super(Cookie, self).__init__('cookie', color, name)


class Date(WorldObj):
    def __init__(self, color=None, name='date'):
        super(Date, self).__init__('date', color, name)


class Door(WorldObj):
    def __init__(self, color, is_open=False, name='door'):
        self.is_open = is_open
        super().__init__('door', name=name, color=color, can_overlap=is_open, can_seebehind=is_open)
        self.block_idx = {1, 2, 3}

    def update(self, env):
        self.is_open = self.states['openable'].get_value(env)
        self.can_overlap = self.is_open
        self.can_seebehind = self.is_open

    def encode(self):
        """Encode the a description of this object as a seed 10_3-tuple of integers"""

        # State, 0: open, seed 0_2: closed, seed 0_2: locked
        if self.is_open:
            state = 0
        # elif self.is_locked:
        #     state = 2
        else:
            state = 1

        return OBJECT_TO_IDX[self.type], COLOR_TO_IDX[self.color], state

    def render(self, img):
        c = COLORS[self.color]

        if self.is_open:
            fill_coords(img, point_in_rect(0.88, 1.00, 0.00, 1.00), c)
            fill_coords(img, point_in_rect(0.92, 0.96, 0.04, 0.96), (0,0,0))
            return

        # Door frame and door
        fill_coords(img, point_in_rect(0.00, 1.00, 0.00, 1.00), c)
        fill_coords(img, point_in_rect(0.04, 0.96, 0.04, 0.96), (0,0,0))
        fill_coords(img, point_in_rect(0.08, 0.92, 0.08, 0.92), c)
        fill_coords(img, point_in_rect(0.12, 0.88, 0.12, 0.88), (0,0,0))

        # Draw door handle
        fill_coords(img, point_in_circle(cx=0.75, cy=0.50, r=0.08), c)


class Dustpan(WorldObj):
    def __init__(self, color=None, name='dustpan'):
        super(Dustpan, self).__init__('dustpan', color, name)


class Egg(WorldObj):
    def __init__(self, color=None, name='egg'):
        super(Egg, self).__init__('egg', color, name)


class Fish(WorldObj):
    def __init__(self, color=None, name='fish'):
        super(Fish, self).__init__('fish', color, name)


class Floor(WorldObj):
    """
    Colored floor tile the agent can walk over
    """
    def __init__(self, color='white'):
        super().__init__('floor', color, can_overlap=True)

    def render(self, img):
        # Give the floor a pale color
        color = COLORS[self.color] / 2
        fill_coords(img, point_in_rect(0.031, 1, 0.031, 1), color)


class Folder(WorldObj):
    def __init__(self, color=None, name='folder'):
        super(Folder, self).__init__('folder', color, name, can_contain=True)


class Fork(WorldObj):
    def __init__(self, color=None, name='fork'):
        super(Fork, self).__init__('fork', color, name)


class GymShoe(WorldObj):
    def __init__(self, color=None, name='gym_shoe'):
        super(GymShoe, self).__init__('gym_shoe', color, name)


class Hamburger(WorldObj):
    def __init__(self, color=None, name='hamburger'):
        super(Hamburger, self).__init__('hamburger', color, name)


class Hammer(WorldObj):
    def __init__(self, color=None, name='hammer'):
        super(Hammer, self).__init__('hammer', color, name)


class Highlighter(WorldObj):
    def __init__(self, color=None, name='highlighter'):
        super(Highlighter, self).__init__('highlighter', color, name)


class Jar(WorldObj):
    def __init__(self, color=None, name='jar'):
        super(Jar, self).__init__('jar', color, name, can_contain=True)


class Jewelry(WorldObj):
    def __init__(self, color=None, name='jewelry'):
        super(Jewelry, self).__init__('jewelry', color, name)

class Juice(WorldObj):
    def __init__(self, color=None, name='juice'):
        super(Juice, self).__init__('juice', color, name)


class Kettle(WorldObj):
    def __init__(self, color=None, name='kettle'):
        super(Kettle, self).__init__('kettle', color, name)


class Knife(WorldObj):
    def __init__(self, color=None, name='knife'):
        super(Knife, self).__init__('knife', color, name)


class Lemon(WorldObj):
    def __init__(self, color=None, name='lemon'):
        super(Lemon, self).__init__('lemon', color, name)


class Lettuce(WorldObj):
    def __init__(self, color=None, name='lettuce'):
        super(Lettuce, self).__init__('lettuce', color, name)


class Necklace(WorldObj):
    def __init__(self, color=None, name='necklace'):
        super(Necklace, self).__init__('necklace', color, name)


class Notebook(WorldObj):
    def __init__(self, color=None, name='notebook'):
        super(Notebook, self).__init__('notebook', color, name)


class Olive(WorldObj):
    def __init__(self, color=None, name='olive'):
        super(Olive, self).__init__('olive', color, name)


class Package(WorldObj):
    def __init__(self, color=None, name='package'):
        super(Package, self).__init__('package', color, name, can_contain=True)


class Pan(WorldObj):
    def __init__(self, color=None, name='pan'):
        super(Pan, self).__init__('pan', color, name)


class Pen(WorldObj):
    def __init__(self, color=None, name='pen'):
        super(Pen, self).__init__('pen', color, name)


class Pencil(WorldObj):
    def __init__(self, color=None, name='pencil'):
        super(Pencil, self).__init__('pencil', color, name)


class Plate(WorldObj):
    def __init__(self, color=None, name='plate'):
        super(Plate, self).__init__('plate', color, name)


class Plywood(WorldObj):
    def __init__(self, color=None, name='plywood'):
        super(Plywood, self).__init__('plywood', color, name)


class Pop(WorldObj):
    def __init__(self, color=None, name='pop'):
        super(Pop, self).__init__('pop', color, name)


class Printer(WorldObj):
    def __init__(self, color=None, name='printer'):
        super(Printer, self).__init__('printer', color, name)


class Radish(WorldObj):
    def __init__(self, color=None, name='radish'):
        super(Radish, self).__init__('radish', color, name)


class Rag(WorldObj):
    def __init__(self, color=None, name='rag'):
        super(Rag, self).__init__('rag', color, name)


class Salad(WorldObj):
    def __init__(self, color=None, name='salad'):
        super(Salad, self).__init__('salad', color, name)


class Sandwich(WorldObj):
    def __init__(self, color=None, name='sandwich'):
        super(Sandwich, self).__init__('sandwich', color, name)


class Saw(WorldObj):
    def __init__(self, color=None, name='saw'):
        super(Saw, self).__init__('saw', color, name)

class ScrubBrush(WorldObj):
    def __init__(self, color=None, name='scrub_brush'):
        super(ScrubBrush, self).__init__('scrub_brush', color, name)


class Shoe(WorldObj):
    def __init__(self, color=None, name='shoe'):
        super(Shoe, self).__init__('shoe', color, name)


class Soap(WorldObj):
    def __init__(self, color=None, name='soap'):
        super(Soap, self).__init__('soap', color, name)


class Sock(WorldObj):
    def __init__(self, color=None, name='sock'):
        super(Sock, self).__init__('sock', color, name)


class Soup(WorldObj):
    def __init__(self, color=None, name='soup'):
        super(Soup, self).__init__('soup', color, name)


class Spoon(WorldObj):
    def __init__(self, color=None, name='spoon'):
        super(Spoon, self).__init__('spoon', color, name)


class Strawberry(WorldObj):
    def __init__(self, color=None, name='strawberry'):
        super(Strawberry, self).__init__('strawberry', color, name)


class TeaBag(WorldObj):
    def __init__(self, color=None, name='tea_bag'):
        super(TeaBag, self).__init__('tea_bag', color, name)


class Teapot(WorldObj):
    def __init__(self, color=None, name='teapot'):
        super(Teapot, self).__init__('teapot', color, name, can_contain=True)


class Toilet(WorldObj):
    def __init__(self, color=None, name='toilet'):
        super(Toilet, self).__init__('toilet', color, name)
        self.block_idx = {2, 3}


class Tomato(WorldObj):
    def __init__(self, color=None, name='tomato'):
        super(Tomato, self).__init__('tomato', color, name)


class Towel(WorldObj):
    def __init__(self, color=None, name='towel'):
        super(Towel, self).__init__('towel', color, name)


class VegetableOil(WorldObj):
    def __init__(self, color=None, name='vegetable_oil'):
        super(VegetableOil, self).__init__('vegetable_oil', color, name)


# TODO: add wall to object properties
class Wall(WorldObj):
    def __init__(self, color='grey'):
        super().__init__('wall', color=color, can_seebehind=False)
        self.height = 1
        self.width = 1
        self.valid_idx = [0]
        self.block_idx = {1, 2, 3}

    def render(self, img):
        fill_coords(img, point_in_rect(0, 1, 0, 1), COLORS['grey'])


class Water(WorldObj):
    def __init__(self, color=None, name='water'):
        super(Water, self).__init__('water', color, name)


class Window(WorldObj):
    def __init__(self, color=None, name='window'):
        super(Window, self).__init__('window', color, name)


#######################################################################################################################


class Bed(FurnitureObj):
    def __init__(self, width=3, height=2, color='purple', name='bed'):
        super(Bed, self).__init__('bed', width, height, color, name, can_overlap=True)
        self.block_idx = {2, 3}


class Cabinet(FurnitureObj):
    def __init__(self, width=2, height=3, color='brown', name='cabinet'):
        super(Cabinet, self).__init__('cabinet', width, height, color, name, can_contain=True, can_seebehind=False)
        self.block_idx ={3}


class Countertop(FurnitureObj):
    def __init__(self, width=3, height=2, color='tan', name='countertop'):
        super(Countertop, self).__init__('countertop', width, height, color, name, can_seebehind=True)
        self.block_idx = {2, 3}


class ElectricRefrigerator(FurnitureObj):
    def __init__(self, width=2, height=3, color='l_blue', name='electric_refrigerator'):
        super(ElectricRefrigerator, self).__init__('electric_refrigerator', width, height, color, name, can_contain=True, can_seebehind=False)
        self.block_idx = {3}


class Shelf(FurnitureObj):
    def __init__(self, width=2, height=3, color='brown', name='shelf'):
        super(Shelf, self).__init__('shelf', width, height, color, name, can_contain=True, can_seebehind=False)
        self.block_idx = {2, 3}


class Shower(FurnitureObj):
    def __init__(self, width=3, height=2, color='l_blue', name='shower'):
        super(Shower, self).__init__('shower', width, height, color, name)
        self.block_idx = {2, 3}


class Sink(FurnitureObj):
    def __init__(self, width=2, height=2, color='blue', name='sink'):
        super(Sink, self).__init__('sink', width, height, color, name, can_overlap=False, can_seebehind=True)
        self.block_idx = {2, 3}


class Sofa(FurnitureObj):
    def __init__(self, width=3, height=2, color='red', name='sofa'):
        super(Sofa, self).__init__('sofa', width=width, height=height, color=color, name=name)
        self.block_idx = {2, 3}


class Stove(FurnitureObj):
    def __init__(self, width=3, height=2, color='grey', name='stove'):
        super(Stove, self).__init__('stove', width, height, color, name)
        self.block_idx = {2, 3}


class Table(FurnitureObj):
    def __init__(self, width=3, height=2, color='tan', name='table'):
        super(Table, self).__init__('table', width, height, color, name)
        self.block_idx = {2, 3}


OBJECT_CLASS = {
    "apple": Apple,
    "ashcan": Ashcan,
    "backpack": Backpack,
    "ball": Ball,
    "banana": Banana,
    "basket": Basket,
    "bed": Bed,
    "beef": Beef,
    "bin": Bin,
    "blender": Blender,
    "book": Book,
    "bow": Bow,
    "bread": Bread,
    "broom": Broom,
    "bucket": Bucket,
    "cabinet": Cabinet,
    "cake": Cake,
    "calculator": Calculator,
    "candy": Candy,
    "car": Car,
    "carton": Carton,
    "carving_knife": CarvingKnife,
    "casserole": Casserole,
    "chicken": Chicken,
    "chip": Chip,
    "cookie": Cookie,
    "countertop": Countertop,
    "date": Date,
    "door": Door,
    "dustpan": Dustpan,
    "egg": Egg,
    "electric_refrigerator": ElectricRefrigerator,
    "fish": Fish,
    "floor": Floor,
    "folder": Folder,
    "fork": Fork,
    "gym_shoe": GymShoe,
    "hamburger": Hamburger,
    "hammer": Hammer,
    "highlighter": Highlighter,
    "jar": Jar,
    "jewelry": Jewelry,
    "juice": Juice,
    "kettle": Kettle,
    "knife": Knife,
    "lemon": Lemon,
    "lettuce": Lettuce,
    "necklace": Necklace,
    "notebook": Notebook,
    "olive": Olive,
    "package": Package,
    "pan": Pan,
    "pen": Pen,
    "pencil": Pencil,
    "plate": Plate,
    "plywood": Plywood,
    "pop": Pop,
    "printer": Printer,
    "radish": Radish,
    "rag": Rag,
    "salad": Salad,
    "sandwich": Sandwich,
    "saw": Saw,
    "scrub_brush": ScrubBrush,
    "shelf": Shelf,
    "shoe": Shoe,
    "shower": Shower,
    "sink": Sink,
    "soap": Soap,
    "sock": Sock,
    "sofa": Sofa,
    "soup": Soup,
    "spoon": Spoon,
    "stove": Stove,
    "strawberry": Strawberry,
    "table": Table,
    "tea_bag": TeaBag,
    "teapot": Teapot,
    "toilet": Toilet,
    "tomato": Tomato,
    "towel": Towel,
    "vegetable_oil": VegetableOil,
    "wall": Wall,
    "water": Water,
    "window ": Window,
}
