s = input().upper()
char_frequency = {}  #문자의 빈도를 딕셔너리를 활용
max_frequency = 0
max_char = ''

for char in s:
  if char in char_frequency:
    char_frequency[char] += 1  #이렇게 하면 key가 char인 값의 value를 1증
  else:
    char_frequency[char] = 1
  if char_frequency[char] > max_frequency:
    max_frequency = char_frequency[char]
    max_char = char
  #char의 빈도수와 가장 많이 있는 문자의 빈도수가 같음 그리고 문자가 가장 많은 문자와 다를때
  #즉 다른 문자인데 그 수가 동일한 경우
  elif char_frequency[char] == max_frequency and char != max_char:
    max_char = '?'
print(max_char)