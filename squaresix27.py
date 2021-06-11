#! /usr/bin/env python2

"""
This file is part of the lolpi package.

lolpi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

lolpi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with lolpi.  If not, see <https://www.gnu.org/licenses/>.

Approximate pi^2/6 by adding the inverses of squares of natural numbers.
That is,

    pi^2 / 6 = (1)^-2 + (2)^-2 + (3)^-2 + .....

"""
import sys

def squaresix(limit):
    """
    Takes an integer limit and sums the inverses of squares up to this.
    Then it multiplies that number by 6 and returns the square root.
    There should be other more efficient ways to do so.
    """
    return (6 * sum([x ** -2 for x in range(1, limit + 1)])) ** 0.5

def main():
    """
    Calls the squaresix function, getting the limit from input arguments.
    """
    limit = int(sys.argv[1])
    print "Our estimate using %d terms is: \n%1.20f" % (limit, squaresix(limit))

if __name__ == "__main__":
    main()
