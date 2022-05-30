from metalabblender import blender

def test_render():
    blend = blender.Blender("fpath", "output", "3.0.1", "PNG", "CYCLES", 1, 5,
                            "CUDA", False, False, False, False, True, True, "token")
    blend.test_log()