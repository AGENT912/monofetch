import colorama
import linecache

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
    with open('/etc/rpi-issue'):
        print(colorama.Style.BRIGHT + colorama.fore.RED + RASPBERRY)
        print(colorama.Fore.RED + SYSINFO)
        print(colorama.Fore.RED + de)
        print(colorama.Fore.RED + wm_found)
        
except (FileNotFoundError, PermissionError):
    if LINE == "ID=debian":
        print(colorama.Style.BRIGHT + colorama.Fore.RED + DEBIAN)
        print(colorama.Fore.RED + SYSINFO)
        print(colorama.Fore.RED + de)
        print(colorama.Fore.RED + wm_found)
    
    elif LINE == "ID=fedora":
        print(colorama.Style.BRIGHT + colorama.Fore.CYAN + FEDORA)
        print(colorama.Fore.CYAN + SYSINFO)
        print(colorama.Fore.CYAN + de)
        print(colorama.Fore.CYAN + wm_found)
    
    elif LINE == "ID=arch":
        print(colorama.Style.BRIGHT + colorama.Fore.RED + ARCH)
        print(colorama.Fore.RED + SYSINFO)
        print(colorama.Fore.RED + de)
        print(colorama.Fore.RED + wm_found)
    
    elif LINE == "ID=kali":
        print(colorama.Style.BRIGHT + colorama.Fore.BLUE + KALI)
        print(colorama.Fore.BLUE + SYSINFO)
        print(colorama.Fore.BLUE + de)
        print(colorama.Fore.BLUE + wm_found)
    
    elif LINE == "ID=gentoo":
        print(colorama.Style.BRIGHT + colorama.Fore.MAGENTA + GENTOO)
        print(colorama.Fore.MAGENTA + SYSINFO)
        print(colorama.Fore.MAGENTA + de)
        print(colorama.Fore.MAGENTA + wm_found)
        
    elif LINE == "ID=ubuntu":
        print(colorama.Style.BRIGHT + colorama.Fore.RED + GENTOO)
        print(colorama.Fore.RED + SYSINFO)
        print(colorama.Fore.RED + de)
        print(colorama.Fore.RED + wm_found)
    
    else:
        print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + LINUX)
        print(colorama.Fore.YELLOW + SYSINFO)
        print(colorama.Fore.YELLOW + de)
        print(colorama.Fore.YELLOW + wm_found)
