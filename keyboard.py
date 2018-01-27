class Key:
    char = ""
    links = []
    line_nr = -1
    left_boundary = False
    right_boundary = False

    def __init__(self, char, line_nr, left_boundary=False, right_bounary=False):
        self.char = char
        self.line_nr = line_nr
        self.left_boundary = left_boundary
        self.right_boundary = right_bounary
        self.links = []

    def __str__(self):
        out = "<{}> line {}, rel: {}".format(self.char, self.line_nr, "".join(self.links))
        if self.left_boundary:
            return out + " left"
        elif self.right_boundary:
            return out + " right"
        return out

    def __repr__(self):
        return self.__str__()


class Keyboard:
    keys = []
    lines = [
        "1234567890-",
        "qwertyiuop[",
        "asdfghkjl;'",
        "zxcvbn,m./\\"
    ]

    def _build_keymap(self):
        for line_nr, line in enumerate(self.lines):
            for key_nr, key in enumerate(line):
                if key_nr == 0:
                    k = Key(key, line_nr, left_boundary=True)
                    k.links.append(self.lines[line_nr][key_nr + 1])

                elif key_nr == len(line) - 1:
                    k = Key(key, line_nr, right_bounary=True)
                    k.links.append(self.lines[line_nr][key_nr - 1])
                else:
                    k = Key(key, line_nr)
                    k.links.append(self.lines[line_nr][key_nr + 1])
                    k.links.append(self.lines[line_nr][key_nr - 1])

                # add relation (neighbour) for upper/lower line
                if line_nr == 0:
                    k.links.append(self.lines[line_nr + 1][key_nr])
                elif line_nr == 3:
                    k.links.append(self.lines[line_nr - 1][key_nr])
                else:
                    k.links.append(self.lines[line_nr + 1][key_nr])
                    k.links.append(self.lines[line_nr - 1][key_nr])

                self.keys.append(k)

    def __getitem__(self, item):
        for k in self.keys:
            if k.char == item:
                return k
        raise KeyError

    def __init__(self):
        self._build_keymap()
