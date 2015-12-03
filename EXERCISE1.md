# Exercise 1
Build the `landsat_helpers` module with a `get_scene_details`
function that will return a dictionary containing the path, row,
and year of a Landsat 8 scene based on its SceneID.

Example:

* Input: LC81160462015249LGN00
* Output: {'path': '116', 'year': '2015', 'day': '249', 'row': '046'}

Run `exer1.py` to confirm that your module is correct. More details
inside `exer1.py`

=========================================================================

## Hint 1

Landsat SceneID's follow this the form **LXSPPPRRRYYYYDDDGSIVV**
and is segmented as follows:

```
L = Landsat
X = Sensor
S = Satellite
PPP = WRS path
RRR = WRS row
YYYY = Year
DDD = Julian day of year
GSI = Ground station identifier
VV = Archive version number
```

## Hint 2

Strings can also be sliced just like list using the [:] notation

Example.
```
>>> s = "This is a long string"
>>> print s[5:7]
>>> 'is'
```
