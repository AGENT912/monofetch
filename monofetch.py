DEBIAN="""

        ***********
     *******************
   ******          ******
  *****              *****
 *****       ****     ****
*****     *****        ***
 ***      ***          ***
 ***      ***        *****
 ***      ****   ******
 ****       ********
 ****
  *****
   *****
     *****
       ******
         ******
             *****

"""

FEDORA="""

            *************
           **********************
          ***************************
         ********************************
        ************** ********* ********
       ************* *********** ********
      ************* **** * **** *********
     ************* **** ** **** *********
    ************* **** *** **** *********
   ******* *************** **************
  ****** ****************** *************
 ***** **** **** ***** ******************
***** ***** **** ***** ****************
***** **** **** **** ****************
 ******* ********* **************
  ********* *** *************
   **************************


"""

ARCH="""
                  **
                 ****
                ******
               ********
              **********
             ************
            **************
           ****************
          ******************
         ********************
        **********************
       ********       *********
      *********       **********
     **********       ***********
    ***********       ************
   ************       *************
  **                              **

"""

KALI="""

**************
            **********
          **************
**********************
           ***************
      ******            ***********
   ****               *************
 **                  ***           ******
                    ***               ****
                    ****               *****
                    ***
                     ****
                       ***********
                           ***************
                                    *********
                                       ******
                                            **

                                              
"""

GENTOO="""

         *************
     ********************
   *************************
 ***************    ***********
 **************      ***********
***************     **************
 **************    *****************
  *********************************
    ********************************
       ****************************
    ******************************
  ******************************
 ****************************
*************************
*********************
*******************
 ***************
  
"""

RASPBERRY="""

        **                     **
         ***                 ***
         *****             *****
       ********         ********

       ***       ***        ***
     *******   *******    *******
       ***       ***        ***

   ***       ***      ***      ***
 *******   *******  *******  *******
   ***       ***      ***      ***

      ***       ***        ***
    *******   *******    *******
      ***       ***        ***
             
"""

UBUNTU="""

              *********    ********
           ************  ************
        ***************  ************
       *********          **********
         ****                ******  *****
  **********                       *******
 ***********                        ******
*************                        ******
************                         ******
 ***********                        *******
   *******                          ******
       ***                         *******
    ********               *****  ******
      ********           **********  ***
       ***********      ************
          ********       **********
               ***         *****
               
"""

DEEPIN="""

             ************
         ********       *****
      **********       *********
    ***********     **************
   ***********    *****          **
  **  ********   ** ** **         **
 **    *******  ** *** ** **       **
***     ****** ** ***  ** ***       **
**       *****  ****  *** ****      **
**        ****** *   ***  ****      **
***         ***********  *****      **
 **            *****   ******      **
  *****            **********     **
   ************************      **
    **********************     ***
      *******************    ****
        **************    ******
            
"""

NIXOS="""

           ****            ****         ****
             ****           ****       ****
               ****          ****     ****
          **************      ***********
          **************       ****             ****
                                ****           ****
        ****                     ****         ****
       ****                                 **********
**********                                  ***********
**********                                 ****
    ****                                  ****
   ****   ****                           ****
  ****     ****                              
 ****      ******        ************************
          **** ****      ************************
         ****   ****               ****
        ****     ****               ****
       ****       ****               ****
       
"""

PARROT="""

    ****
 *****************
  *****************
   *****************
    *****************
     ***     **************
      **      **************
       *       **************
                **************
                 **************
                 ********  ****
                  *******   ****
                   *******    ***
                    *******    **
                    ********     *
                    ***   ***
                     ***   ***
                      **    
                      
"""

LINUX="""

        *****
       *******
      ** * * **
       *******
     ***********
   *** ******* ***
  **** ******* ****
  **** ******* ****
  ****************
***** *********** *****
**** ************* ****
  *** ***********  ***

"""

SYSWAY = ("/etc/os-release")
with open(SYSWAY, "r", encoding="utf-8") as f:
    SYSINFO = f.read().rstrip()
