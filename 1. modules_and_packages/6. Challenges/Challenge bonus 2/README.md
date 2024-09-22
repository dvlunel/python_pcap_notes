# Random Fruit Picker

## Challenge

Create a function that simulates a fruit selection process by randomly picking fruits from a given list.

### Task

Create a python file called fruit_market.py and write a function named `pick_fruits` that accepts two arguments:

- `fruit_count`: the number of unique fruits to select
- `fruit_list`: a list of available fruits to choose from

The function should return a tuple with exactly two elements:

1. A list of random unique fruits selected from `fruit_list`; the number of elements should be equal to `fruit_count`.
2. One random fruit from the selected list, representing the chosen fruit.

### Example

Calling `pick_fruits(3, ['apple', 'banana', 'cherry', 'date', 'elderberry'])` should generate a list of 3 random unique fruits. 
An example return value could be:

(['banana', 'cherry', 'apple']')
