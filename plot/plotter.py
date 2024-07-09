import matplotlib.pyplot as plt

def plot_results(yd, y, e, phi, u):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig1, fig2, fig3, fig4 = axs[0,0], axs[0,1], axs[1,0], axs[1,1]

    fig1.plot(yd, '-b', label='Desired Output')
    fig1.plot(y[0][:-1], '--r', label='y1')
    fig1.plot(y[1][:-1], '-g', label='y2')
    fig1.plot(y[2][:-1], '-y', label='y3')
    fig1.plot(y[3][:-1], '-.k', label='y4')
    fig1.legend(['Desired Output','y1','y2','y3','y4'])
    fig1.grid(True)
    fig1.set_title('Tracking performance for time invariable desired trajectory')
    fig1.set_xlabel('Step')
    fig1.set_ylabel('The tracking performance')

    fig2.plot(e[0][:-1], '--r', label='e1')
    fig2.plot(e[1][:-1], '-g', label='e2')
    fig2.plot(e[2][:-1], '-y', label='e3')
    fig2.plot(e[3][:-1], '-.k', label='e4')
    fig2.legend(['e1','e2','e3','e4'])
    fig2.grid(True)
    fig2.set_title('Consensus tracking errors for time invariable desired trajectory')
    fig2.set_xlabel('Step')
    fig2.set_ylabel('The tracking errors')

    fig3.plot(phi[0][:-1], '--r', label='phi1')
    fig3.plot(phi[1][:-1], '-g', label='phi2')
    fig3.plot(phi[2][:-1], '-y', label='phi3')
    fig3.plot(phi[3][:-1], '-.k', label='phi4')
    fig3.legend(['phi1','phi2','phi3','phi4'])
    fig3.grid(True)
    fig3.set_title('PPD estimation for time invariable desired trajectory')
    fig3.set_xlabel('Step')
    fig3.set_ylabel('The PPD estimation')

    fig4.plot(u[0][:-1], '--r', label='u1')
    fig4.plot(u[1][:-1], '-g', label='u2')
    fig4.plot(u[2][:-1], '-y', label='u3')
    fig4.plot(u[3][:-1], '-.k', label='u4')
    fig4.legend(['u1','u2','u3','u4'])
    fig4.grid(True)
    fig4.set_title('Input for time invariable desired trajectory')
    fig4.set_xlabel('Step')
    fig4.set_ylabel('The input signal')

    plt.show()
