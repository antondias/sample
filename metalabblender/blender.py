from metalabblender import blender,tokenhandler,ldpreload,setupblender
import subprocess

class Blender:

	token = None
	blenderFilePath = None
	outputPath = None
	blenderVersion = None
	fileFormat = None
	renderEngine = None
	startFrame = None
	endFrame = None
	renderer = None
	optixEnabled = None
	gpuEnabled = None
	cpuEnabled = None
	animation = None

	def __init__(self, blenderFilePath, outputPath, blenderVersion, fileFormat, renderEngine, startFrame, endFrame, 
				renderer, optixEnabled, gpuEnabled, cpuEnabled, animation, token):
		self.token = token
		self.blenderFilePath = blenderFilePath
		self.outputPath = outputPath
		self.blenderVersion = blenderVersion
		self.fileFormat = fileFormat
		self.renderEngine = renderEngine
		self.startFrame = startFrame
		self.endFrame = endFrame
		self.renderer = renderer
		self.optixEnabled = optixEnabled
		self.gpuEnabled = gpuEnabled


	def gpu_setup():
		gpu = subprocess.run(["nvidia-smi", "--query-gpu=gpu_name", "--format=csv,noheader"],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		gpu = gpu.stdout
		print("Current GPU: " + gpu)

		if gpu == "Tesla K80" and self.optixEnabled:
			print("OptiX disabled because of unsupported GPU")
			self.optixEnabled = False

	def set_renderer():
		if optix_enabled:
		self.renderer = "OPTIX"		

	def setup():
		blenderRenderer = Blender()
		blenderRenderer.gpu_setup()
		ldpreload.preload()
		setupblender.setup(self.blenderVersion)
		setupblender.enable_rendering(self.gpuEnabled, self. cpuEnabled)
		blenderRenderer.set_renderer()


	def render(self):
		tokenhandler.TokenHandler.test()
		print("token = " + self.token);	
		print("starting to process blender...")
		blender_binary = './'+self.blenderVersion+"/blender"	
		if (self.animation):
			if start_frame == end_frame:	
				args = ["sudo", blender_binary, 
						"-b", blender_file_path,
						"-P", "setgpu.py", 
						"-noaudio","-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath,
						"-a", "--", "--cycles-device", self.renderer
					]
			else:
				args = ["sudo", blender_binary, 
						"-b", blender_file_path,
						"-P", "setgpu.py",
						"-noaudio","-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath, 
						"-s", str(self.startFrame),
						"-e", str(self.endFrame),
						"-a", "--", "--cycles-device", self.renderer
					]
		else:
			args = ["sudo", blender_binary, 
						"-b", blender_file_path,
						"-P", "setgpu.py",
						"-noaudio","-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath,
						"-f", str(self.startFrame),
						"--", "--cycles-device", self.renderer
					]	

		try:
			print(' '.join(args))
			process = subprocess.Popen(args, stdout=subprocess.PIPE)
			print(process.stdout.read())
			print("Blender Completed...............................................")
			empty_temp_folder()
		except subprocess.CalledProcessError as e:
			print("Something went wrong..... Blender file did not executed.....")
			print(e.output)