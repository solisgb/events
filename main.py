# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:15:01 2022

@author: solis
"""
import littleLogging as logging

org = r'H:\LSGB\20220324_informe_pz\data_chs\saih\pp_mmenor_saih.csv'
dst = r'H:\LSGB\20220324_informe_pz\data_chs\saih\pp_mmenor_saih_events.csv'

if __name__ == "__main__":

    try:
        from datetime import datetime
        from time import time
        import traceback

        import temporal_events as te

        startTime = time()

        te.tevents(org, dst)

        xtime = time() - startTime
        print(f'El script tardó {xtime:0.1f} s')

    except ValueError:
        msg = traceback.format_exc()
        logging.append(f'ValueError exception\n{msg}')
    except ImportError:
        msg = traceback.format_exc()
        print (f'ImportError exception\n{msg}')
    except Exception:
        msg = traceback.format_exc()
        logging.append(f'Exception\n{msg}')
    finally:
        logging.dump()
        print('\nFin')
