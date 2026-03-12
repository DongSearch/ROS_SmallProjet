# Thermometer

## Object
send and receivce messages using Toptic message
## Function
- randomly generate value of humidity(float) and temperature(float)
- using keyboard it can turn on/off(int) -> for visualization

## Interface
- msg
```
float32 temp
float32 hum
int32 onoff(50 on, 0 off for visualization)
```

## Consequence
### Terminal
<img width="1812" height="714" alt="image" src="https://github.com/user-attachments/assets/c1e2187a-1236-48d3-a85b-22a1caba8b6a" />


### Node graph
<img width="850" height="531" alt="image" src="https://github.com/user-attachments/assets/97831c7b-7927-4556-a5f9-aae57993a5ee" />

### Plot
<img width="1629" height="712" alt="image" src="https://github.com/user-attachments/assets/b04986f8-1677-4525-b686-71d153360d5c" />


### Troblue Shooting
1. not working ctrl + C(not available to do exit) -> because sys.stdin.read(1) induces blocking
-> setcbreak(fd) -> it keep ctrl+c as interrupt signal
-> select(read_list, write_list, except_list, timeout) they check if there is input every 0.1s -> keep from staying in infinite read waiting
```
def getch(self):
  fd = sys.stdin.fileno()
  old_setting = termios.tcgetattr(fd)
  try: tty.setraw(fd)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN,old_setting)
return ch
```
change
```
    def getch_nonblocking(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            if select.select([sys.stdin], [], [], 0.1)[0]:
                return sys.stdin.read(1)
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
```


2. when you turn off , terminal don't display anything, but when to check plot-graph, it still generates values, not 0
- > when turning off, it put 0 to values of temp and hum  
<img width="1812" height="714" alt="image" src="https://github.com/user-attachments/assets/1b7d65e4-802f-4a83-bd9e-3b5b10b9a9dd" />

### Appendix
```
def getch(self):
  fd = sys.stdin.fileno() #load file descriptor in stdin, terminal input is taken as file in Linux
  old_setting = termios.tcgetattr(fd) # store current termial parameter
  try: tty.setraw(fd) # raw - read before enter, read after enter
    ch = sys.stdin.read(1) # infinite blocking when key input put 
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN,old_setting) # restore to termial mode
return ch
```
