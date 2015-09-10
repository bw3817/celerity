from django.shortcuts import render
from numerals.forms import NumeralsForm


def calc_numerals(value):
    basic_values = {
        1: 'I', 5: 'V', 10: 'X', 50: 'L',
        100: 'C', 500: 'D', 1000: 'M',
    }
    other_values = {
        4: 'IV',
        9: 'IX',
        40: 'XL',
        90: 'XC',
        400: 'CD',
        900: 'CM',
    }
    basic_values.update(other_values)
    sorted_basic_values = sorted(basic_values.keys(), reverse=True)
    numerals = []

    while value > 0:
        for basic_value in sorted_basic_values:
            q, r = divmod(value, basic_value)
            if q > 0:
                numerals.append(basic_values[basic_value]*q)
                value -= basic_value * q

    return ''.join(numerals)


def convert(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = NumeralsForm(data)
        if form.is_valid():
            data['roman_numerals'] = calc_numerals(int(data['some_number']))

    else:
        form = NumeralsForm()

    return render(request, 'convert.html', {'form': form})
