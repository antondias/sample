from metalabblender import blender

class LogData:

	def print_data(data):
		print("at log data print = " + str(blender.testVar))
		if (blender.Blender.logEnable):
			print(data)