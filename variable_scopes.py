def print_s():
  ##########################
  ### START OF YOUR CODE ###
  ##########################


  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  print(s)

  s = "Inside"

  print(s)
  
def increment_printer(start = 0):
  i = start

  def increment():
    ##########################
    ### START OF YOUR CODE ###
    ##########################


    ##########################
    ###  END OF YOUR CODE  ###
    ##########################
    i += 1
    print(i)

  return increment

if __name__ == "__main__":
  s = "1"
  print_s()

  s = "2"
  print_s()

  print("=========")
  printer = increment_printer(0)
  for i in range(5):
    printer()