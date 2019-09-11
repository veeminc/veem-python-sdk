# import from python libraries
import yaml
import logging
import argparse

from veem.models.context import VeemContext

from veem.utils import file_access_check, reverse_attrdict

logger = logging.getLogger(__name__)

class ConfigLoader(object):

    @property
    def parser(self):
        parser = argparse.ArgumentParser(description='Configuration Loader')
        parser.add_argument('--yaml_file', type=str,
                            help='Path of configuration yaml file')
        parser.add_argument('--configs', type=str,
                            help='YAML string content of secrets')
        return parser

    def __init__(self, yaml_file=None, configs=None, **kwargs):
        self.args = self.parser.parse_args()
        self.configs = configs or self.args.configs
        yaml_file = yaml_file or self.args.yaml_file
        if not self.configs and file_access_check(yaml_file):
            with open(yaml_file, 'r') as fp:
                self.configs = fp.read()

        try:
            self.configs = yaml.load(self.configs, Loader=yaml.FullLoader)
        except Exception as e:
            logger.error('Failed to yaml load configuration: %s' % str(e))
            self.configs = {}

        if not self.configs:
            raise AttributeError('Missing configuration')

        self.configs = reverse_attrdict(self.configs)
        self.context = VeemContext(**self.configs)

    def __getattr__(self, attr):
        """ dunder getattr method from secrets"""
        return self.configs.get(attr, None)

    @property
    def environment(self):
        return self.configs.get('environment', 'SANDBOX')

    @property
    def connectionTimeout(self):
        return self.configs.get('connectionTimeout', 1000)

    @property
    def readTimeout(self):
        return self.configs.get('readTimeout', 1000)

    @property
    def retryAttempts(self):
        return self.configs.get('retryAttempts', 1)
