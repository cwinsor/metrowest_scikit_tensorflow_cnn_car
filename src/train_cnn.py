import numpy as np
from sklearn.datasets import load_sample_images

# Load sample images
china = load_sample_image("china.jpg")
flower = load_sample_image("flower.jpg")
dataset = np.array([china,flower] dtype=np.float32)
batch_size, height, width, channels = dataset.shape

# Create 2 filters
Filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)
filters[:, 3, :, 0] = 1  # vertical line
filters[3, :, :, 1] = 1  # horizontal line

# Create a graph with input X plus a convolutional layer applying the 2 filters
x = tf.placeholder(tf.float32, shape=(None, height, width, channels))
convolution = tf.nn.conv2d(x, filters, strides=[1,2,2,1], padding='SAME')

with tf.Session() as sess:
	output = sess.run(convolution, feed_dist=[x: dataset])

	plt.imshow(output[8, :, :, 1], cmap='gray')  # plot 1st image's second feature map
	plt.show()


