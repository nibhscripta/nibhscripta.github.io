from control import ss

from numpy import array
A = array([
    [-2, 0.5],
    [-1, 0]
])
B = array([
    [1, 1],
    [0, 1]
])
c = array([1, 0])
d = 0

sys = ss(A, B, c, d)

from control import step_response
t, y = step_response(sys)

from matplotlib.pyplot import plot, legend, xlabel, ylabel, show
plot(t, y[0, 0], label="h")
plot(t, y[0, 1], label=r"$e_I$")
xlabel("Time")
ylabel("Response")
legend()
show()

from control import input_output_response

from numpy import ones, zeros, linspace
t = linspace(0, 20, 100)
u_sp = array([
    zeros(100),
    ones(100)
])

t, y = input_output_response(sys, t, u_sp)

plot(t, y[0])
xlabel("Time")
ylabel("Response")
show()

t = linspace(0, 20, 100)
u_disturbance = array([
    ones(100),
    zeros(100)
])

t, y = input_output_response(sys, t, u_disturbance)

plot(t, y[0])
xlabel("Time")
ylabel("Response")
show()