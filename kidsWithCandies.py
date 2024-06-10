def kidsWithCandies(self, candies, extraCandies):
        max_candy=max(candies)
        return [num + extraCandies >= max_candy for num in candies ]