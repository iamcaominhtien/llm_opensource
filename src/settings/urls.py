from src.services.demo_test.controllers.ollama_api_demo import OllamaApiDemoAPIController


class APIPath:
	def __init__(self, resource, url):
		self.resource = resource
		self.url = url


api_list = [
	APIPath(OllamaApiDemoAPIController, "/demo-test/ollama-api-demo"),
]
