# Random ways to approximate pi

Inspired by the Stand-up Maths channel, I'm gonna poke at ways to approximate
pi in various programming languages.

It's an excuse to practice different languages and compare run times.

## Algorithms

 - oddfracts: 1 - 1/3 + 1/5 - 1/7 + ... = pi / 4
 - squaresix: 1 + 1/4 + 1/9 + 1/16 + .. = pi^2 / 6

## Languages

 - Python 2.7 (I know it's deprecated, but it's installed here.)

## Performance

This is done on Ubuntu 18.04 in WSL1 with ~16GB of memory.

 - squaresix-2.7 takes 1m41s to get 3.14159264498238988139 (20M terms)
