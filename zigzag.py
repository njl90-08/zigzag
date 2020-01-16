import time, sys
indent = 0 # How many spaces to indent.
indent_negative = 20
indentIncreasing = True # Whether the indentation is increasing or not.
indentDecreasing = True

try:
    while True: # The main program loop
        print(" " * indent, end="")
        print("*********")
        print(" " * indent_negative, end="")
        print("*********")
        time.sleep(0.1) # Pause for 1/10th of a second
        
        if indentIncreasing and indentDecreasing:
            # Increase the number of spaces.
            indent = indent + 1
            indent_negative = indent_negative - 1
            if indent == 20 and indent_negative == 0:
                # Change direction:
                indentIncreasing = False
                indentDecreasing = False
            
            
        else: # Decreasing the number of spaces:
            indent = indent - 1
            indent_negative = indent_negative + 1
            if indent == 0 and indent_negative == 20:
                # Change direction:
                indentIncreasing = True
                indentDecreasing = True
                
except KeyboardInterrupt:
    sys.exit()