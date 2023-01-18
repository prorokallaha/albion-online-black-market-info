from bm_prices import script
from items_db import checker
from threading import *

t1 = Thread(script.prices_json())
t2 = Thread(checker.checker_items())


def main():
    t1.start()
    t2.start()


if __name__=="__main__":
    main()
