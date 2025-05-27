import os

############### Number of log files ###############
LOGS_NUM = int(os.getenv("logs_num", "0"))
log_file_name = os.getenv("log_file", "demo")
