# TM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    #contador para contar todos los datos correctos del string, lo ideal es que este contador tenga el mismo largo de strin ya que esto quiere decir que todos los caracteres del string son validos.
    contador = 0
    #validador de caracteres del string
    for caracter in pin:
        for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if caracter == num:
                contador += 1
    #validador de las condiciones para arrojar el resultado
    if ((len(pin) ==4) or (len(pin) ==6)) and contador == len(pin):
        return True
    else: return False


#other option
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()