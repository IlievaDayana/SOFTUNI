def power(nums):
    num_pos = sum([int(i) for i in nums if int(i) > 0])
    num_neg = sum([int(i) for i in nums if int(i) < 0])
    if abs(num_neg) > abs(num_pos):
        print(num_neg)
        print(num_pos)
        print("The negatives are stronger than the positives")
    elif abs(num_neg) < abs(num_pos):
        print(num_pos)
        print(num_neg)
        print("The positives are stronger than the negatives")


power(input().split(" "))
