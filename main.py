import imageio.v3 as iio

filenames = ['photo1.jpg', 'photo2.jpg']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('result.gif', images, duration = 500, loop = 0)