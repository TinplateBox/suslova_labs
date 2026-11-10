
def check_window(window, n):
    if not isinstance(window, int) or window < 1:
        raise ValueError("окно должно быть целым числом >= 1")
    if window > n:
        raise ValueError("окно не может превышать длину ряда")

def simple_moving_average(data, window):
    check_window(window,len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data, window):
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError("для центрированного среднего окно должно быть нечетным")
    half = window // 2
    result = [None]*len(data)
    for i in range(half, len(data) - half):
        result[i] = sum(data[i - half : i + half + 1]) / window
    return  result

def exponential_moving_average(data, alpha):
    if not (0 < alpha <= 1):
        raise ValueError("коэффициент альфа должен быть в диапазоне (0, 1]")
    result = [data[0]]
    for i in range(1, len(data)):
        ema_val = alpha*data[i] + (1 - alpha)*result[i - 1]
        result.append(ema_val)
    return result