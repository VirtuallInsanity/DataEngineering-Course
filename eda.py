import os
import cv2
import shutil
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

directory = 'data/pics'

dims = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        dims.append(str(cv2.imread(f).shape))

print(dims)
dims_df = pd.DataFrame(dims, columns=['dimensions'])
dims_df.groupby('dimensions')

plt.figure(figsize=(10,10))
plt.title('New images size distribution')
plt.hist(dims_df)
plt.xticks(rotation='vertical')
plt.savefig('eda_imgs/new_img_sizes.png')
plt.show()

# -----

directory = 'data/images_300'

dims = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        dims.append(str(cv2.imread(f).shape))

print(dims)
dims_df = pd.DataFrame(dims, columns=['dimensions'])
dims_df.groupby('dimensions')

plt.figure(figsize=(10,10))
plt.title('Images size distribution')
plt.hist(dims_df)
plt.xticks(rotation='vertical')
plt.savefig('eda_imgs/img_sizes.png')
plt.show()

# ----

directory = 'data/labels_300'

labels_boxes = []
labels_count = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f) as txt_f:
            lines = txt_f.readlines()
            print(lines)
            labels_boxes.append(lines)
            labels_count.append(len(lines))

print(labels_count)

unique, counts = np.unique(labels_count, return_counts=True)
unique = [str(i) for i in unique]
labels_histogram = dict(zip(unique, counts))
values_df = pd.DataFrame([labels_histogram])

plt.figure(figsize=(10,10))
plt.title('Number of objects on images')
plt.bar(unique,counts)
plt.savefig('eda_imgs/obj_num.png')
plt.show()

# ---combine images---

old_path = 'data/a/'
new_path = 'data/b/'

for image in os.listdir(old_path):
    print(image)
    shutil.move(old_path+image, new_path+image)


