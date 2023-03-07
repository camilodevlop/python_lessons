# Logging management.

import logging as log

log.basicConfig(level = log.DEBUG,
                format = '%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s %(message)s]',
                datefmt = '%I:%M:%S %p',
                handlers = [
                            log.FileHandler('data_layer.log'),
                            log.StreamHandler()
                            ]
                )

if __name__ == '__main__':
    log.debug('\tDEBUG level message')
    log.info('\tINFO level message')
    log.warning('\tWARNING level message')
    log.error('\tERROR level message')
    log.critical('\tCRITICAL level message')

#-------------------------------------------------------------------
