# Debug Quiz: Session 01 Foundations

## Question 1
There are two errors. Fix the function so it correctly counts items in a list.

Broken:
```python
def my_len(data)
    count = 0
    for item in data:
        count =+ 1
    return count
```

Fixed:
```python
def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count
```

Type: debug
Hint: Start at line 1, then check the counter update on line 4.
Explanation: Function definitions need `:`, and `count += 1` increments the counter correctly.

## Question 2
There are two errors. Fix the script to print all valid indexes.

Broken:
```python
data = [10, 20, 30, 40]

for i in range(len(data) + 1):
    print(data[i
```

Fixed:
```python
data = [10, 20, 30, 40]

for i in range(len(data)):
    print(data[i])
```

Type: debug
Hint: Look at the loop bound first, then check the print line punctuation.
Explanation: `range(len(data) + 1)` goes out of bounds; also `print` is missing a closing parenthesis.

## Question 3
There is one logic error. Fix the script so it safely handles an empty list when computing the average.

Broken:
```python
# The list can have any number of values, from empty ("No data") to hundreds.

data = [10,20,30]

total,count = 0,0

for x in data:
    total += x
    count += 1

print(total / count)
```

Fixed:
```python
data = [10,20,30]

total,count = 0,0

for x in data:
    total += x
    count += 1

if count != 0:
    print(total / count)
else:
    print("No data")
```

Type: debug
Hint: Check what happens if the list is empty before dividing by `count`.
Explanation: Dividing by `count` is unsafe when `count == 0`; add a guard so empty input prints a safe message.
