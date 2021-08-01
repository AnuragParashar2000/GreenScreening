
from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6


def redscreen(main_filename, back_filename):
    """
    Implements the notion of "redscreening".  That is,
    the image in the main_filename has its "sufficiently red"
    pixels replaced with pixel from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "redscreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    back.make_as_big_as(image)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in
            # the main image with that from the back image.
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image


def main():
    image = SimpleImage("firetruck2.jpg")
    back = SimpleImage("fire.jpg")
    original_stop = SimpleImage("firetruck2.jpg")
    original_stop.show()

    original_leaves = SimpleImage("fire.jpg")
    original_leaves.show()

    #a = image.width
    #b = back.width
    # print(a, b)
    stop_leaves_replaced = redscreen("firetruck2.jpg", "fire.jpg")
    stop_leaves_replaced.show()
    #print(a,b)

if __name__ == '__main__':
    main()
