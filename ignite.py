from src.boiler import app
from src.config_provider import ConfigProvider

app.config['PROPAGATE_EXCEPTIONS'] = False

provided_config = ConfigProvider.provide()

workers = provided_config['workers']
timeout = provided_config['wsgi_timeout']

worker_class = 'sync'
bind = f"{provided_config['host']}:{provided_config['port']}"
