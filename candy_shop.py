# function of min price to purchase N candies
def minPrice(candy_list, n, k):
    result = 0
    i = 0

    while n:
        result += candy_list[i]
        n = n - k
        i += 1
    return result


# # function of max price to purchase N candies
def maxPrice(candy_list, n, k):
    result = 0
    index = 0
    i = n - 1
    while i >= index:
        result += candy_list[i]

        # And get k candies  for free from  the starting
        index += k
        i -= 1
    return result


candy_list_price = [3, 2, 1, 4]
n = len(candy_list_price)
k = 2

# first sort the list of the price
candy_list_price.sort()

print(minPrice(candy_list_price, n, k))
print(maxPrice(candy_list_price, n, k))
