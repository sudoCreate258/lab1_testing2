import logging as lg

lg.basicConfig(
    filename="logs/lab1_test2.log",
    level=lg.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="w"
)

log = lg.getLogger(__name__)
