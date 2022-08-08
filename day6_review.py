size_of_the_word = int(input())


for i in range(size_of_the_word):
    string = input()
    even_string = ""
    odd_string = ""

    for j in range (len(string)):
        if j % 2 == 0:
            even_string = even_string + string[j]
        else:
            odd_string = odd_string + string[j]
        
            
    print(even_string + " " + odd_string)
