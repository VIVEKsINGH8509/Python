import logging

logging.basicConfig(filename= "advancedConfig.log", level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %("
                                                                                 "message)s")

logger = logging.getLogger('advancedConfig_logger')
handler = logger.FileHandler('advancedConfig.log')
formatter = logging.Formatter("%(pastime)s - %(levelness)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('debug message')
logger.info('Info message')

