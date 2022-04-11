# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:15:55 2022

@author: solis
"""
import csv
from os.path import isfile


def tevents(org, dst, delimiter=','):
    """
    Readss pp in org and writes only events pp>0 limited by 0 in the the time
    before and after it

    Parameters
    ----------
    org : str
        csv input file
    dst : text
        csv output file

    Returns
    -------
    None.

    """
    def pp_get(row):
        return float(row[2])


    if isfile(dst):
        ask = input('The output file already exists, continue? y/n: ')
        if ask.lower() != 'y':
            return

    with open(org) as fi, open(dst, mode='w', newline='') as fo:
        reader = csv.reader(fi, delimiter=",")
        writer = csv.writer(fo, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for nrow, row in enumerate(reader):
            print(nrow)
            if nrow == 0:
                writer.writerow(row)
            elif nrow == 1:
                writer.writerow(row)
                prev_row = list(row)
                xpp = pp_get(row)
                if xpp > 0.:
                    in_event = True
                else:
                    in_event = False
            else:
                xpp = pp_get(row)
                if in_event == True:
                    writer.writerow(row)
                    if xpp <= 0.:
                        in_event = False
                else:
                    if xpp > 0.:
                        if in_event == False:
                            in_event = True
                            writer.writerow(prev_row)
                        writer.writerow(row)
                    else:
                        if in_event == True:
                            in_event = False
                            writer.writerow(row)
                prev_row = list(row)

        if in_event == False:
            writer.writerow(prev_row)


