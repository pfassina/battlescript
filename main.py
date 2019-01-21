
class Army:

    def __init__(self, nation):
        self.nation = nation
        self.province = None
        self.commanders = []

    def set_province(self, province):
        self.province = province

    def add_commanders(self, commanders):
        for commander in commanders:
            self.commanders.append(commander)

    def get_blurb(self):

        blurb = '\n\n#allowedplayer {0}'.format(str(self.nation))
        blurb += '\n#specstart {0} {1}'.format(str(self.nation), str(self.province))
        blurb += '\n#setland {0}'.format(str(self.province))
        for commander in self.commanders:
            blurb += commander.get_blurb()

        return blurb


class Commander:

    def __init__(self, commander_id):
        self.id = commander_id
        self.paths = []
        self.units = []

    def add_path(self, path, level):
        self.paths.append({'path': path, 'level': level})

    def add_unit(self, unit_id, quantity):
        self.units.append({'id': unit_id, 'quantity': quantity})

    def get_blurb(self):

        blurb = '\n\n#commander {0}'.format(str(self.id))

        if self.paths:
            blurb += '\n#clearmagic'
            for path in self.paths:

                path_name, path_level = path['path'], str(path['level'])
                blurb += '\n#mag_{0} {1}'.format(path_name, path_level)

        for unit in self.units:
            unit_id, unit_qty = str(unit['id']), str(unit['quantity'])
            blurb += '\n#units {0} {1}'.format(unit_qty, unit_id)

        return blurb


def parse_path(path):

    path_id, level = path
    path_dict = {
        'F': 'fire',
        'A': 'air',
        'W': 'water',
        'E': 'earth',
        'S': 'astral',
        'D': 'death',
        'N': 'nature',
        'B': 'blood',
        'H': 'priest'
    }

    return path_dict[path_id], level


def create_army(nation, province, commanders):

    army = Army(nation)
    army.set_province(province)

    cmdr_list = []
    for c in commanders:
        commander_id, paths, units = c
        cmdr = Commander(commander_id)
        if paths:
            for path in paths:
                path_name, level = parse_path(path)
                cmdr.add_path(path=path_name, level=level)
        if units:
            for unit in units:
                unit_id, quantity = unit
                cmdr.add_unit(unit_id=unit_id, quantity=quantity)
        cmdr_list.append(cmdr)

    army.add_commanders(cmdr_list)
    blurb = army.get_blurb()

    return blurb


def generate_blurb(armies):
    blurb = ''
    for army in armies:
        n = army['id']
        p = army['province']
        c = army['commanders']
        blurb += create_army(nation=n, province=p, commanders=c)

    return blurb


def create_map_file(blurb):

    with open('template.txt', 'r') as template:
        blurb = template.read() + blurb

    with open('Arena.map', 'w') as map_file:
        map_file.write(blurb)

    return print('Success!')
