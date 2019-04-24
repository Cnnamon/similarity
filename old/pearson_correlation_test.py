import cv2
import glob
import re
import numpy as np

dataset_dir = '/opt/datasets/data/simulated_flight_1/valid/'
test_data_dir = dataset_dir + '0/*'

all_files = glob.glob(test_data_dir)
all_files.sort()

triplet = 0
r = []

for filename in all_files:
  if triplet == 0:
    file_a = filename
  elif triplet == 1:
    file_b = filename
  elif triplet == 2:
    file_c = filename

    template = cv2.imread(file_a)
    img_b = cv2.imread(file_b)
    img_c = cv2.imread(file_c)

    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    img_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2GRAY)
    img_c = cv2.cvtColor(img_c, cv2.COLOR_BGR2GRAY)
    
    template = cv2.resize(template, (150, 150))
    img_b = cv2.resize(img_b, (150, 150))
    img_c = cv2.resize(img_c, (150, 150))

    res_a = cv2.matchTemplate(img_b, template, cv2.TM_CCORR_NORMED)
    res_b = cv2.matchTemplate(img_c, template, cv2.TM_CCORR_NORMED)
    
    r.append([res_a[0][0], res_b[0][0]])

    triplet = 0

  triplet += 1

r = np.array(r)

a = (r[:, 0] - r[:, 1])
b = (r[:, 0] - r[:, 1])

print(np.sum(np.array(a) >= 0, axis=0))
print(np.sum(np.array(b) >= 0, axis=0))

