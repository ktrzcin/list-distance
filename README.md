# list-distance
Simple script calculating distance between two lists as `min(|Ai - Bj|)`.

## Assumptions
1. All input values are ints
2. List A is sorted in descending manner
3. List B is sorted in ascending manner

## Input format
```
m n
A1 A2 A3 ... Am
B1 B2 B3 ... Bn
```
```
m - elements count in list A
n - elements count in list B
A1...Am - space seperated elements of list A
B1...Bn - space seperated elements of list B
```

## Usage
For following program invocation:
```console
foo@bar:~$ python3 list_distance.py
3 2
3 2 1
5 6
```
Expected output is:
```console
2
```
