import os


class ConfigProvider:
    DEFAULT_HOST = '0.0.0.0'
    DEFAULT_WORKERS = 4
    DEFAULT_WSGI_TIMEOUT = 10

    @classmethod
    def provide(cls):
        return {
            'port': os.getenv('PORT'),
            'host': os.getenv('HOST', cls.DEFAULT_HOST),
            'workers': os.getenv('WORKERS', cls.DEFAULT_WORKERS),
            'wsgi_timeout': os.getenv('WSGI_TIMEOUT', cls.DEFAULT_WSGI_TIMEOUT),
            'reload': cls._extract_reload(),
        }

    @classmethod
    def _extract_reload(cls):
        raw_value = os.getenv('RELOAD', 'false')

        return raw_value.lower() == 'true'
