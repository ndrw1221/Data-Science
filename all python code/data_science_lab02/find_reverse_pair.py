def find_reverse_pair(word_list, case_sensitive = False):
    reverse_pair_list = []
    
    if not case_sensitive:
        word_list = [word.lower() for word in word_list]
    
    for word in word_list:
        if word[::-1] in word_list[word_list.index(word) + 1::]:
            reverse_pair_list.append([word, word[::-1]])
            
    return reverse_pair_list

if __name__ == '__main__':   
   import time
   time_start = time.time()

   with open(r'C:\Users\88697\Downloads\words.txt', 'r') as file:
       word_list = file.read().splitlines()
       reverse_pair_list = find_reverse_pair(word_list)

   time_end = time.time()

   print('Finish executing after', time_end - time_start, 's\n')
   print('Found', len(reverse_pair_list), 'reverse pairs\n', )
   print(reverse_pair_list)  