# easyCanFrame
 the command line tool to view signal position in CAN frame

# why I create it?
I feel vector tool chain sometimes were too heavy for me, Intel and Motorola format were little confused even for a experienced engineer, then I decide write my own.

# how to use it

- put the easyframe.exe in a folder and add the folder path to you system env variable
- in powershell or git console just call easyframe and add the optional parameter that u need
  
# optional parameters
- --flen:  the CAN frame length, default value were **8** it means it was a 8 byte len CAN frame
- --name:  the signal name you want to specify ,  default name were **signal**
- --repr:  the signal represent in the ouptput screen, default char were **A**,Attention the reresent only support a single char!!!!!!!, do not use '@'
- --start: the signal start bit , default value were **0**
- --len:   the signal length, default value were **8**
- --format: the CAN frame format, motorola(M) or intel(I),the default value were **I** 

# example
exp1
```
easyframe --start 0 --len 18

| 7 6 5 4 3 2 1 0 |
| A A A A A A A A |
| A A A A A A A A |
| . . . . . . A A |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
signal : A
```

exp2
```
easyframe --name fuckit --repr Z --start 7 --len 17 --format M
| 7 6 5 4 3 2 1 0 |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| Z Z Z Z Z Z Z Z |
| Z Z Z Z Z Z Z Z |
| Z . . . . . . . |

fuckit : Z
```

exp3
```
easyframe
| 7 6 5 4 3 2 1 0 |
| A A A A A A A A |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |

signal : A
```

exp4
```
# a 19 bytes len CAN frame
easyframe --flen 19 --start 27 --len 38
| 7 6 5 4 3 2 1 0 |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| A A A A A . . . |
| A A A A A A A A |
| A A A A A A A A |
| A A A A A A A A |
| A A A A A A A A |
| . . . . . . . A |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |

signal : A
```
exp5
```
easyframe --help
Usage: easyframe.exe [OPTIONS]

Options:
  --flen INTEGER   This field help you set the CAN frame length
  --name TEXT      This field help you set the signal name
  --repr TEXT      This field help you set the signal represent character for
                   you view
  --start INTEGER  This field help you set the signal start bit position
  --len INTEGER    This field help you set the signal length
  --format TEXT    This field help you set the frame format were intel or
                   mortorola
  --help           Show this message and exit.
```