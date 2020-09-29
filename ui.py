import palette
import opener

address=opener.open_file()
destination=opener.save_file()
origin = palette.get_img(address)
img = palette.resize(origin)
empty = palette.empty_palette(origin)
colors = palette.get_colors(img)
empty=palette.save_palette(empty,colors[0],colors[1],colors[2],colors[3],colors[4])
final = palette.img_final(origin,empty)
palette.save_final(final,destination)