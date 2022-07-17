class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area


    def __str__(self):
        return "[%s] takes up %.2f " % (self.name, self.area)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "type: %s\ntotal area: %.2f[free %.2f]\n" \
               "item: %s" % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        if item.area > self.free_area:
            print("not enough!")
            return

        self.item_list.append(item.name)
        self.free_area -= item.area


house = House("type_one", 156.5)
print(house)

house.add_item(HouseItem("desk", 5.5))
print(house)