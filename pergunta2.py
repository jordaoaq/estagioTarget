
def pertence_fibonacci(numero):
  a, b = 0, 1
  while b < numero:
    a, b = b, a + b
  return b == numero

while True:

    num = int(input("Digite um número: "))

    if pertence_fibonacci(num):
      print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
      print(f"O número {num} não pertence à sequência de Fibonacci.")
