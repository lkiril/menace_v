from collections import namedtuple

from PIL import Image, ImageDraw, ImageFont


CELL_SIZE = 30
TEXT_OFFSET = CELL_SIZE
BEAD_SIZE = 20
MARK_SIZE = 16
MARGIN_SIZE = 4

BOARD_SIZE = (
    CELL_SIZE*3 + MARGIN_SIZE*2,
    CELL_SIZE*3 + TEXT_OFFSET + MARGIN_SIZE*2
)


def frame(draw):
    draw.line((CELL_SIZE + MARGIN_SIZE, TEXT_OFFSET + MARGIN_SIZE, CELL_SIZE + MARGIN_SIZE, CELL_SIZE*3 + TEXT_OFFSET + MARGIN_SIZE), fill=(0, 0, 0))
    draw.line((CELL_SIZE*2 + MARGIN_SIZE, TEXT_OFFSET + MARGIN_SIZE, CELL_SIZE*2 + MARGIN_SIZE, CELL_SIZE*3 + TEXT_OFFSET + MARGIN_SIZE), fill=(0, 0, 0))
    draw.line((0 + MARGIN_SIZE, CELL_SIZE + TEXT_OFFSET + MARGIN_SIZE, CELL_SIZE*3 + MARGIN_SIZE, CELL_SIZE + TEXT_OFFSET + MARGIN_SIZE), fill=(0, 0, 0))
    draw.line((0 + MARGIN_SIZE, CELL_SIZE*2 + TEXT_OFFSET + MARGIN_SIZE, CELL_SIZE*3 + MARGIN_SIZE, CELL_SIZE*2 + TEXT_OFFSET + MARGIN_SIZE), fill=(0, 0, 0))
    draw.line((0, 0, 0, BOARD_SIZE[1]-1), fill=(0xd3, 0xd3, 0xd3))
    draw.line((0, BOARD_SIZE[1]-1, BOARD_SIZE[0]-1, BOARD_SIZE[1]-1), fill=(0xd3, 0xd3, 0xd3))
    draw.line((BOARD_SIZE[0]-1, BOARD_SIZE[1]-1, BOARD_SIZE[0]-1, 0), fill=(0xd3, 0xd3, 0xd3))
    draw.line((BOARD_SIZE[0]-1, 0, 0, 0), fill=(0xd3, 0xd3, 0xd3))


colors = {
    0: (0xff, 0xb6, 0xc1),
    1: (0xff, 0xff, 0x00),
    2: (0x00, 0x00, 0x00),
    3: (0x55, 0x1a, 0x8b),
    4: (0xd3, 0xd3, 0xd3),
    5: (0x00, 0xff, 0x00),
    6: (0xff, 0x00, 0x00),
    7: (0x40, 0xe0, 0xd0),
    8: (0xff, 0xff, 0xff),
}


def bead(draw, cell):
    x = cell % 3
    y = cell / 3
    bead_position = (
                            CELL_SIZE * x + (CELL_SIZE - BEAD_SIZE) / 2 + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - BEAD_SIZE) / 2 + TEXT_OFFSET + MARGIN_SIZE,
                            CELL_SIZE * x + (CELL_SIZE - BEAD_SIZE) / 2 + BEAD_SIZE + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - BEAD_SIZE) / 2 + BEAD_SIZE + TEXT_OFFSET + MARGIN_SIZE
    )
    fill = colors[cell]
    outline = tuple([element/2 for element in fill])
    draw.ellipse(bead_position, fill=fill, outline=outline)


def mark_x(draw, cell):
    x = cell % 3
    y = cell / 3
    line1 = (
                            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + TEXT_OFFSET + MARGIN_SIZE,
                            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE + TEXT_OFFSET + MARGIN_SIZE
    )
    line2 = (
                            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE + TEXT_OFFSET + MARGIN_SIZE,
                            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE + MARGIN_SIZE,
                            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + TEXT_OFFSET + MARGIN_SIZE
    )
    draw.line(line1, fill="black", width=5)
    draw.line(line2, fill="black", width=5)


def mark_o(draw, cell):
    x = cell % 3
    y = cell / 3
    for i in xrange(-1, 3):
        position = (
            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + i + MARGIN_SIZE,
            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + i + TEXT_OFFSET + MARGIN_SIZE,
            CELL_SIZE * x + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE - i + MARGIN_SIZE,
            CELL_SIZE * y + (CELL_SIZE - MARK_SIZE) / 2 + MARK_SIZE - i + TEXT_OFFSET + MARGIN_SIZE
        )
        draw.ellipse(position, outline="black")


