import logging

# here I am doing the logging for the code
logging.basicConfig(
    filename='quest_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Logging system processing.")
#Now in the file quest_log I can capture every download and error 