import os


class ConfigProvider:
    @classmethod
    def provide(cls):
        return {
            'port': 8000,
            'host': '0.0.0.0',
            'workers': 4,
            'wsgi_timeout': 30,
        }
