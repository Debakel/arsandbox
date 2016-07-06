import time
from sandbox_api import SandboxAPI

sandbox = SandboxAPI('Control.fifo')
dir = 'dir/'
colormaps = ['colormap1.cpt', 'colormap2.cpt']

while True:
    for colormap in colormaps:
        sandbox.set_colormap(dir + colormap)
        time.sleep(1)  # pause 1 second

temperatur_farbe = {}
