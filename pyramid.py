
my_star = "*"

#star_pyramid = my_star

#print(star_pyramid) 

def build_pyramid(height):
    for i in range(height):
        print((" " * (height - 1 - i)), ("*" * (2 * i + 1)))

build_pyramid(9)

