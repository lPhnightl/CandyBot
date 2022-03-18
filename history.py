def log(user, bot, time, result):
  file = open('stat.csv', 'a', encoding="UTF8")
  file.write(f'{user}, {bot}, {time}, {result}\n')
  file.close()