def SEARCHID(SYSWAY):
    with open(SYSWAY, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if line.startswith("ID="):
                return line_number
    return None

DISTROIDNUMBER = SEARCHID(SYSWAY)
DISTROIDNUMBER=int(DISTROIDNUMBER)
DISTROIDNUMBER = DISTROIDNUMBER - 1

with open(SYSWAY, 'r', encoding='utf-8') as f:
    LINES = f.readlines()
    LINE = LINES[DISTROIDNUMBER].strip()

def fread(path, mode='r'):
    try:
        f = open(path, mode)
        data = f.read()
        f.close()
        return data
    except:
        return None
environ_data = fread('/proc/self/environ', 'rb')
environ = {}
if environ_data:
    for item in environ_data.split(b'\x00'):
        if item:
            try:
                item_str = item.decode('utf-8')
            except:
                item_str = item.decode('latin-1', errors='ignore')
            if '=' in item_str:
                key, val = item_str.split('=', 1)
                environ[key] = val
de = None
if 'XDG_CURRENT_DESKTOP' in environ:
    de = environ['XDG_CURRENT_DESKTOP'].split(':')[0]
elif 'DESKTOP_SESSION' in environ:
    de = environ['DESKTOP_SESSION']
elif 'GDMSESSION' in environ:
    de = environ['GDMSESSION']
elif 'XDG_SESSION_DESKTOP' in environ:
    de = environ['XDG_SESSION_DESKTOP']
wm_names = [
    'awesome', 'i3', 'openbox', 'fluxbox', 'blackbox', 'compiz', 'metacity',
    'marco', 'muffin', 'mutter', 'kwin', 'kwin_x11', 'kwin_wayland', 'xfwm4',
    'enlightenment', 'fvwm', 'windowmaker', 'icewm', 'jwm', 'pekwm',
    'herbstluftwm', 'bspwm', 'qtile', 'dwm', 'spectrwm', 'xmonad', 'stumpwm',
    'ratpoison', 'gnome-shell', 'plasmashell', 'unity', 'sway', 'hyprland',
    'wayfire', 'river', 'labwc', 'cage', 'weston'
]
max_pid = 65535
pid_max_data = fread('/proc/sys/kernel/pid_max')
if pid_max_data:
    max_pid = int(pid_max_data.strip())
for pid in range(1, max_pid + 1):
    comm_path = f'/proc/{pid}/comm'
    comm = fread(comm_path, 'r')
    if comm:
        comm = comm.strip()
        if comm in wm_names:
            wm_found = comm
            break
        
if not wm_found:
    for pid in range(1, max_pid + 1):
        comm_path = f'/proc/{pid}/comm'
        comm = fread(comm_path, 'r')
        if comm:
            comm = comm.strip()
            for wm in wm_names:
                if wm in comm:
                    wm_found = comm
                    break
            if wm_found:
                break
            
de="DE=" + de
wm_found="WM=" + wm_found

try:
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        RAWTEMP = f.read().strip()
        TEMPC = int(RAWTEMP) / 1000
        TEMPK = int(TEMPC) + 273.15
        TEMPF = int(TEMPC) * 1.8; TEMPF = int(TEMPF) + 32
        TEMPC = str(TEMPC); TEMPK = str(TEMPK); TEMPF = str(TEMPF)
        TEMP=("TEMPERATURE = °C " + TEMPC + "; °K " + TEMPK + "; °F " + TEMPF)
except FileNotFoundError:
    TEMP=("Can't find temperature")
except PermissionError:
    TEMP=("Can't find temperature")
    
try:
    with open('/sys/class/power_supply/BAT0/capacity', 'r') as f:
        BPRECENT = str(f.read().strip()); BPRECENT = BPRECENT + "%"
except FileNotFoundError:
    BPRECENT=("Unknown")
except PermissionError:
    BPRECENT=("Unknown")
    
try:
    with open('/sys/class/power_supply/BAT0/status', 'r') as f:
        BSTATUS = str(f.read().strip())
except FileNotFoundError:
    BSTATUS=("Unknown")
except PermissionError:
    BSTATUS=("Unknown")
    
BATTERY=(BPRECENT, BSTATUS)
BATTERY=str(BATTERY)
FIX=str.maketrans("", "", "()',")
BATTERY=BATTERY.translate(FIX)
BATTERY=str(BATTERY)
BSTATUS = " (" + BSTATUS + ")"
BATTERY=BPRECENT + BSTATUS
BATTERY="BATTERY = " + BATTERY

RED=("\033[31m")
GREEN=("\033[32m")
YELLOW=("\033[33m")
BLUE=("\033[34m")
MAGENTA=("\033[35m")
CYAN=("\033[36m")
ORANGE=("\033[93m")
RESET = ("\033[0m")

try:
    with open('/etc/rpi-issue'):
        print(RED + RASPBERRY + RESET)
        print(RED + SYSINFO + RESET)
        print(RED + de + RESET)
        print(RED + wm_found + RESET)
        print(RED + TEMP + RESET)
        print(RED + BATTERY + RESET)
except FileNotFoundError:
    if LINE == "ID=debian":
        print(RED + DEBIAN + RESET)
        print(RED + SYSINFO + RESET)
        print(RED + de + RESET)
        print(RED + wm_found + RESET)
        print(RED + TEMP + RESET)
        print(RED + BATTERY + RESET)
    
    elif LINE == "ID=fedora":
        print(CYAN + FEDORA + RESET)
        print(CYAN + SYSINFO + RESET)
        print(CYAN + de + RESET)
        print(CYAN + wm_found + RESET)
        print(CYAN + TEMP + RESET)
        print(CYAN + BATTERY + RESET)
    
    elif LINE == "ID=arch":
        print(BLUE + ARCH + RESET)
        print(BLUE + SYSINFO + RESET)
        print(BLUE + de + RESET)
        print(BLUE + wm_found + RESET)
        print(BLUE + TEMP + RESET)
        print(BLUE + BATTERY + RESET)
    
    elif LINE == "ID=kali":
        print(BLUE + KALI + RESET)
        print(BLUE + SYSINFO + RESET)
        print(BLUE + de + RESET)
        print(BLUE + wm_found + RESET)
        print(BLUE + TEMP + RESET)
        print(BLUE + BATTERY + RESET)
    
    elif LINE == "ID=gentoo":
        print(MAGENTA + GENTOO + RESET)
        print(MAGENTA + SYSINFO + RESET)
        print(MAGENTA + de + RESET)
        print(MAGENTA + wm_found + RESET)
        print(MAGENTA + TEMP + RESET)
        print(MAGENTA + BATTERY + RESET)
        
    elif LINE == "ID=ubuntu":
        print(ORANGE + UBUNTU + RESET)
        print(ORANGE + SYSINFO + RESET)
        print(ORANGE + de + RESET)
        print(ORANGE + wm_found + RESET)
        print(ORANGE + TEMP + RESET)
        print(ORANGE + BATTERY + RESET)
        
    elif LINE == "ID=deepin":
        print(CYAN + DEEPIN + RESET)
        print(CYAN + SYSINFO + RESET)
        print(CYAN + de + RESET)
        print(CYAN + wm_found + RESET)
        print(CYAN + TEMP + RESET)
        print(CYAN + BATTERY + RESET)
        
    elif LINE == "ID=nixos":
        print(BLUE + NIXOS + RESET)
        print(BLUE + SYSINFO + RESET)
        print(BLUE + de + RESET)
        print(BLUE + wm_found + RESET)
        print(BLUE + TEMP + RESET)
        print(BLUE + BATTERY + RESET)
        
    elif LINE == "ID=parrot":
        print(CYAN + PARROT + RESET)
        print(CYAN + SYSINFO + RESET)
        print(CYAN + de + RESET)
        print(CYAN + wm_found + RESET)
        print(CYAN + TEMP + RESET)
        print(CYAN + BATTERY + RESET)
    
    else:
        print(YELLOW + LINUX + RESET)
        print(YELLOW + SYSINFO + RESET)
        print(YELLOW + de + RESET)
        print(YELLOW + wm_found + RESET)
        print(YELLOW + TEMP + RESET)
        print(YELLOW + BATTERY + RESET)
