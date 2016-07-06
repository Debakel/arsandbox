class SandboxAPI:
    def __init__(self, pipe_file):
        self.pipe_file = pipe_file
        self.pipe = open(self.pipe_file, 'w')
   
    def set_colormap(self, color_map_file):
        self.pipe.write("colorMap " + color_map_file)

sandbox = SandboxAPI('Control.fifo')
dir = '###'
colormaps = ['colormap1.cpt', 'colormap2.cpt']

while True:
    for colormap in colormaps:
        sandbox.set_colormap(colormap)
        time.sleep(1) # pause 1 second
    
	
temperatur_farbe = {}
