import json
import logging
import random
from contextlib import contextmanager,closing
"""
1.输出型
2.远程型
3.防御型
"""
#------------------------function------------------------
def initLog():
    logger = logging.getLogger('System')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
logger = initLog()
def write_json(Path:str,data):
    with open(f"./DataBase/{Path}.json", 'w') as f:
        json.dump(data, f)
    return True
def read_json(Path:str):
    try:
        with open(f"./DataBase/{Path}.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def find_id_index(Path:str,type:str,target_id:int):
        with open(f'./DataBase/{Path}.json', 'r', encoding='utf-8') as f:
            Context = json.load(f)
            for index, item in enumerate(Context):
                if item.get(type) == target_id:
                    return index,Context
            return -1
#------------------------function------------------------
#------------------------Monster_cfg------------------------

def apply_buffs(func):
    def wrapper(self, *args, **kwargs):
        # 先执行原始的 Base_init 方法
        result = func(self, *args, **kwargs)
        # 检查并应用所有 buff
        IdIndex, Context = find_id_index("weapon","id",self.WeaponId)
        buffs = Context[IdIndex].get("Buff", {})
        if "HP_Buff" in buffs:
            self.HP *= buffs["HP_Buff"]
        if "Defense_Buff" in buffs:
            self.defense *= buffs["Defense_Buff"]
        if "Attack_Buff" in buffs:
            self.attack *= buffs["Attack_Buff"]
        #添加其他.
        return float(self.HP)
    return wrapper
def apply_Base(func):
    def wrapper(self, *args, **kwargs):
        if 0< self.lv <=10:
            self.HP += 10
            self.defense += 5
            self.attack +=1
        elif 10< self.lv <=19:
            self.HP += 20
            self.attack +=3
            self.defense += 10
        elif 19< self.lv <=29:
            self.HP += 30
            self.defense += 15
            self.attack +=4
        elif 29< self.lv <=39:
            self.HP += 40
            self.defense += 20
            self.attack +=5
        elif 39< self.lv <=49:
            self.HP += 50
            self.defense += 25
            self.attack +=6
        elif 49< self.lv <=59:
            self.HP += 60
            self.defense += 30
            self.attack +=7
        elif 59< self.lv <=69:
            self.HP += 70
            self.defense += 35
            self.attack +=8
        elif 69< self.lv <=79:
            self.HP += 80
            self.defense += 40
            self.attack +=9
        elif 79< self.lv <=89:
            self.HP += 90
            self.defense += 45
            self.attack +=10
        elif 89< self.lv <=100:
            self.HP += 100
            self.defense += 50
            self.attack +=11
        else:
            logger.error("not found：",self.lv)
        return func(self, *args, **kwargs)
    return wrapper
def apply_Drop(func):
    def wrapper(self, *args, **kwargs):
        if 0< self.lv <=10:
            Drop = random.choice([1,2])
        elif 10< self.lv <=19:
            Drop = random.choice([1,3])
        elif 19< self.lv <=29:
            Drop = random.choice([1,4])
        elif 29< self.lv <=39:
            Drop = random.choice([1,5])
        elif 39< self.lv <=49:
            Drop = random.choice([1,6])
        elif 49< self.lv <=59:
            Drop = random.choice([1,7])
        elif 59< self.lv <=69:
            Drop = random.choice([1,8])
        elif 69< self.lv <=79:
            Drop = random.choice([1,9])
        elif 79< self.lv <=89:
            Drop = random.choice([1,10])
        elif 89< self.lv <=100:
            Drop = random.choice([1,11])
        else:
            logger.error("Drop_Lv not found：",self.lv)
            Drop = 0
        self.Drop = Drop
        return func(self, *args, **kwargs)
    return wrapper
#------------------------Monster_cfg------------------------








#------------------------main------------------------
class Monster(object):
    def __init__(self,ID:int,name:str = "null",attack:float = 1,lv:int = 1,HP:float = 1,defense:float = 1,WeaponId:int = 1):
        self.ID = ID#填掉落的物品id就好。
        self.name = name
        self.attack = attack
        self.lv = lv
        self.HP = HP
        self.defense = defense
        self.WeaponId = WeaponId
    @apply_buffs
    @apply_buffs
    def Base_init(self)-> tuple[float, float, float]:
        self.HP = self.HP + self.defense / 2.5
        return float(self.HP),float(self.defense),float(self.attack)
    @apply_Drop
    def Drop_Item(self):
        ItemId,Value = find_id_index("item","id",self.ID)
        Drop_Name = Value[ItemId].get("name", default=None)
        print(f"掉落：{Drop_Name} x{self.Drop}")
        Drop_Total = {}
        Drop_Total[ItemId] = Value
        return Drop_Total


    def A(self):
        return self.attack
class Sword_Monster(Monster):
    def __init__(self, ID: int, name: str = "null", attack: float = 1, lv: int = 1, HP: float = 1, defense: float = 1, WeaponId: int = None):
        super().__init__(ID, name, attack, lv, HP, defense, WeaponId)
    def E(self) ->float:
        return random.choice([self.attack,self.attack*2])
    def Q(self) ->float:
        self.HP *= 0.5
        self.defense *= 0.5
        return random.choice([self.attack,self.attack*2])
