import os
import logging
import logging.handlers

# LOGGER = logging.getLogger(__name__)
print("log")

def init_log(name):

    print("init_log()")
    log_file_path = r"/Users/elber9898/Desktop/log.txt"
    LOGGER = logging.getLogger(name)

    LOGGER.setLevel(logging.INFO)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s(%(lineno)d) %(message)s ", "%Y-%m-%d %H:%M:%S")
    # ch.setFormatter(formatter)
    # LOGGER.addHandler(ch)

    log_dir = os.path.dirname(log_file_path)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    fh = logging.handlers.RotatingFileHandler(log_file_path, maxBytes=10 * 1024 * 1024, backupCount=9)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    LOGGER.addHandler(fh)
    return LOGGER

# if __name__=="__main__":
#     LOGGER = logging.getLogger()
#     filePath = r'D:\log.txt'
#     init_log(LOGGER, filePath)