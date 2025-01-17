import os as _os



ACCESS_TOKEN: str = _os.environ.get('PSS_ACCESS_TOKEN')


PSS_DEVICE_LOGIN_CHECKSUM_KEY: str = _os.environ.get('PSS_DEVICE_LOGIN_CHECKSUM_KEY')


DEFAULT_PSS_PRODUCTION_SERVER: str = 'https://api.pixelstarships.com/'

DEVICE_ID: str = _os.environ.get('PSS_DEVICE_ID')
DEVICE_TYPE: str = 'DeviceTypeAndroid'


LANGUAGE_KEY: str = 'en'


OVERWRITE_PSS_PRODUCTION_SERVER: str = _os.environ.get('PSS_PRODUCTION_SERVER')


TIMESTAMP_FORMAT_PSS: str = '%Y-%m-%dT%H:%M:%S'