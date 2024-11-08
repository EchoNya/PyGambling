import random

import time

numero = random.randint(1, 100)

print("Tenta la sorte, Riuscitai a vincere il jackpot? (Possibilitá di 1/100")

time.sleep(3)

print("La ruota gira...")

time.sleep(3)

print("Ci siamo quasi....")

time.sleep(4)

if numero == 1:
    print("Che colpo di fortuna!! Hai appena vinto il jackpot di 1 millione di Euro!!!")
    time.sleep(3)
    print("no stavo scherzando, non hai realmente vinto")
else:
     print("Che sfortuna :( Hai perso. Ritenta e magari vincerai")
