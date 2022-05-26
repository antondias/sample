from metalabblender import blender

def test_render():
    blend = blender.Blender("fpath", "3.0.1", "PNG", "CUDA", 1, 100, "token")
    blend.render() 