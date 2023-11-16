
init python:
    class Item:
        def __init__(self, name, cost, imageref):
            self.name = name
            self.cost = cost
            self.command = False
            self.receive = False
            self.imageref = imageref

    class Inventory:
        def __init__(self):
            self.items = []
        
        
        def buy(self, item):
            global money
            global shop
            if money >= item.cost:
                money -= item.cost
                item.command = True
                renpy.jump("buyitem")
            else:
                renpy.jump("toopoor")
        
        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False
        def get_item(self, item):
            item.receive = False
            self.items.append(item)
    def addvar():
        if 'inventory' not in globals():
            globals()["inventory"] = Inventory()
        
        if 'Gymclothes' not in globals():
            globals()["Gymclothes"] = Item("Bộ đồ tập Gym", 20,"")
        
        Gymclothes.imageref = "ui/itemshopgymclothes.webp"  
        
        if 'Tsounade' not in globals():
            globals()["Tsounade"] = Item("Bộ đồ Cosplay của Tsounade", 50,"")
        
        Tsounade.imageref = "ui/itemtsounade.webp"   
        
        if 'Swimwear' not in globals():
            globals()["Swimwear"] = Item("Bộ đồ bơi", 30,"")
        
        Swimwear.imageref = "0.1.7/swimwearthumbnail.webp"   
        
        if 'Toolkit' not in globals():
            globals()["Toolkit"] = Item("Bộ công cụ", 40,"")
        
        Toolkit.imageref = "ui/Toolkit.webp"
        
        globals()["shop"] = [Gymclothes, Tsounade, Swimwear, Toolkit]

define tsounaderef = "ui/itemtsounade.webp"
define gymclothesref = "ui/itemshopgymclothes.webp"






define inventtest = [Item("Bộ đồ tập Gym", 0,"ui/itemshopbg.webp"),
    Item("Bộ đồ tập Gym 2", 0,"ui/itemshopbg.webp"),
    Item("Bộ đồ tập Gym 3", 0,"ui/itemshopbg.webp"),
    Item("Bộ đồ tập Gym 4", 0,"ui/itemshopbg.webp")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
