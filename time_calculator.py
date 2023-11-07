def add_time(start, duration, new_day=None):
  day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#  print(day_of_week)
  start_parts = start.split()
  s_time = start_parts[0]
  am_pm = start_parts[1]
  am_and_pm_flip = {'AM': 'PM', 'PM': 'AM'}
#  print('Start time:', s_time)
#  print("AM/PM:", am_pm)
  duration_parts = duration.split()
  d_time = duration_parts[0]
#  print("Duration time:", d_time)  
  s_hr, s_min = map(int, s_time.split(':'))
  d_hr, d_min = map(int, d_time.split(':'))
#  print('Hrs AND Mins:', s_hr, s_min, d_hr, d_min)
  day = int(d_hr / 24)
#  print('d_day:',day)
  min = s_min + d_min
  if min >= 60:
    s_hr += 1
    min = min % 60
#  print('Final minutes:', min)
  hr = (s_hr + d_hr) % 12
#  print('Final hours:', hr)
  min = str(min) if min > 9 else '0' + str(min)
#  print('format min', min)
  hr = 12 if hr == 0 else str(hr) 
#  print('fomate hr', hr)
  am_pm_flip = int((s_hr + d_hr) / 12)
#  print('flip', am_pm_flip)
  if am_pm == 'PM' and s_hr + (d_hr % 12) >= 12:
    day += 1
  am_pm = am_and_pm_flip[am_pm] if am_pm_flip % 2 == 1 else am_pm
#  print('Final am_pm', am_pm)
  return_time = str(hr) + ':' + min + ' ' + am_pm
#  print('final time zone is here', return_time)
  if new_day:
    new_day =  day_of_week[(day_of_week.index(new_day.capitalize()) + day) % 7]
#    print('day of week', new_day)
    return_time += ', ' + new_day
  if day == 1:
    return return_time + ' (next day)'
  elif day > 1:
    return return_time + ' (' + str(day) + ' days later)'
  return return_time