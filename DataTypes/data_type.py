ef data_type(val):
  if val is None:
    results = "no value"
  elif isinstance(val, str):
    results = len(val)
  elif isinstance(val, bool):
    results = val

  elif isinstance(val, int):
    if val < 100:
      results = "less than 100"
    if val == 100:
      results = "eaqual to 100"
    elif val > 100:
      results = "more than 100"
  elif isinstance(val, list):
    results = val[2] if len(val) > 2 else None


  return results  
