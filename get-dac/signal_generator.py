import numpy
import time
import math
def get_sin_wave_amplitude(freq,time):
    sinx = math.sin(2*math.pi*freq*time)
    norm = (sinx+1)/2
    return norm
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0/sampling_frequency)