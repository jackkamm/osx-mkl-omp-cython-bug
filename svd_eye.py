import os
import numpy as np
import scipy.linalg

# import the extension but don't do anything with it
import ext

n = 50
eye = np.eye(n+1, n+1)
u, s, vh = scipy.linalg.svd(eye)
eye2 = u @ np.diag(s) @ vh

print("All close: ", np.allclose(eye, eye2)) 
print("Min(eye2): ", np.min(eye2))

## plot the SVD

from matplotlib import pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,4))
ax = plt.subplot(1, 3, 1)
sns.heatmap(u, ax=ax)
ax.set_title("U")

ax = plt.subplot(1, 3, 2)
sns.heatmap(vh, ax=ax)
ax.set_title("Vh")

ax = plt.subplot(1, 3, 3)
sns.heatmap(eye2, ax=ax)
ax.set_title("U @ S @ Vh")

fname = "svd_eye.png"
try:
	if os.environ["MKL_NUM_THREADS"] == "1":
		fname = "svd_eye_1thread.png"
except KeyError:
	pass
plt.savefig(fname)
