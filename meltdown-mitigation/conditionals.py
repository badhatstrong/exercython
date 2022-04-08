from typing import Union


def is_criticality_balanced(temperature, neutrons_emitted: Union[int, float]) -> bool:
    """
    temperature: temperature value in kelvin (integer or float)
    neutrons_emitted: number of neutrons emitted per second (integer or float)
    result - boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power: Union[int, float]) -> str:
    """
    voltage: voltage value (integer or float)
    current: current value (integer or float)
    theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    str one of 'green', 'orange', 'red', or 'black'

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    efficiency: Union[int, float] = voltage * current / theoretical_max_power * 100

    if efficiency < 30:
        return "black"
    elif efficiency < 60:
        return "red"
    elif efficiency < 80:
        return "orange"
    return "green"


def fail_safe(temperature, neutrons_produced_per_second, threshold: Union[int, float]) -> str:
    """
    temperature: value of the temperature in kelvin (integer or float)
    neutrons_produced_per_second: neutron flux (integer or float)
    threshold: threshold (integer or float)
    str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    variable: Union[int, float] = temperature * neutrons_produced_per_second

    if variable < threshold * 0.9:
        return "LOW"
    elif threshold * 0.9 < variable < threshold * 1.1:
        return "NORMAL"
    return "DANGER"
