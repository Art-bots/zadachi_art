from datetime import datetime
import logging
import os

def setup_logger():

    today_str = datetime.now().strftime("%Y-%m-%d")

    log_dir = os.path.join("logs", today_str)
    os.makedirs(log_dir, exist_ok=True)  # Создаём папку, если её нет

    log_file_path = os.path.join(log_dir, "bot.log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger