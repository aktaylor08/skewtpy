import skewtpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # read the wyo sounding and plot it out.
    sounding = skewtpy.profile.from_wyo_text('test_wyo_sounding')
    fig = plt.figure()
    fig, ax = skewtpy.plot_simple_sounding(sounding, fig)
    plt.show()

