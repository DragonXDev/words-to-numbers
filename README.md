# Words to Numbers

## Introduction
The challenge is simple: Convert numbers into their word form, with no tricks like libraries, packages, caching, etc.

The "Words to Numbers" project is a challenging Python script that converts numbers (greater than 0) into their word form only with a single line of code. Originally aimed to produce this program in under 90 lines in Python, I refined and rewrote it over and over to achieve its final state.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributors](#contributors)
- [License](#license)

## Installation

To set up the project environment and run the script, you must have Poetry installed. If you do not have Poetry, you can install it by following the instructions [here](https://python-poetry.org/docs/).

After installing Poetry, clone this repository to your local machine:

```bash
git clone https://your-repository-url/words_to_numbers.git
cd words_to_numbers
poetry install    # No dependencies to install
```
## Usage

To run the script, use the following command:

```bash
poetry run python -m words_to_numbers
```

## Features

- **Single-Line Conversion**: The core feature of this script is its ability to convert numbers into words in a single line of Python code.
- **Expanding**: Expanding the range of the program's output is simple, just add more elements to the 3 lists each currently created as
```py
[ "", "hundred ", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "hextillion ", "septillion "]
```
and increment the number 9 found in 3 different places within the program, all in places with boilerplate:
```py
if (
    0
    if (len(x) - i) == 1
    else (
        (0 if x[i] == "0" else 1)
        if (len(x) - i) % 3 == 0
        else (
            (((len(x) - i) - 4) // 3) + 2
            if ((len(x) - i) - 4) % 3 == 0
            and (
                x[i] != "0"
                or x[i if (i - 1) < 0 else i - 1] != "0"
                or x[i if (i - 2) < 0 else i - 2] != "0"
            )
            else 0
        )
    )
) > 9:       # Update the 9 in 3 locations all with this context (expanded version)
```

## Contributors

I am the sole contributor for this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)

