#In this problem we have a list of stock prices and we have to buy a stock at a price when its price is lower and then sell it so we would get maximum profit.
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=float('inf')

        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                max_profit=price-min_price

        return max_profit
    
sol=Solution()
prices=[2,1,5,7,6]
res=sol.maxProfit(prices)
print(res)
                
            
#The output here we get is 6 so basically we buy the stock when the price is 1 and sell it when it becomes 7 and gain aprofit of 6.      
            

    

        
            
        
        

        
        
        