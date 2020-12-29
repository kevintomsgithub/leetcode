def meeting_planner(slotsA, slotsB, dur):
  '''
  input:  slotsA = [[10, 50], [60, 120], [140, 210]]
          slotsB = [[0, 15], [60, 70]]
          dur = 8

  input:  slotsA = [[10, 50], [60, 120], [140, 210]]
          slotsB = [[0, 15], [60, 70]]
          dur = 12
          15 - 10 = 5
          
          [[10, 200], [300, 320], [140, 210]]
          [[10, 50], [60, 120], [140, 200]]
          [10 ..... 60. ..... 120 .... 200]
                     ^         ^ 
                     +12
                     [60, 72]
                        i        j
          
  '''
  a_len = len(slotsA)
  b_len = len(slotsB)
  i = 0; j=0
  while i < a_len and j < b_len:
    end_time = min(slotsA[i][1], slotsB[j][1])
    start_time = max(slotsA[i][0], slotsB[j][0])
    if end_time - start_time >= dur:
      return [start_time, start_time+dur]
    else:
      if slotsA[i][1] > slotsB[j][1]:
        j += 1
      else: i += 1
  return []

'''
time : O(n+m)
space : O(1)
'''