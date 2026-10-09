class MinStack:

    def __init__(self):
      self.valors = []
      self.minims = []

    def push(self, val: int) -> None:
       self.valors.append(val)

      if len(self.minims) == 0:
          self.minims.append(val)
      else:
          if val < self.minims[-1]:
              self.minims.append(val)
          else:
              self.minims.append(self.minims[-1])
      
        

    def pop(self) -> None:
      self.valors.pop()
      self.minims.pop()

    def top(self) -> int:
      return self.valors[-1]

    def getMin(self) -> int:
      return self.minims[-1]
