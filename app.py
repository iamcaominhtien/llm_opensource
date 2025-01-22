import os

from src.settings.configs import BaseConfig
from src.settings.init_app import create_app, setup_logging

config = BaseConfig
setup_logging()
app = create_app(config_class=config)

if __name__ == '__main__':
	server_port = os.environ.get('PORT', '8080')
	app.run(debug=False, port=server_port, host='0.0.0.0')
