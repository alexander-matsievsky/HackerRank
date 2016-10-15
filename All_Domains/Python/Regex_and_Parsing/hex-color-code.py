import re
import sys

css = re.sub(r'(?<=[{}:;,])\s+|\s+(?=[{}:;,])', '', ''.join(sys.stdin))
hex_colors = (
    hex_color.group(0)
    for value in re.finditer(r'(?<=:)(.*?)(?=;)', css)
    for hex_color in re.finditer(r'#[a-f\d]{6}|#[a-f\d]{3}', value.group(0), re.I)
)
print(sep='\n', *hex_colors)
