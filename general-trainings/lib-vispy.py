import numpy as np
from vispy import app, visuals, scene

# Створюємо дані
N = 100
pos = np.zeros((N, 3))
colors = np.ones((N, 4))
pos[:, 0] = np.linspace(-0.9, 0.9, N)
colors[:, 0] = np.linspace(0, 1, N)

# Створюємо canvas
canvas = scene.SceneCanvas(keys='interactive', show=True)

# Додаємо точковий графік
scatter = visuals.Markers()
scatter.set_data(pos, face_color=colors)
canvas.central_widget.add_view().add(scatter)

# Запускаємо програму
app.run()
