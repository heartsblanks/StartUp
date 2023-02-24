import json
import logging


class JSONValidator:
    def __init__(self, json_file):
        self.json_file = json_file
        self.logger = logging.getLogger(__name__)

    def validate(self):
        try:
            with open(self.json_file) as f:
                json.load(f)
        except Exception as e:
            self.logger.error(f"Error validating JSON file: {e}")
            raise e

