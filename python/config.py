from os import path, getcwd
import yaml

# parses the yml file relative to the current working directory if it config_filename is a relative path
# or at the path specified if it's an absolute path
def read_config(config_filename = "../DO-NOT-COMMIT/config.yml"):
    if path.isabs(config_filename):
        config_path = config_filename
    else:
        config_path = path.join(getcwd(), config_filename)
    with open(config_path) as s:
        return yaml.safe_load(s)
    