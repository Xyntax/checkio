# Your optional code here

# You can import some modules or create additional functions

# my solution
def checkio(data):
    L = []
    for i in range(len(data)):
        count = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                count += 1
        if count > 1:
            L.append(data[i])
    return L


# ans
def checkio2(data):
    # Your code here

    # It's main function. Don't remove this function

    # It's used for auto-testing and must return a result for check.



    data = [num for num in data if data.count(num) > 1]

    return data

# Some hints

# You can use list.count(element) method for counting.

# Create new list with non-unique elements

# Loop over original list
