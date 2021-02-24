# PyProgress

Simple progressbar function that prints an ASCII-based progressbar in the terminal with the additional textual description on the left and right-hand side. In programs where there is a long loop, this method can be used to print a progressbar with progress text.

Here is an example program to use this library:

```python
import time

# Importing the module
from py_progress import progressbar

for i in range(100):
    progressbar(i, 100, f"Loss: {i*2123}", f"Accuracy: {i*2}%")
    time.sleep(.3)
```

This will return the following result
```bash
~/.../experiments/progress-bar-test >>> python main.py
--> Loss: 210177 |||||||||||||||||||||||||||||||| Accuracy: 100 %
```
Here the text Loss: 210177 and Accuracy: 100% is both texts passed in the method.

Args:
- current_index (float): Current progress in the task
- total_index (float): Total number of steps in the task
- left_description (str, optional): Some description to put on the left side of the progressbar. Defaults to None.
- right_description (str, optional): Some description to put on the right side of the progressbar. Defaults to None.

Raises:
- ValueError: If the input validation failed, then it throws the error