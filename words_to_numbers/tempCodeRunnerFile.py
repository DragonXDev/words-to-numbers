print( ( lambda x: ( "zero" if x[0] == "0" else ( "".join( [ ( { "0": "", "1": "", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety", }[x[i]] + "-" if ((len(x) - i) == 2 or ((len(x) - i) - 2) % 3 == 0) and (x[i] != "1" and x[i] != "0") else ( { "0": "ten", "1": "eleven", "2": "twelve", "3": "thirteen", "4": "fourteen", "5": "fifteen", "6": "sixteen", "7": "seventeen", "8": "eighteen", "9": "nineteen", }[x[i]] + " " if ( ((len(x) - i) == 1 or ((len(x) - i) - 1) % 3 == 0) and (len(x) > (len(x) - i)) and x[i - 1] == "1" ) else "" ) ) + ( [ "", "hundred ", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "hextillion ", "septillion ", ][ 0 if ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i) - 4) % 3 == 0 and ( x[i] != "0" or x[i if (i - 1) < 0 else i - 1] != "0" or x[i if (i - 2) < 0 else i - 2] != "0" ) else 0 ) ) ) > 9 else ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i) - 4) % 3 == 0 and ( x[i] != "0" or x[i if (i - 1) < 0 else i - 1] != "0" or x[i if (i - 2) < 0 else i - 2] != "0" ) else 0 ) ) ) ] if ( ((len(x) - i) == 1 or ((len(x) - i) - 1) % 3 == 0) and (len(x) > (len(x) - i)) and x[i - 1] == "1" ) else ( [ "", "hundred ", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "hextillion ", "septillion ", ][ 0 if ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i) - 4) % 3 == 0 and ( x[i] != "0" or x[i if (i - 1) < 0 else i - 1] != "0" or x[i if (i - 2) < 0 else i - 2] != "0" ) else 0 ) ) ) > 9 else ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i) - 4) % 3 == 0 and ( x[i] != "0" or x[i if (i - 1) < 0 else i - 1] != "0" or x[i if (i - 2) < 0 else i - 2] != "0" ) else 0 ) ) ) ] if ((len(x) - i) == 2 or ((len(x) - i) - 2) % 3 == 0) and (x[i] != "0") else { "0": "", "1": "one ", "2": "two ", "3": "three ", "4": "four ", "5": "five ", "6": "six ", "7": "seven ", "8": "eight ", "9": "nine ", }[x[i]] + [ "", "hundred ", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "hextillion ", "septillion ", ][ 0 if ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i) - 4) % 3 == 0 and ( x[i] != "0" or x[i if (i - 1) < 0 else i - 1] != "0" or x[i if (i - 2) < 0 else i - 2] != "0" ) else 0 ) ) ) > 9 else ( 0 if (len(x) - i) == 1 else ( (0 if x[i] == "0" else 1) if (len(x) - i) % 3 == 0 else ( (((len(x) - i) - 4) // 3) + 2 if ((len(x) - i)