__author__ = 'ataylor'

from pandas import DataFrame
import numpy as np
import warnings


def create_sounding_df(data=None, index=None, columns=None, dtype=None, copy=False):
    df = DataFrame(data, index, columns, dtype, copy)
    if 'pressure' not in df.columns:
        df['pressure'] = np.nan
        warnings.warn('warning no pressure data present')
    else:
        df.set_index('pressure', inplace=True)
    if 'temperature' not in df.columns:
        df['temperature'] = np.nan
    if 'dew_point' not in df.columns:
        df['dew_point'] = np.nan
    if 'wind_dir' not in df.columns:
        df['wind_dir'] = np.nan
    if 'wind_speed' not in df.columns:
        df['wind_speed'] = np.nan
    return df


def line_generator(filename):
    """Generate a line of data from the wyo text file.
    At the moment only accepts numerical lines of 11 and
    the returned values are pres, Height, T, Td, WindDir, WindSpeed
    """
    with open(filename) as sound_file:
        good = True
        for line in sound_file:
            if line.startswith('-'):
                continue
            split = line.split()
            if len(split) == 0:
                continue
            try:
                vals = [float(x) for x in split]
            except:
                continue
            if len(vals) != 11:
                continue
            yield [vals[0], vals[1], vals[2], vals[3], vals[6], vals[7]]


def from_wyo_text(filename):
    gen = line_generator(filename)
    sound = create_sounding_df(list(gen), columns=['pressure', 'height', 'temperature',
                                                      'dew_point', 'wind_dir', 'wind_speed'])
    return sound



    



