from pathlib import Path

from work_mode import WorkMode

class Config:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

        self.package_name: str = None
        self.uri: str = None
        self.work_mode: WorkMode = None
        self.package_version: str = None
        self.output_file: str = None
        self.ascii_tree: bool = None
        self.max_depth: int = None
        self.filter_substring: str = None

    def parse(self) -> 'Config':
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config_data = {}

            for line in f:
                key, value = self._parse_csv_line(line)
                config_data[key] = value

            self._set_attributes(config_data)

            return self
        
    def print(self) -> None:
        print("=== Configuration params ===")

        config_params = {
            'package_name': self.package_name,
            'uri': self.uri,
            'work_mode': self.work_mode.name,
            'package_version': self.package_version,
            'output_file': self.output_file,
            'ascii_tree': self.ascii_tree,
            'max_depth': self.max_depth,
            'filter_substring': self.filter_substring
        }

        for [key, value] in config_params.items():
            print(f"{key}: {value}")

        
    def _set_attributes(self, config_data: dict):
        self.package_name = config_data['package_name']
        self.uri = config_data['uri']
        
        work_mode = config_data['work_mode'].lower()
        if work_mode == 'local':
            self.work_mode = WorkMode.LOCAL
        elif work_mode == 'remote':
            self.work_mode = WorkMode.REMOTE
        else:
            print("Unknown work mode.")

        self.package_version = config_data['package_version']
        self.ascii_tree = config_data['ascii_tree']
        self.output_file = config_data['output_file']
        self.max_depth = config_data['max_depth']
        self.filter_substring = config_data['filter_substring']

    def _parse_csv_line(self, line: str):
        line = line.strip()
        
        comma_index = line.find(',')
        key = line[:comma_index].strip()
        value = line[comma_index + 1:].strip()

        return key, value