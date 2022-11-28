"""
Flyweight pattern example.
"""
class Pixel:

    def __init__(self, rgb_code):
        self.rgb_code = rgb_code
        self.values = {
            "red": int(self.rgb_code[1:3], base=16),
            "green": int(self.rgb_code[3:5], base=16),
            "blue": int(self.rgb_code[5:7], base=16)
        }


class Image:

    def __init__(self, array):
        self.height = len(array)
        self.width = len(array[0])
        self.palette = {}
        self.pixel_array = self.compress(array)

    def compress(self, array):
        return [[self.add_pixel(array[y][x])
                for x in range(self.width)]
                for y in range(self.height)]


    def add_pixel(self, code):
        if not code in self.palette:
            self.palette[code] = Pixel(code)
        return self.palette[code]

    def __str__(self):
        msg = "Image of size {}x{} with {} unique pixels."
        return msg.format(
            self.height, self.width, len(self.palette.keys()))

    def get_values(self, channel="red"):
        return [[self.pixel_array[y][x].values[channel]
                for x in range(self.width)]
                for y in range(self.height)]



data = (
    ("#ff00ee", "#1345ab", "#ff00ee"),
    ("#ef001e", "#ff00ee", "#ff01ab"),
    ("#ff00ee", "#1345ab", "#ff00ee"),
    ("#ff00ee", "#1345ab", "#ff00ee"),
)

img = Image(data)
print(img)
print(img.get_values(channel="red"))
