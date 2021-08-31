'''
Дана строка из букв A-Z. Нужно вернуть строку формата [БукваКоличествоПовторений]. Если буква встречается 1 раз, количество повторений писать не нужно.
Например, строка "AAABBCDDDGGGGGGGKKKLMMNNOOOP" вернет "A3B2CD3G7K3LM2NO3P"
Решать задачу нужно без использования специализированных методов, библиотек и т.д.
https://t.me/c/1533281926/20
'''
def RLE(s: str) -> str:
  result = []
  last_sym = None  # последний символ, что мы видели
  count = 0  # и сколько мы его видели

  # мы будем идти по строке и записывать в result при смене символа
  for sym in (list(s) + [None]):  # последний None искусственно триггерит посленюю смену символа

      if last_sym and sym != last_sym:  # если случилась смена символа

          if count == 1:
              result.append(last_sym)
          else:
              result.append(last_sym + str(count))

      	  # начнаем запоминать новый символ
          count = 1
          last_sym = sym

      else:  # символ просто повторился
          count += 1  # ну ок, запомнили что символ видели на 1 раз больше

  return ''.join(result)
