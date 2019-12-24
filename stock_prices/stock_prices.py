#!/usr/bin/python

import argparse

"""
1) INPUT: [] list (stock prices)
2) output: Max profit integer (max diff from two list items, buy always must subtract an item that come before it in list )
3)  keep track of curr_minbuy & curr_maxsell 


[1050, 270, 1540, 3800, 2]

-loop through use curr_buy - curr_sell => store in result => find max number in result list = return max 
"""


def find_max_profit(prices):
    results = []
    for i in range(0, len(prices)):

        curr_buy = prices[i]
        print("current buy:", curr_buy)
        for j in range(0, len(prices)):
            if i > j:
                curr_sell = prices[j]
                print("curr sell:", curr_sell, "curr buy:", curr_buy)
                results.append(curr_buy-curr_sell)
                print("results:", results)
    print(results)
    maxprofit = max(results)
    return maxprofit


print(find_max_profit([1050, 270, 1540, 3800, 2]))

"""

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  """
