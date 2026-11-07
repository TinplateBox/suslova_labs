
# Коэффициенты режима обработки
K_1: float = 1.0 # руч дуг
K_2: float = 1.15 # mig mag
K_3: float = 0.85 # tig

# Допустимые диапазоны входных данных
S_MIN: float = 0.5
S_MAX: float = 20.0
V_MIN: float = 5.0
V_MAX: float = 80.0
I_MIN: float = 20.0
I_MAX: float = 400.0

# напряжение
VOLT_DEFAULT: float = 25.0
VOLT_TIG: float = 20.0

# коэф-ы и конст-ы
EF_ETA: float = 0.8
ALPHA_N: float = 10.0

# границы толщины металла
THIN: float = 2.0
MEDIUM: float = 8.0

# файл журнала ошибок
LOG_FILE: str = "input_errors.log"
