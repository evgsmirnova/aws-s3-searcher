import search_in_bucket
from config import Config
import loggers
import time

CONFIGFILE_NAME = 'config.json'


def main(config: Config) -> None:
    try:
        with open(config.output_file, 'w') as out:
            res = search_in_bucket.get_object_list(config)
            loggers.logging.info(f"Getting data into {config.output_file}")
            out.writelines(f"{item}\n" for item in res)
    except FileNotFoundError:
        loggers.logging.error(f"File Not Found Error: No such file or directory {config.output_file}")
        exit()
    except OSError as e:
        loggers.logging.error(f"File write error: {e}")
        exit()


if __name__ == '__main__':
    start_time = time.time()
    config = Config.get_config(CONFIGFILE_NAME)
    main(config)
    end_time = time.time()
    execution_time = end_time - start_time
    loggers.logging.info(f"Program execution time: {format(execution_time, '.2f')} seconds")




