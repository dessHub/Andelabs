def fizz_buzz(val):

  if (val%3 == 0) and (val%5 == 0):
    results = "FizzBuzz"
  elif val%3 == 0 :
    results = "Fizz"
  elif val%5 == 0:
    results = "Buzz"
  else :
    results = val

  return results
