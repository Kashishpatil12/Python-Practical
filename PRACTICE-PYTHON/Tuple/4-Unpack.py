
# Unpacking a Tuple

flowers = ("rose","lotus","marigold")
(red, pink, yellow) = flowers
print(red)
print(pink)
print(yellow)
print("______________________________________________________")
# Using Asterisk*
flowers = ("rose","lotus","Lily","marigold")
(red,*pink,yellow) = flowers
print(red)
print(pink)
print(yellow)
print("______________________________________________________")
