import logging
import os
import time

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename="logs.log", filemode='w', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def task_with_logging():
    setup_logger()
    start = time.time()
    while (elapsed := time.time() - start) < 60:
        logging.info(f"Програма працює {elapsed:.2f} секунд")
        time.sleep(5)
    logging.error("Task completed")

if __name__ == "__main__":
    task_with_logging()