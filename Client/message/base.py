import json
from Client.util import logger

log = logger.getChild('MessageClass')

class BaseMessage:
    def __init__(self, data=None):
        self._init_type()
        self.log = log.getChild(self.type)

        self._parse(data)
        self._check_data()

    def _init_type(self):
        self.type = 'BaseMessage'

    def _parse_dict(self, data):
        if data.get('type') is not None:
            self.type = data.get('type')
        self.source = data.get('source')


    def _parse(self, data=None):
        if data is not None:
            if isinstance(data, str):
                self._parse_dict(json.loads(data))
            elif isinstance(data, dict):
                self._parse_dict(data)
            else:
                self.log.error('Wrong type with data: {0}'.format(data))

    def _check_data(self):
        for key in self.to_dict().keys():
            if self.__dict__[key] is None:
                self.log.error('{0} is None'.format(key))
                return False
        return True

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        data = {}
        data['type'] = self.type

        return data

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()