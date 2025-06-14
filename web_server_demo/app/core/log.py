import os
import re
import datetime
import logging
import sys
from app.core.config import settings


try:
    import codecs
except ImportError:
    codecs = None


class MultiprocessHandler(logging.FileHandler):
    """
    Say something about the ExampleClass...

    Args:
        args_0 (`type`):
        ...
    """
    def __init__(self, filename, when='D', backupCount=0, encoding=None, delay=False):
        self.prefix = filename
        self.backupCount = backupCount
        self.when = when.upper()
        self.extMath = r"^\d{4}-\d{2}-\d{2}"

        self.when_dict = {
            'S': "%Y-%m-%d-%H-%M-%S",
            'M': "%Y-%m-%d-%H-%M",
            'H': "%Y-%m-%d-%H",
            'D': "%Y-%m-%d"
        }

        self.suffix = self.when_dict.get(when)
        if not self.suffix:
            print('The specified date interval unit is invalid: ', self.when)
            sys.exit(1)

        self.filefmt = os.path.join('.', "logs", f'{self.prefix}-{self.suffix}.log')

        self.filePath = datetime.datetime.now().strftime(self.filefmt)

        _dir = os.path.dirname(self.filefmt)
        try:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception as e:
            print('Failed to create log file: ', e)
            print("log_path：" + self.filePath)
            sys.exit(1)

        if codecs is None:
            encoding = None

        logging.FileHandler.__init__(self, self.filePath, 'a+', encoding, delay)

    def shouldChangeFileToWrite(self):
        _filePath = datetime.datetime.now().strftime(self.filefmt)
        if _filePath != self.filePath:
            self.filePath = _filePath
            return True
        return False

    def doChangeFile(self):
        self.baseFilename = os.path.abspath(self.filePath)
        if self.stream:
            self.stream.close()
            self.stream = None

        if not self.delay:
            self.stream = self._open()
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)

    def getFilesToDelete(self):
        dir_name, _ = os.path.split(self.baseFilename)
        file_names = os.listdir(dir_name)
        result = []
        prefix = self.prefix + '-'
        for file_name in file_names:
            if file_name[:len(prefix)] == prefix:
                suffix = file_name[len(prefix):-4]
                if re.compile(self.extMath).match(suffix):
                    result.append(os.path.join(dir_name, file_name))
        result.sort()

        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        try:
            if self.shouldChangeFileToWrite():
                self.doChangeFile()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def write_log():
    loggerTmp = logging.getLogger()
    loggerTmp.setLevel(logging.DEBUG)
    # formatter = '%(asctime)s ｜ %(levelname)s ｜ %(filename)s ｜ %(funcName)s ｜ %(module)s ｜ %(lineno)s ｜ %(message)s'
    fmt = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(funcName)s %(message)s')

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(fmt)

    log_name = settings.LOG_NAME
    file_handler = MultiprocessHandler(log_name, when='D', backupCount=settings.LOGS_NUM)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)
    file_handler.doChangeFile()

    loggerTmp.addHandler(stream_handler)
    loggerTmp.addHandler(file_handler)

    return loggerTmp


logger = write_log()


if __name__ == "__main__":
    message = 'test writing logs'
    loggerT = write_log()
    loggerT.info(message)
    loggerT.debug(message)
    loggerT.error(message)