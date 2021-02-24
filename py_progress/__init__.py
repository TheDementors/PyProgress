import shutil


def progressbar(
    current_index, total_index, left_description=None, right_description=None
):
    """Simple progressbar function that prints an ASCII-based progressbar
    in the terminal with the additional textual description on the left and
    right-hand side. In programs where there is a long loop, this method can
    be used to print a progressbar with progress text.


    Here is a example program to use this library:

    import time
    from py_progress import progressbar

    for i in range(100):
        progressbar(i, 100, f"Loss: {i*2123}", f"Accuracy: {i*2}%")
        time.sleep(.3)

    This will return the following result
    ~/.../experiments/progress-bar-test >>> python main.py
    --> Loss: 210177 |||||||||||||||||||||||||||||||| Accuracy: 100 %

    Here the text Loss: 210177 and Accuracy: 100% is both text passed in the method.

    Args:
        current_index (float): Current progress in the task
        total_index (float): Total number of steps in the task
        left_description (str, optional): Some description to put in the left side of
            the progressbar. Defaults to None.
        right_description (str, optional): Some description to put in the right side of
            the progressbar. Defaults to None.

    Raises:
        ValueError: If the input validation failed, then it throws the error
    """
    if not isinstance(current_index, int) and current_index < 0:
        raise ValueError(
            "The parameter current_index is not valid, please provide a value that is\
greater than -1"
        )

    if not isinstance(total_index, int) and total_index < 1:
        raise ValueError(
            "The parameter total_index is not valid, please provide a value that is\
greater than 0"
        )

    if left_description and not isinstance(left_description, str):
        raise ValueError(
            "The parameter left_description is not valid, please pass None or provide\
a string"
        )

    if right_description and not isinstance(right_description, str):
        raise ValueError(
            "The parameter right_description is not valid, please pass None or provide\
a string"
        )

    width, _ = shutil.get_terminal_size()

    if left_description:
        left_description = left_description + " "
    else:
        left_description = ""

    if right_description:
        right_description = " " + right_description
    else:
        right_description = ""

    total_index_chars = len(left_description + right_description)
    progressbar_text = ""

    if width > total_index_chars:
        percent = (width - total_index_chars) * current_index / total_index

        progressbar_text = left_description + ("|" * int(percent)) + right_description

    else:
        progressbar_text = left_description + "|" + right_description

    print("\r" + progressbar_text, end="")
