import logging


class DeleteItems:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info("Delete items selected.")

