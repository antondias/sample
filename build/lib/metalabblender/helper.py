
class Helper:

	def make_base_directories():
		os.makedirs(base_images, exist_ok=True)
		os.makedirs(output_path, exist_ok=True)
		os.makedirs(temp_path, exist_ok=True)