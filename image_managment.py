import colors
import json

#Important Variables
debug = False
valid_filetypes = ["img", "iso"]

with open('data/distrolist.json', 'r') as f:
  distro_list = json.load(f)["Distros"]

def list_downloadables():
    print(colors.red("distribution links are not gaurenteed to always be up to date."))
    print(colors.green("Select your distribution by number."))
    print(colors.green("Distributions marked by a green check represent an available torrent which I recommend using."))
    print(colors.green("---name--------------------------------torrent-----------------------------------------------"))

    list_count = 1
    for distros in distro_list:
        hasTorrent = colors.green("✓") if distro_list[distros]['hasTorrent'] else colors.red("✗")
        print(str(list_count) + ". " + colors.blue(distro_list[distros]['DisplayName'] + "\t\t\t\t[" + hasTorrent + colors.blue("]")))
        list_count+= 1
        
    selection = str(input(colors.cyan("Selection (1, 2, etc.): ")))
    if distro_list[selection]['hasTorrent']:
        if ask_to_torrent():
            http_download_file(distro_list[selection]['torrentURL'], distro_list[selection]['fileName'] + ".torrent")
            print(colors.green("Finished Downloading! Open this file in your torrent program, and select the file at the main menu when finished."))
        else:
            http_download_file(distro_list[selection]['imageURL'], distro_list[selection]['fileName'] + ".iso")
    else:
        http_download_file(distro_list[selection]['imageURL'], distro_list[selection]['fileName'] + ".iso")
    
def ask_to_torrent():
    print(colors.green("\nThere is a torrent available for this distribution. If you have a bittorrent client, I recommend using the torrent file this program will download if you want."))
    print(colors.green("Torrenting the distribution can relieve server load, and give better download times."))
    print(colors.green("If you want to torrent, enter Y. If not, enter N and we will download via HTTPS."))
    selection = str(input(colors.cyan("Selection (y/n): ")))
    if selection == "y" or selection == "Y":
        return True
    else:
        return False

def http_download_file(url, filename):
    #I pray for the kind souls at Stack Overflow 🙏
    import functools
    import pathlib
    import shutil
    import requests
    from tqdm.auto import tqdm
    
    r = requests.get(url, stream=True, allow_redirects=True)
    if r.status_code != 200: # Executes if an error occurs while attempting to download a file !!
        r.raise_for_status()
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}") #Intentionaly raises error
    file_size = int(r.headers.get('Content-Length', 0))
    
    path = pathlib.Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

     
    if debug:
        print(str(file_size))
        print(str(path))
        
    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = functools.partial(r.raw.read, decode_content=True)  # Decompress if needed
    with tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            shutil.copyfileobj(r_raw, f)

    return path

def select_local_image():
    # !- WARNING MESSAGE
    print(colors.red("THIS PROGRAM WILL NOT CHECK IF THE IMAGE IS BROKEN! Please verify your file's integrity!"))
    print(colors.blue("This Program will NOT PROPERLY flash a Windows Installer due to FAT limits. Please make sure your file is compatabile."))
    
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return path
    
def check_if_image_compatible(path):
    file_ext = path[len(path) - 3:len(path)]
    valid_file = False
    
    for filetypes in valid_filetypes:
        if filetypes == file_ext:
            valid_file = True
            break
        
    if valid_file:
        return colors.green("File is valid!")
    else:
        raise Exception("Image Type not compatible")
        
#http_download_image("https://mirrors.acm.wpi.edu/archlinux/iso/2023.10.14/archlinux-2023.10.14-x86_64.iso", "arch.iso")
# try:
#     #print(check_if_image_compatible(select_local_image()))
    
# except:
#     print(colors.red("Whoops, An error occured! Please check your log files to resolve the issue!"))