#test post request



if __name__=="__main__":
	import requests
	data_load = {"username": "Dale"}
	r = requests.post(r"http://localhost:5000/requests_page", json=data_load)
	
	print(r.text)