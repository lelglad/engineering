import RPi.GPIO as GPIO
dac_bits = [16,5,25,17,27,23,22,24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits,GPIO.OUT)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not(0.0 <= voltage <= dynamic_range):
        print('Напряжение выходит за динамический диапазон ЦАП (0.00 - {dinamic_range:.2f} B)')
        print('Устанавливаем 0.0 B')
        return 0
    return int(voltage/dynamic_range * 255)
def number_to_dac(number):
    bits = [int(element) for element in bin(number)[2:].zfill(8)]
    GPIO.output(dac_bits,bits)
    return(f'Число на вход ЦАП: {number}, биты: {bits}')

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            print(number_to_dac(number))
        except ValueError:
            print('Вы ввели не число. Попробуйте еще раз\n')
finally:
    GPIO.output(dac_bits,0)
    GPIO.cleanup()
