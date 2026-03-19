import numpy as np

humedad = np.random.rand(5, 5)
sequia = humedad < 0.2  # matriz booleana del mismo tamaño
print(sequia)
