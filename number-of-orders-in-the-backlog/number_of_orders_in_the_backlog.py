import heapq
from typing import List


class Solution:
    def get_number_of_backlog_orders(self, orders: List[List[int]]) -> int:
        sell_backlog = []
        buy_backlog = []
        for price, amount, order_type in orders:
            if order_type == 0:
                while amount > 0:
                    if sell_backlog and sell_backlog[0][0] <= price:
                        sell_price, sell_amount = heapq.heappop(sell_backlog)
                        if sell_amount > amount:
                            heapq.heappush(sell_backlog,
                                           (sell_price, sell_amount - amount))
                            amount = 0
                        else:
                            amount -= sell_amount
                    else:
                        heapq.heappush(buy_backlog, (-price, amount))
                        amount = 0
            else:
                while amount > 0:
                    if buy_backlog and -buy_backlog[0][0] >= price:
                        buy_price, buy_amount = heapq.heappop(buy_backlog)
                        if buy_amount > amount:
                            heapq.heappush(buy_backlog,
                                           (buy_price, buy_amount - amount))
                            amount = 0
                        else:
                            amount -= buy_amount
                    else:
                        heapq.heappush(sell_backlog, (price, amount))
                        amount = 0
        result = 0
        for _, amount in sell_backlog:
            result += amount
        for _, amount in buy_backlog:
            result += amount
        return result % (10**9 + 7)
