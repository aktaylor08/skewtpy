__author__ = 'ataylor'


from pandas import DataFrame
import numpy as np
import warnings

from . import plotting

class Sounding(DataFrame):

    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False):
        DataFrame.__init__(self, data, index, columns, dtype, copy)
        if 'pressure' not in self.columns:
            self['pressure'] = np.nan
            warnings.warn('warning no pressure data present')
        else:
            self.set_index('pressure', inplace=True)
        if 'temperature' not in self.columns:
            self['temperature'] = np.nan
        if 'dew_point' not in self.columns:
            self['dew_point'] = np.nan
        if 'wind_dir' not in self.columns:
            self['wind_dir'] = np.nan
        if 'wind_speed' not in self.columns:
            self['wind_speed'] = np.nan

    def create_fig_ax(figure=None):
        if figure is None:
            plotting.create_figure()
        figure, axis = plotting.get_axis(figure)
        axis.semilogy(self.pressure, self.temperature)
        axis.semilogx(self.pressure, self.dew_point)
        


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
    sound = Sounding.from_records(list(gen), columns=['pressure', 'height', 'temperature',
        'dew_point', 'wind_dir', 'wind_speed'])
    return sound



    



