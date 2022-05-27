import os
import subprocess

blender_url_dict = {'2.79b'   : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2",
                    '2.80rc3' : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.80/blender-2.80rc3-linux-glibc217-x86_64.tar.bz2",
                    '2.81a'   : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2",
                    '2.82a'   : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.82/blender-2.82a-linux64.tar.xz",
                    '2.83.19' : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.83/blender-2.83.19-linux-x64.tar.xz",
                    '2.90.1'  : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.90/blender-2.90.1-linux64.tar.xz",
                    '2.91.2'  : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.91/blender-2.91.2-linux64.tar.xz",
                    '2.92.0'  : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.92/blender-2.92.0-linux64.tar.xz",
                    '2.93.8'  : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.93/blender-2.93.8-linux-x64.tar.xz",
                    '3.0.1'   : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender3.0/blender-3.0.1-linux-x64.tar.xz",
                    '3.1.2'   : "https://ftp.nluug.nl/pub/graphics/blender/release/Blender3.1/blender-3.1.2-linux-x64.tar.xz"}

def setup(blenderVersion):
    blender_url = blender_url_dict[blenderVersion]
    base_url = os.path.basename(blender_url)

    try:
        subprocess.run(["mkdir", blenderVersion],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["wget", "-nc", blender_url],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["tar", "-xfk", base_url, "-C", './'+blenderVersion, '--strip-components=1'],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Blender installed..." + blenderVersion)
    except subprocess.CalledProcessError as e:
        print("Something went wrong..... Blender library installtion failed.....")
        print(e.output)


def enable_rendering(gpu_enabled, cpu_enabled):
    data = "import re\n"+\
    "import bpy\n"+\
    "scene = bpy.context.scene\n"+\
    "scene.cycles.device = 'GPU'\n"+\
    "prefs = bpy.context.preferences\n"+\
    "prefs.addons['cycles'].preferences.get_devices()\n"+\
    "cprefs = prefs.addons['cycles'].preferences\n"+\
    "print(cprefs)\n"+\
    "for compute_device_type in ('CUDA', 'OPENCL', 'NONE'):\n"+\
    "    try:\n"+\
    "        cprefs.compute_device_type = compute_device_type\n"+\
    "        print('Device found:',compute_device_type)\n"+\
    "        break\n"+\
    "    except TypeError:\n"+\
    "        pass\n"+\
    "for device in cprefs.devices:\n"+\
    "    if not re.match('intel', device.name, re.I):\n"+\
    "        print('Activating',device)\n"+\
    "        device.use = "+str(gpu_enabled)+"\n"+\
    "    else:\n"+\
    "        device.use = "+str(cpu_enabled)+"\n"
    with open('setgpu.py', 'w') as f:
        f.write(data)    