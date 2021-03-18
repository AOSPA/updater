import os

class Config(object):
    GERRIT_URL = os.environ.get('GERRIT_URL', 'https://gerrit.aospa.co')
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_DEFAULT_TIMEOUT', '3600'))
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST', 'redis')
    CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB', 4)

    UPSTREAM_URL = os.environ.get('UPSTREAM_URL', '')
    DOWNLOAD_BASE_URL = os.environ.get('DOWNLOAD_BASE_URL', 'https://updates.aospa.co')

    DEVICES_JSON_PATH = os.environ.get('DEVICES_JSON_PATH', 'devices.json')
    DEVICE_DEPS_PATH = os.environ.get('DEVICE_DEPS_PATH', 'device_deps.json')
