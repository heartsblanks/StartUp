import logging


class BrokerFunctions:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info("Broker functions selected.")

