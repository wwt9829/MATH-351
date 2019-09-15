# Havel-Hakimi Theorem problem solver

## Usage: `python havel-hakimi.py [integers]`
- Separate integers by spaces
- Integers do not have to be sorted

## `python havel-hakimi.py 7 6 5 4 4 3 2 1`

Identifies graphable sequences of degrees

```
Performing Havel-Hakimi theorem
[1. 2. 3. 4. 4. 5. 6. 7.]
[1. 2. 3. 4. 4. 5. 6.]
[0. 1. 2. 3. 3. 4. 5.]
[0. 1. 2. 3. 3. 4.]
[0. 0. 1. 2. 2. 3.]
[0. 0. 1. 2. 2.]
[0. 0. 0. 1. 1.]
[0. 0. 0. 1.]
[0. 0. 0. 0.]
Obviously graphable
```

## `python havel-hakimi.py 4 4 3 2 1 0`

Identifies non-graphable sequences of degrees by:
- Negative degrees occurring
- Leading degree is greater than the length of the rest of the array

```
Performing Havel-Hakimi theorem
[0. 1. 2. 3. 4. 4.]
[0. 1. 2. 3. 4.]
[0. 0. 1. 2. 3.]
[0. 0. 1. 2.]
[-1.  0.  0.  1.]
Not graphable: a degree cannot be negative
```
