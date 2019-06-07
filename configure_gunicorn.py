from src.config_provider import ConfigProvider

provided_config = ConfigProvider.provide()

workers = provided_config['workers']
timeout = provided_config['wsgi_timeout']
reload = provided_config['reload']

worker_class = 'sync'
bind = f"{provided_config['host']}:{provided_config['port']}"
