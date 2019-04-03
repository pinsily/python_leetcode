import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt='%Y/%m/%d %H:%M:%S'
)

logging.basicConfig()
logger = logging.getLogger()


def run_function(solution, function, *args):
    """运行方法并日志打印

    :param
        solution: [第几种方法]
        function: [方法名]
        *args: [方法的顺序参数]
    """
    start = time.clock()
    rt = function(*args)
    logger.info("solution {0} result: {1}".format(solution, rt))
    end = time.clock()
    logger.info("solution {0} time  : {1} s".format(solution, (end - start)))
    return rt
