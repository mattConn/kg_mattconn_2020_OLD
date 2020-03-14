# kg mattconn 2020

Kargo Summer Intern Pre-assessment

Python code to check if two strings can be mapped 1-to-1 to each other.

My website: [mattconn.github.io](https://mattconn.github.io)

## Brief explanation

The idea is to map a string to another, 1-to-1.  

For strings A and B, this is possible if every char in A can be paired with exactly 1 char in B.

The best example for this kind of mapping would be a dictionary (a set of key-value pairs), where one or more keys may map to the same value, but one key may NOT map to more than one value.

Bad:
```
  a
 /
A
 \
  b
```

Good:
```
A 
 \
  a
 /
B
```

The above "Good" example maps values as depicted, but assuming position of chars in each string determines which char gets mapped to which, the mapping would really look like below:

```
A - a

B - a
```

My boolean function (in "isOneToOne.py") then checks for two conditions, in order:
1. Are both strings the same length? No char can be without a partner
2. Are there duplicate chars in string A? There are no duplicate keys allowed

The return value from this function will indicate whether or not two strings can be mapped to each other 1-to-1.
