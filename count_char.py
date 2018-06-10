def count_characters():
     count_dict = {}
     string = input("Input a character:")
     for c in string:
         if c in count_dict:
             count_dict[c] += 1
         else:
             count_dict[c] = 1

     print(count_dict)

count_characters()


from collections import Counter

print(Counter(input("Input a char:")))
