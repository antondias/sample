import jwt
import json
import base64
import datetime
import time

class TokenHandler:

	secret = "GEwLxiNDTXYErljimTdf"

	def decode_token(token):	
			try:
			    decode_data = jwt.decode(jwt=token, \
			                            key=self.secret, algorithms="HS256")
			    return decode_data
			except jwt.ExpiredSignatureError:
				print("Token expired")
			except jwt.InvalidTokenError:
				print("Invalid Token")

	def validate(base64Value):
		if (base64Value == None):
			raise Exception("Token not found")
		current_time = None
		user_time = None
		try:
			base64String = base64.b64decode(base64Value) 
			jsonString = json.loads(base64String)
			ct = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
			user_time = time.strptime(jsonString['exp'], "%Y-%m-%d %H:%M:%S")
			current_time = time.strptime(ct, "%Y-%m-%d %H:%M:%S")
		except:
			raise Exception("Error.Can't extract data from token")
		if (current_time > user_time):
			raise Exception("Token expired. please regenerate script from https://blendertool.com")	