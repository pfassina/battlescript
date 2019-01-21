# battlescript

Creates a dominions map file to be used with [DasTactic's Arena Map](https://steamcommunity.com/sharedfiles/filedetails/?id=1404827698&searchtext=arena)
Takes as input a python dictionary of 2 armies, and updates the map file with pre-defined units for each nation.
As it is stands, you can use battlescript to define the commanders for each nation with the desired magic paths and units under their command.

## How to Run battlescript

```python main.py dictionary```

The script will create a ```Arena.map``` file on the current work directory.
You can replace Das's original map file with the one generated by this script.
Games created with this new map file will have nations with armies predefined by this script.


## Dictionary Format

```
dict = [
    {
        'id': '# Nation Id',
        'province': '# Province Number',
        'commanders': [
            ('# Commander Id', ['#PathLevel', ...], [('#Unit Id', 'Quantity'), ...]),
            ...
        ]
    },
    {
        'id': '# Nation Id',
        'province': '# Province Number',
        'commanders': [
            ('# Commander Id', ['#PathLevel', ...], [('#Unit Id', 'Quantity'), ...]),
            ...
        ]
    },
]
```

## Real Example

```
dict = [
    {
        'id': 74,
        'province': 12,
        'commanders': [
            (333, ['E1', 'S1', 'H2'], []),
            (333, ['S2', 'H2'], [(337, 60)]),
            (333, ['S2', 'H2'], [(337, 59)]),
            (333, ['E1', 'S1', 'H2'], [(337, 20)]),
            (1518, ['W3', 'S1'], []),
            (1518, ['W2', 'S2'], []),
            (1518, ['W2', 'E1', 'S1'], []),
            (1518, ['W2', 'S1', 'N1'], []),
            (1518, ['W2', 'S1', 'N1'], []),
            (443, ['S1'], [])
        ]
    },
    {
        'id': 44,
        'province': 5,
        'commanders': [
            (258, [], [(197, 122), (1657, 37)]),
            (260, [], [(198, 118)]),
            (188, [], [(197, 53), (259, 23)]),
            (188, [], [(184, 29), (189, 12), (186, 29)]),
            (188, [], [(187, 45), (186, 35)]),
            (188, [], [(1658, 46), (186, 34)]),
            (240, [], []),
            (240, [], []),
            (240, [], []),
            (240, [], []),
            (240, [], []),
            (240, [], [])
        ]
    }
]
```

## Coming soon
- ability to add items to commanders


