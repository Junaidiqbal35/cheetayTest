def activitySelection(arr, n):
    selected = []
    arr.sort(key=lambda x: x[1])
    i = 0
    selected.append(arr[i])

    for j in range(n):
        if arr[j][0] > arr[i][1]:
            selected.append(arr[j])
            i = j
    print("selected Activities are ", end=' ')
    print(selected)

    return len(selected)


start = [1, 3, 2, 5]
end = [2, 4, 3, 6]

# merging two list together by using zip method
Activity = zip(start, end)
activities = list(Activity)
n = len(activities)
selected = activitySelection(activities, n)
print("Total activities are selected :")
print(selected)
