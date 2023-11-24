import os

directory_img = 'labeled_data/train/images'
directory_labels = 'labeled_data/train/labels'

remove_filename = 'a4a84dd61b_png.rf.91f9c2102de370d4aeffe343c3285700'

dims = []
for filename in os.listdir(directory_img):
    f = os.path.join(directory_img, filename)
    fl = os.path.join(directory_labels, filename[:-4]+'.txt')
    if filename[:-4] == remove_filename:
        os.remove(f)
        os.remove(fl)
        print('removed')
    print(f)
    print(fl)
