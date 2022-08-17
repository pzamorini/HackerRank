# the objective is to show as the output the maximum number of consecutive 1's
# after convert numbers to binary
if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    max_count = 0


    while n > 0:
        bi_number = n % 2
    # the binary's numbers are calculated dividing by 2 and the rest
    # determines if it is a 0 or a 1
        if bi_number == 1:
                count += 1
                if count > max_count:
                        max_count = count
        else:
            count = 0 
        n = n//2            
        # here i'm saying : if the rest it is 1, add 1 on the count
        # and if the count is larger than de max count, so it is the large count

    print(max_count)
        


