import skewtpy

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    sounding = skewtpy.profile.from_wyo_text('./test/test_wyo_sounding')
    fig = plt.figure()
    fig, ax = sounding.create_fig_ax(figure)
    plt.show()
