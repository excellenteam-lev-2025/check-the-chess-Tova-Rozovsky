import logging

logger = logging.getLogger("chess_logger")
logger.setLevel(logging.DEBUG)

# למנוע כפילות אם כבר קיים
if not logger.handlers:
    # קונסולה (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # לקובץ
    file_handler = logging.FileHandler("log.log_chess", mode='a')
    file_handler.setLevel(logging.DEBUG)

    # פורמט
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

