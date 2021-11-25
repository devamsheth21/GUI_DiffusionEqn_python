import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("2D heat equation solver")

class Add_transaction():
    

    def add_transaction(self,var1,var2,var3,var4,var5,var6,var7,var8,t):
        countlist = []
        klist = []
        plate_length = int(var1)
        max_iter_time = 250

        alpha =int( var2)  # diffusion term m2/s
        delta_x = int(var3)  # Grid Spacing
        ncell = (plate_length / delta_x)
        delta_t = (delta_x ** 2) / (4 * alpha)  # Time Step
        gamma = (alpha * delta_t) / (delta_x ** 2)
        rms = 0

        # Initialize solution: the grid of u(k, i, j)
        u = np.empty((max_iter_time, plate_length, plate_length))
        u_iter = np.empty((max_iter_time, plate_length, plate_length))
        # Initial condition everywhere inside the grid
        u_initial = int(var4)

        # Boundary conditions
        u_top = int(var5)
        u_left = int(var6)
        u_bottom = int(var7)
        u_right = int(var8)

        #v=2 impli
        which_code = 2

        #v=1 expli
        if which_code == 1:
            # Set the initial condition
            u.fill(u_initial)

            # Set the boundary conditions
            u[:, (plate_length - 1):, :] = u_top
            u[:, :, :1] = u_left
            u[:, :1, 1:] = u_bottom
            u[:, :, (plate_length - 1):] = u_right


            # Solving explicitly
            def calculate(u):
                for k in range(0, max_iter_time - 1, 1):
                    for i in range(1, plate_length - 1, delta_x):
                        for j in range(1, plate_length - 1, delta_x):
                            u[k + 1, i, j] = gamma * (
                                    u[k][i + 1][j] + u[k][i - 1][j] + u[k][i][j + 1] + u[k][i][j - 1] - 4 * u[k][i][j]) + \
                                            u[k][i][j]

                return u


            def plotheatmap(u_k, k):
                # Clear the current plot figure
                plt.clf()

                plt.title(f"Temperature at t = {k * delta_t:.3f} unit time")
                plt.xlabel("x")
                plt.ylabel("y")

                # This is to plot u_k (u at time-step k)
                plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)

                plt.colorbar()

                return plt


            # Do the calculation here
            u = calculate(u)


            def animate(k):
                plotheatmap(u[k], k)


            # Writer = animation.writers['pillow']
            # Writer = animation.writers['ffmpeg']
            # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
            # writer = animation.FFMpegWriter(fps=5, codec=None, bitrate=1800, extra_args=None, metadata= dict(artist='Me'))

            anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
            # anim.save("heat_equation_solution")

            writergif = animation.PillowWriter(fps=15)
            anim.save("saved.gif", writer=writergif)

            print("Done for explicit!")


        elif which_code == 2:
            # Set the initial condition
            u.fill(u_initial)
            u_iter.fill(u_initial)

            # Set the boundary conditions
            u[:, (plate_length - 1):, :] = u_top
            u[:, :, :1] = u_left
            u[:, :1, 1:] = u_bottom
            u[:, :, (plate_length - 1):] = u_right


            # Solving Implicitly Using gauss seidel algorithm

            def calculate(u):
                for k in range(0, max_iter_time - 1, 1):
                    rms = 2.0
                    sq = 0
                    count = 0
                    while rms > 0.00000001:
                        sum = 0
                        for i in range(1, plate_length - 1, delta_x):
                            for j in range(1, plate_length - 1, delta_x):
                                u[k + 1, i, j] = (gamma * (
                                        u[k + 1][i + 1][j] + u[k + 1][i - 1][j] + u[k + 1][i][j + 1] + u[k + 1][i][j - 1]) +
                                                u[k][i][j]) / (1 + 4 * gamma)
                        # print("for loop 1 completed")
                        for i in range(1, plate_length - 1, delta_x):
                            for j in range(1, plate_length - 1, delta_x):
                                sq = ((u[k + 1][i][j]) - (u_iter[k + 1][i][j])) ** 2
                                sum += sq
                        # print("for loop 2 completed")
                        rms = (math.sqrt(sum)) / (plate_length ** 2)
                        for i in range(1, plate_length - 1, delta_x):
                            for j in range(1, plate_length - 1, delta_x):
                                u_iter[k + 1, i, j] = u[k + 1, i, j]
                        count += 1
                    countlist.append(count)
                    klist.append(k + 1)
                    print(count, k + 1)
                return u


            def plotheatmap(u_k, k):
                # Clear the current plot figure
                plt.clf()

                plt.title(f"Temperature at t = {k * delta_t:.3f} unit time")
                plt.xlabel("x")
                plt.ylabel("y")

                # This is to plot u_k (u at time-step k)
                plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)

                plt.colorbar()

                return plt


            # Do the calculation here
            u = calculate(u)


            def animate(k):
                plotheatmap(u[k], k)


            # Writer = animation.writers['pillow']
            # Writer = animation.writers['ffmpeg']
            # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
            # writer = animation.FFMpegWriter(fps=5, codec=None, bitrate=1800, extra_args=None, metadata= dict(artist='Me'))

            anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
            # anim.save("heat_equation_solution")

            writergif = animation.PillowWriter(fps=15)
            anim.save("saved.gif", writer=writergif)

            print("Done for implicit!")

            print(countlist)
            print(klist)
            



