# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.


def fake_bin(x):
    resultado = []
    for i in x:
        if int(i) < 5:
            resultado.append("0")
        else:
            resultado.append("1")
    return "".join(resultado)