def create_stickers():
    data = "ccccccccc01ccccccc0ccc1cccc0cccc1ccc10cccccccc0cc1cccc1c0ccccccc1c0ccccc1ccc0ccccc1cc0cccc1cccc0cccc1ccccc0c1ccccccc000cc11ccc00cc1cc1c00ccc1c1c0101ccccc010c1cccc100c1cccc100cc1ccc100ccc1cc010cccc1c0c0c1cc1c100cccc1c100ccccc11100ccccc1010ccccc01c01cccc10c01cccc01c0c1ccc10c0c1ccc01c0ccc1c10c0cccc1110c0cccc11c00cccc101c0cccc01c10cccc01cc01ccc10cc01ccc1c0c01ccc10cc0c1cc01cc0cc1c0ccc01c1c10cc0cc1c1c0c0cc1cc1c00cc1c10cc0ccc11c0c0ccc1110cc0ccc11c0c0ccc11cc00ccc01c1c0cccc1c100ccc01cc10ccc10cc10ccc1c0c10cccc1c010ccc10ccc01cc01ccc0c1c10ccc0c1c1c0cc0c1cc1c0c0c1c10ccc0cc1110ccc0cc11c0cc0cc11cc0c0cc11ccc00cc101ccc0cc1c1c0c0cc01cc1c0cc10cc1c0cc1c0c1c0cc01ccc10cc10ccc10cc1c0cc10cc01cccc01c10cccc01c10cccc0c11c0ccc0c1110cccc0c11c0ccc0c11cc0cc0c11ccc0c0c11cccc00c101cccc0c1c1c0cc0c1c1ccc00cc1c1c0c0c01cc1cc0c10cc1cc0c1c0c1cc0cc1c01cc0c1ccc10c0c01ccc1c0c0ccc11c0c10ccc1c0c1c0cc1c0c1ccc01c0c10cccc10c10ccccc01110ccccc011c0cccc011cc0ccc011ccc0cc011cccc0c011ccccc001c1ccc0c001c1cccc001cc1ccc010cc1ccc01c0c1ccc01ccc10cc001ccc1cc010ccc1cc01c0cc1cc01ccc01cc01cccc1c0010cccc1c001ccccc1010ccccc101c0cccc10100011ccc00c011c1c10001cc1c1000c1c1c010101ccc110001ccc100c011cc11000c1cc10100c1cc01010cc1c100c01c1c11000cc1c10100cc1c01c001c1c10c001c1c100c0c1c111000ccc110100ccc1110100ccc010110ccc110010ccc101010ccc100c101cc1100c01cc1010c01cc110c001cc0101c0c1c100c10c1c1100c0c1c1010c0c1c110c00c1c100cc01c11100c0cc1110c00cc110cc001c11101c00cc01011c0cc11001c0cc10101c0cc110c100cc11c0100cc0101c10cc100c110cc1100c10cc11c0010cc100c1c01c100cc101c1100cc01c1010cc01c11c00c01c101c0c01c01cc0101c10cc0101c110cc001c11c0c001c11cc0001c10cc1001c1100cc0c11010cc0c111c00c0c1110cc00c111c0c00c111cc000c111010cc0c1101c0c0c11c100c0c01011cc0c11001cc0c10101cc0c110c10c0c11c010c0c01c110c0c110c1c00c11c01c00c11cc1000c101c1c00c0101c1c0c100c11c0c1100c1c0c01c011c0c10c011c0c110c01c0c11c001c0c01c101c0c110cc100c11c0c100c11cc0100c01cc1100c10cc1100c1c0c1100c100c1c10c100cc110c1100cc10c110c0c10c11c00c10c110cc010c11c0c010c11cc0010c10cc1010c1100ccc011010ccc01110c0cc0111c00cc01110cc0c0111c0c0c0111cc00c01110ccc00111c0cc00111cc0c00111ccc000111010ccc011c100cc01101cc0c01101ccc0011c1c0c0001011ccc011001ccc010101ccc011c010cc001c110cc0110c1c0c011c01c0c011cc100c0101c1c0c0110c1cc0011c01cc0011cc10c00100c11cc01100c1cc001c011cc010c011cc0110c01cc011c001cc0110cc10c011c0c10c011cc010c001cc110c010cc110c01c0c110c0110cc1c0011c0c1c0011cc01c0001c1c1c0010cc11c001c0c11c00100c1c1c0100cc11c01100cc1c01010cc1c0110c0c1c011c00c1c0101c0c1c010cc011c011c0c01c011cc001c010cc101c0110ccc10011c0cc10011cc0c10011ccc0100101ccc1000101ccc10100c1cc10100cc1c101100ccc101010ccc1010c0c1c10110c0cc1011c00cc1010cc01c101c0c01c1011c0c0c1011cc00c1010cc10c10110ccc01011c0cc01011cc0c01011ccc0010101ccc0101c1c0c01010cc1c01010ccc10101c0cc1010"
    paths = []
    for b in xrange(len(data)/9):
        board = Image.new("RGB", BOARD_SIZE, (255, 255, 255))
        draw = ImageDraw.Draw(board)
        frame(draw)
        for cell in xrange(9):
            idx = b * 9 + cell
            if data[idx] == "c":
                bead(draw, cell)
            elif data[idx] == "1":
                mark_o(draw, cell)
            elif data[idx] == "0":
                mark_x(draw, cell)
        text = str(b)
        font = ImageFont.truetype(font="/Applications/Microsoft Word.app/Contents/Resources/DFonts/arial.ttf", size=TEXT_OFFSET-MARGIN_SIZE)
        text_size = draw.textsize(text, font)
        text_position = (
            MARGIN_SIZE + (CELL_SIZE*3 - text_size[0])/2,
            MARGIN_SIZE
        )
        draw.text(text_position, text, fill="black", font=font)
        path = "board_stickers/{0:03}.png".format(b)
        board.save(path)
        paths.append(path)
    return paths


def create_pages(cols, rows, paths):
    page_size = (BOARD_SIZE[0]*cols, BOARD_SIZE[1]*rows)
    page = Image.new("RGB", page_size, (255, 255, 255))
    stickers = 0
    for i, path in enumerate(paths):
        if stickers == cols * rows:
            page.save("board_stickers/page_{0}.png".format(i))
            stickers = 0
            page = Image.new("RGB", page_size, (255, 255, 255))
        x = (stickers % cols) * BOARD_SIZE[0]
        y = (stickers / cols) * BOARD_SIZE[1]
        with open(path, "rb") as f:
            img = Image.open(f)
            page.paste(img, (x, y))
        stickers += 1
    if stickers > 0:
        page.save("board_stickers/page_{0}.png".format(i))





if __name__ == '__main__':
    paths = create_stickers()
    create_pages(6, 6, paths)
