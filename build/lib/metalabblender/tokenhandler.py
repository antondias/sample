import jwt

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

	def test():
		print("token handler test")