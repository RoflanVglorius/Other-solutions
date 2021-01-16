def compute(day, film):
  if day == 8:
    if film == "ирония":
      return 1
    else:
      return 0
  if film == "ёлки":
    return compute(day + 1, "один") * 0.2 + compute(day + 1, "ирония") * 0.8
  elif film == "один":
    return compute(day + 1, "ёлки") * 0.5 + compute(day + 1, "ирония") * 0.5
  else: 
    return compute(day + 1, "один") * 0.3 + compute(day + 1, "ирония") * 0.7
print(compute(1, "один") * 0.2 + compute(1, "ирония") * 0.8)

# Данный код позволяет нам найти вероятность того, что покажут фильм "Ирония судьбы" на Новый Год. Ответ: 0.6666623399999998
