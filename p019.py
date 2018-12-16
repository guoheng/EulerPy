#!/usr/bin/python

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
import logging

def main(args):
    n = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            d = datetime.date(year, month, 1)
            if (d.weekday() == 6):
                n += 1
                logging.debug(d)
                
    logging.info(n)
