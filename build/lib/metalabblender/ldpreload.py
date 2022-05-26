import os
import subprocess

def preload():
	os.environ["LD_PRELOAD"] = ""

	subprocess.run(["apt", "remove", "libtcmalloc-minimal4"],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run(["apt", "install", "libtcmalloc-minimal4"],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	os.environ["LD_PRELOAD"] = "/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4.3.0"