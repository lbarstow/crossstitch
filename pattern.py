from PIL import Image
import numpy
myimg = Image.open('flowercopy.jpg')
avg_color_per_row = numpy.average(myimg, axis=0)
avg_color = numpy.average(avg_color_per_row, axis=0)
print(avg_color)
