# given n names and phone numbers, assemble a phone book that maps friends
# names to teis respective phone numbers. You will then be given an unknown
# numbers of names to query your phone book for.
# For each name queried, print the associated entry from your book on a
# new in the form name=phoneNumber; if an entry for name is not found
# print Not found instead


#entries = int(input())
number_of_trials = int(input())
phone_book = {}

for i in range(number_of_trials):
    name, number = input().split()
    phone_book[name] = number
# here in this loop the script takes 
# the input, split and then save in two variables
# after that, the script saves in the dict created before
# as a key and value

while True:
    try:
        queries = input()
        if queries in phone_book:
            print (f'{queries}={phone_book[queries]}')
        else:
            print('Not found')
        # here the script takes an input, search in the dictionary 
        # and if the name is there, print in the terminal the querie
        # while true and the number saved before
        # in case that the number is not there will return "not found"
    except:
        break

