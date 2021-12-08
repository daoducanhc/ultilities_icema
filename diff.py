import numpy as np
from PIL import Image

pre = Image.open('8m.png')
true = Image.open('mask.png')

# pre = pre.resize((1469,1008))
pre = np.array(pre)
# true = true.resize((1469,1008))
true = np.array(true)

diff = np.abs(np.subtract(pre, true))

diff = Image.fromarray(diff).convert('L')
diff = diff.point(lambda p: p > 0 and 255)

diff.save("diff.png")

# diff.save('{}.png'.format(i))
