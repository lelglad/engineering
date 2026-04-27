import mcp4725_driver as mcp
import signal_generator as sg
import time
amplitude = 4
signal_frequency = 10
sampling_frequency = 500
dac = None
try:
    dac = mcp.MCP4725(5,address = 0x61,verbose = False)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        voltage = sg.get_sin_wave_amplitude(signal_frequency,current_time)*amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    if dac is not None:
        dac.deinit()
