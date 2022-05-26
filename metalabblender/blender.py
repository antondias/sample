from metalabblender import blender,tokenhandler,helper,ldpreload
import subprocess

class Blender:

	token = None
	filePath = None
	outputPath = None
	blenderVersion = None
	fileFormat = None
	renderEngine = None
	startFrame = None
	endFrame = None
	renderer = None
	optixEnabled = None

	def __init__(self, filePath, outputPath, blenderVersion, fileFormat, renderEngine, startFrame, endFrame, 
				renderer, optixEnabled, token):
		self.token = token
		self.filePath = filePath
		self.outputPath = outputPath
		self.blenderVersion = blenderVersion
		self.fileFormat = fileFormat
		self.renderEngine = renderEngine
		self.startFrame = startFrame
		self.endFrame = endFrame
		self.renderer = renderer
		self.optixEnabled = optixEnabled
		ldpreload.preload()

	def gpu_setup():
		gpu = subprocess.run(["nvidia-smi", "--query-gpu=gpu_name", "--format=csv,noheader"],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		gpu = gpu.stdout
		print("Current GPU: " + gpu)

		if gpu == "Tesla K80" and self.optixEnabled:
			print("OptiX disabled because of unsupported GPU")
			self.optixEnabled = False	

	def render(self):
		tokenhandler.TokenHandler.test()
		print("token = " + self.token);
		start_thread()	
		print("starting to process blender...")
		if(start == end):
			print("--------------------------------------------")
			print("------ This process has been already completed------")
			print("--------------------------------------------")
			return
		args = ["sudo", blender_binary, 
				"-b", blender_file_path, 
				"-noaudio","-E", self.renderEngine,
				"--log-level","1",
				"-o", self.outputPath, 
				"-s", str(self.startFrame),
				"-e", str(self.endFrame),
				"-a", "--", "--cycles-device", self.renderer
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