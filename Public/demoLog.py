import logging
import datetime


class demo_Log:

    def __init__(self):
        self.logger = logging.getLogger('logger')

    def log(self):
        # 创建日志器
        # 设置日志最低输出等级
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            # 创建处理器
            sh = logging.StreamHandler()

            fh = logging.FileHandler(
                filename='Log/{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S_%f'),
                                             encoding='UTF-8'))
            # 创建格式器
            fm = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %X')
            sh.setFormatter(fm)
            fh.setFormatter(fm)
            self.logger.addHandler(fh)
            self.logger.addHandler(sh)

        return self.logger
