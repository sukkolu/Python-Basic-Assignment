1. RGBA stands for Red, Green, Blue, Alpha. It is a color model that represents colors as a combination of red, green, blue, and alpha (transparency) values.

2. To get the RGBA value of an image using the Pillow module, you can use the `getpixel()` method on the `Image` object. For example, `image.getpixel((x, y))` will return a 4-tuple containing the red, green, blue, and alpha values for the pixel at coordinates (x, y).

3. A box tuple is a 4-tuple of (left, top, right, bottom) coordinates that represents a rectangular region. This is commonly used in Pillow to specify the area of an image to work with, such as for cropping or resizing.

4. To find the width and height of an `Image` object, you can access the `width` and `height` attributes. For example, `image.width` and `image.height` will give you the dimensions of the image.

5. To get an `Image` object for a 100x100 image, excluding the lower-left quarter, you can use the `crop()` method. For example, `image.crop((0, 25, 100, 100))` will create a new `Image` object that is 100x75 pixels, excluding the lower-left 50x25 pixel region.

6. To save an `Image` object as an image file, you can use the `save()` method. For example, `image.save('output.png')` will save the image as a PNG file.

7. The `ImageDraw` module in Pillow contains the shape-drawing code, such as for drawing lines, rectangles, and other shapes on an image.

8. The `ImageDraw` module provides a `Draw` object that has drawing methods, such as `line()`, `rectangle()`, and `text()`. You can create a `Draw` object from an `Image` object using the `ImageDraw.Draw()` function, like this: `draw = ImageDraw.Draw(image)`.