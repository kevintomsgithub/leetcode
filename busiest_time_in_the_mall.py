def find_busiest_period(data):
  max_v = 0
  max_ts = data[0][0]
  local_v = 0
  local_ts = data[0][0]
  for i in data:
    if local_ts != i[0]:
      if local_v > max_v: 
        max_v = local_v
        max_ts = local_ts
      local_ts = i[0]; local_v = 0
    local_v += i[1] if i[2] == 1 else -i[1]
  return max_ts