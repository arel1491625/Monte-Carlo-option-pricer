import numpy as np
import matplotlib.pyplot as plt

input_option = input("Will You Input Paramaters :0) one by one or 1) as a list of parameters?")
if input_option == "0":
    #|Initial price:
    S0 = float(input("Enter the initial stock price (S0): "))
    #|Drift:
    mu = float(input("Enter the drift (mu): "))
    #|Volatility:
    sigma = float(input("Enter the volatility (sigma): "))
    #|Total duration of the option:
    T = float(input("Enter the total duration of the option (T): "))
    #|Time step size:
    dt = float(input("Enter the time step size (dt): "))
    #|Total steps:
    N = int(T/dt)
    #|Number of simulations:
    A = int(input("Enter the number of simulations (A): "))
    #|The strike price:
    K = float(input("Enter the strike price (K): "))
    #|Risk-free interest rate:
    r = float(input("Enter the risk-free interest rate (r): "))

elif input_option == "1":
    param_list = input("Enter the parameters as a list [S0, mu, sigma, T, dt, A, K, r]: ")
    param_list = param_list.strip('[]').split(',')
    S0, mu, sigma, T, dt, A, K, r = map(float, param_list)
    N = int(T/dt)
#|Initial price: S0
#|Drift: mu
#|Volatility: sigma
#|Total duration of the option: T 
#|Time step size: dt
#|Total steps: N
#|Number of simulations: A 
#|The strike price: K
#|Risk-free interest rate: r

a = np.array([S0, mu, sigma, T, dt, A, K, r])
#            [0 , 1 , 2    , 3, 4 , 5, 6, 7]


# takes an array of parameters and returns a matrix of simulated stock price paths
def gen_path_m_c(a):
    arr_path = np.exp((a[1] - 0.5 * a[2]**2) * a[4] + a[2] * np.sqrt(a[4]) * np.random.normal(0, 1, size=(int(a[5]), int(a[3]/a[4]))))
    arr_path = np.cumprod(arr_path, axis=1)
    arr_path *= a[0]
    return arr_path

#takes a matrix of simulated stock price paths and returns the estimated call option premium
def call_premium_estimate(arr_path, a):
    final_prices = arr_path[:, -1]
    payoffs = np.maximum(final_prices - a[6], 0)
    option_price = np.exp(-a[7]*a[3]) * np.mean(payoffs)
    return option_price


#takes a matrix of simulated stock price paths and returns the estimated put option premium
def put_premium_estimate(arr_path, a):
    final_prices = arr_path[:, -1]
    payoffs = np.maximum(a[6] - final_prices, 0)
    option_price = np.exp(-a[7]*a[3]) * np.mean(payoffs)
    return option_price

paths = gen_path_m_c(a)
call = call_premium_estimate(paths, a)
put = put_premium_estimate(paths, a)
print("Call premium:", call)
print("Put premium:", put)
#put-call parity check
print("Put-call parity check - LHS:", call - put, "RHS:", a[0] - a[6]*np.exp(-a[7]*a[3]))
