from metalabblender import blender,tokenhandler,ldpreload,setupblender,datalog
import subprocess
import sys,os

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
	animation = None
	audio = None
	logEnable = None

	def __init__(self, blenderFilePath, outputPath, blenderVersion, fileFormat, renderEngine, startFrame, endFrame, 
				renderer, animation, audio, logEnable, token):
		self.token = token
		self.blenderFilePath = blenderFilePath
		self.outputPath = outputPath
		self.blenderVersion = blenderVersion
		self.fileFormat = fileFormat
		self.renderEngine = renderEngine
		self.startFrame = startFrame
		self.endFrame = endFrame
		self.renderer = renderer
		self.animation = animation
		self.audio = audio
		self.logEnable = logEnable


	def gpu_setup():
		gpu = subprocess.run(["nvidia-smi", "--query-gpu=gpu_name", "--format=csv,noheader"],encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		gpu = gpu.stdout
		print("Current GPU: " + gpu)

	def set_renderer(self):
		if self.optixEnabled:
			self.renderer = "OPTIX"

	def setup(self):
		#tokenhandler.TokenHandler.decode_token(self.token)
		#Blender.set_renderer(self)	
		Blender.gpu_setup()
		ldpreload.preload()
		setupblender.setup(self.blenderVersion)
		#setupblender.enable_rendering(self.gpuEnabled, self.cpuEnabled)
		print("Setup completed")

	def render(self):
		print("starting to process blender...")
		blender_binary = './'+self.blenderVersion+"/blender"
		audioAvailable = ""
		if (self.audio == False):
			audioAvailable = "-noaudio"
		if (self.animation):
			if self.startFrame == self.endFrame:	
				args = ["sudo", blender_binary, 
						"-b", self.blenderFilePath,
						audioAvailable,"-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath,
						"-a", self.fileFormat, "--", "--cycles-device", self.renderer
					]
			else:
				args = ["sudo", blender_binary, 
						"-b", self.blenderFilePath,
						audioAvailable,"-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath, 
						"-s", str(self.startFrame),
						"-e", str(self.endFrame),
						"-a", self.fileFormat, "--", "--cycles-device", self.renderer
					]
		else:
			args = ["sudo", blender_binary, 
						"-b", self.blenderFilePath,
						audioAvailable,"-E", self.renderEngine,
						"--log-level","1",
						"-o", self.outputPath,
						"-f", str(self.startFrame),
						self.fileFormat, "--", "--cycles-device", self.renderer
					]	

		try:
			print(' '.join(args))
			process = subprocess.Popen(args, stdout=subprocess.PIPE)
			print(process.stdout.read())
			print("Blender Completed...............................................")
		except subprocess.CalledProcessError as e:
			print("Something went wrong..... Blender file did not executed.....")
			print(e.output)