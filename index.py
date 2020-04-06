weather_today = '晴れのち雨'
print(weather_today[0])
print(weather_today[-1])


weather_MAP = {
        "晴": 99,
        "曇": chr(0x1000AC),
        "雨": chr(0x1000AA),
        "雪": chr(0x1000AB),
}

print(weather_MAP[weather_today[0]])