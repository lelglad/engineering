import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3
signal_frequency = 10
sampling_frequency = 500

dac = None
try:
    dac = pwm.PWM_DAC(12,10000,3.3,verbose=False)
    start_time = time.time()
    while True:
        current_time = time.time()-start_time
        voltage = sg.get_sin_wave_amplitude(signal_frequency,current_time)*amplitude
        dac.set_voltage(voltage)
finally:
    if dac is not None:
        dac.deinit()