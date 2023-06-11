## Any execution is happen we should log all those informations, execution everything in some file
## so we will be able to track if there are some errors, we can log into the text file
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  ## It creates seperate folder for logs (this comment may be wrong check it)
os.makedirs(logs_path,exist_ok=True) ## Even though there is files, it appends the files


LOG_PATH_FILE = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)
# if __name__=="__main__":
#     logging.info("Logging has started")
