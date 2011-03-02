def get_max_widths(items, columns=()):
  maxes = {}
  for col in columns:
    maxes[col] = 0

  for i in items:
    for col in columns:
      maxes[col] = max(len(str(i[col])), maxes[col])

  return maxes
