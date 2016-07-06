class SandboxAPI:
    def __init__(self, pipe_file):
        self.pipe_file = pipe_file
        self.pipe = open(self.pipe_file, 'w')
   
    def set_colormap(self, color_map_file):
        self.pipe.write("colorMap " + color_map_file)
        self.pipe.flush()
