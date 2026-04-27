import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

dac_pins = [16,20,21,25,26,17,27,22]

try:
    dac = r2r.R2R_DAC(dac_pins,3.3,verbose = False)
    start_time = time.time()
    while True:
        dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()-start_time))
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()