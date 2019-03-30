# Engine2D

This is a simple game engine built on top of pygame.

This is a private project and in early stage

### Engine2D class

#### Constructor

`__init__(self, width = 600, height = 600, bgColor = (0,0,0))`

`width`   = width of the game window
`height`  = height of the game window
`bgColor` = background color

When calling `Engine()` everything will be set up automatically

#### Functions

`setWindowTitle(self, title = "Engine2D - A Pygame Engine")`

With this function you can set the window title

`fillScreen(self, color=(0,0,0))`

Fill the screen with a colour

`drawPoint(self, point = Point(), color = (255, 255, 255), radius=1)`

Draws a point, you can set the position, color and radius

`drawLine(self, line = Line(), color = (255, 255, 255))`

Draws a line, you can set the position of the line and modify the color

### Point class

#### Contructor

`__init__(self, x = 0, y = 0)`

Constructor for a point. If no values for x or y are given, they are 0.

#### Classmethods

`fromList(self, l = []) -> List[]`

This function parses a list into a Point object and returns that

#### Functions

`toList() -> List[]`

Converts the Point object into a List.

`printPosition()`

Prints the current position of the point. Format: `(x/y)`

### Line class

#### Contructor

`__init__(self, p0 = Point(0,0), p1 = Point(100, 100), direction=None)`

`p0` is a required variable.
You can use either `p1` or `direction` as the second point of the line.
`p1` is the point with the coordinates relative to the global coordinates 
`direction` is the point with the coordinations relative to `p0` 

#### Classmethods

`fromLists(self, p0 = [0,0], p1 = [], direction = []) -> List[]`

`p0` is required and either `p1` or `direction` (look: Constructor)
This function parses two lists into the Line object and returns that

#### Functions

`getMissingValue(self)`

Calculates either the missing `p1` or `direction` variable inside the class

`getLength(self)`

Get length of the vector (line)