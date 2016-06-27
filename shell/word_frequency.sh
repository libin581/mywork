#! /bin/bash

sed 's/ /\n/g' "$@"|      # convert to one word per line
tr A-Z a-z|               # map uppercase to lower case
sed "s/[^a-z']//g"|       # remove all characters except a-z and '  
egrep -v '^$'|            # remove empty lines
sort|                     # place words in alphabetical order
uniq -c|                  # use uniq to count how many times each word occurs
sort -n                   # order words in frequency of occurrance
