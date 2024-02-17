import imageio

# List of image filenames to include in the GIF
image_filenames = ['image1.jpeg', 'image2.jpeg', 'image3.jpeg']

# Duration (in seconds) for each frame
duration = 2

# Create a list to store the images
images = []

# Read each image and append it to the list
for filename in image_filenames:
    images.append(imageio.imread(filename))

# Save the images as a GIF
output_file = 'output.gif'
imageio.mimsave(output_file, images, duration=duration)

print(f'GIF saved as {output_file}')
