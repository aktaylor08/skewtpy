__author__ = 'ataylor'


from pandas import DataFrame
import numpy as np

class Sounding(DataFrame):

    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False):
        DataFrame.__init__(self, data, index, columns, dtype, copy)
        if 'temperature' not in self.columns:
            self['temperature'] = np.nan
        if 'dew_point' not in self.columns:
            self['dew_point'] = np.nan
        if 'wind_dir' not in self.columns:
            self['wind_dir'] = np.nan
        if 'wind_speed' not in self.columns:
            self['wind_speed'] = np.nan


def line_generator(filename):
    with open(filename) as sound_file:
        good = True
        for line in sound_file:
            if line.startsiwth('-'):
                continue
            split = line.split()
            if len(split) == 0:
                continue


def from_wyo_text(filename):
    gen = line_generator(filename)
    for line in gen:
        print line


if __name__ == '__main__':
    from_wyo_text('./test/test_wyo_sounding')


