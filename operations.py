
from typing import Annotated
from constants import VOLT_DEFAULT, VOLT_TIG, EF_ETA, ALPHA_N, THIN, MEDIUM

def elect_diam(
    i: Annotated[float, "Сварочный ток, A"],
) -> float:
    # расчет диаметра электрода
    return 0.036*(i**0.5)

def heat_inp(
    k: Annotated[float, "Коэффициент способа сварки"],
    i: Annotated[float, "Сварочный ток, A"],
    v: Annotated[float, "Скорость сварки м/ч"],
    is_tig: Annotated[float, "Признак способа TIG"],
) -> float:
    # расчет погонной энергии
    u = VOLT_TIG if is_tig else VOLT_DEFAULT
    return k*i*u*EF_ETA/v

def depos_rate(
    k: Annotated[float, "Коэффициент способа сварки"],
    i: Annotated[float, "Сварочный ток, A"],
    v: Annotated[float, "Скорость сварки м/ч"],
) -> float:
    # расчет производительности V_напл
    return k*i*ALPHA_N/v

def thick_class(
    s: Annotated[float, "Толщина металла, мм"],
) -> str:
    # классификация толщины
    if s < THIN:
        return "тонкий металл"
    elif s <= MEDIUM:
        return "средний металл"
    else:
        return "толстый металл"