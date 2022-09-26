import matplotlib.pyplot as plt
import numpy as np
image = np.random.randint(0, 255, size = (10, 10, 3))
plt.imshow(image)
plt.show()