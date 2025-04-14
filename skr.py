import numpy as np

# Define the parameters
q = 0.5
alpha = 0.2  # dB/km
miu = 0.48
v = 0.05
Y_0 = 6.8 * 10 ** -6  # Per pulse
e_d = 0.023
e_0 = 0.5
fec = 1.22
n_tx = 0.1  # Transmittance in rx's si
max_dst = 80

def compute_skr(d,loss,key_len):
    eta = n_tx * np.power(10, -1 * ((alpha * d + loss) / 10))
    Q_miu = Y_0 + 1 - np.exp(-1 * eta * miu)
    Q_v = Y_0 + 1 - np.exp(-1 * eta * v)
    E_miu = (e_0 * Y_0 + e_d * (1 - np.exp(-1 * eta * miu))) / Q_miu
    Q_1L = ((np.power(miu, 2) * np.exp(-1 * miu)) / (miu * v - np.power(v, 2))) * (
            Q_v * np.exp(v) - Q_miu * np.exp(miu) * (np.power(v, 2) / np.power(miu, 2)) - E_miu * Q_miu * np.exp(miu) * ((np.power(miu, 2) - np.power(v, 2)) / (np.power(miu, 2) * 0.5)))
    e_1U = E_miu * Q_miu/Q_1L
    H_2_E_miu = (-1) * E_miu/100 * np.log2(E_miu/100) - (1 - E_miu/100) * np.log2(1 - E_miu/100)
    H_2_e_1U = (-1) * e_1U * np.log2(e_1U) - (1 - e_1U) * np.log2(1 - e_1U)
    return ((q * (Q_1L * (1 - H_2_e_1U) - Q_miu * fec * H_2_E_miu)) * 2.5 * np.power(10, 9))/key_len
