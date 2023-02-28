name = 'Color Compiler'
version = 'FINAL'

from tkinter import Tk #Prerequisite for the file explorer
from tkinter.filedialog import askopenfilename #Used to get image through file explorer
from time import sleep

try:
    from PIL import Image, ImageFilter, ImageOps, ImageEnhance #pip install pillow
except ModuleNotFoundError:
    print("")
    print("Pillow may not installed - type: 'pip install pillow' into command prompt")
    quit()
try:
    import pyautogui #pip install pyautogui
except ModuleNotFoundError:
    print("")
    print("PyAutoGUI may not installed - type: 'pip install pyautogui' into command prompt")
    quit()
try:
    import win32api, win32con, win32gui #pip install pywin32
except ModuleNotFoundError:
    print("")
    print("Win32API may not installed - type: 'pip install pywin32' into command prompt")
    quit()
try:
    import pyperclip as pc #pip install pyperclip
except ModuleNotFoundError:
    print("")
    print("PyperClip may not installed - type: 'pip install pyperclip' into command prompt")
    quit()

Sx, Sy = pyautogui.size()
if (Sy%Sx == Sy): #Add support for printing with 21:9 and 4:3
    pass
else:
    print("Screen ratio not supported - only 16:9 is supported")
    print("   Get the coordinates of the buttons and insert them manualy into the variables in the code")
    quit()
text = (int(0.7*Sx), int(0.63*Sy)) #Calculation for color text box
symbols = ['!','','','#','','','$','','','%','','','&','','','(','','',')','','','*','','','+','','',',','','',
'.','','','/','','',':','','',';','','','<','','','=','','','>','','','?','','','@','','','[','','','Ñ','','',']','','',
'^','','','_','','','{','','','|','','','}','','','~','','','¢','','','£','','','¤','','','¥','','','¦','','','§','','',
'¨','','','©','','','ª','','','«','','','¬','','','Ö','','','®','','','¯','','','°','','','±','','','²','','','³','','',
'´','','','µ','','','¶','','','·','','','¸','','','¹','','','º','','','»','','','¼','','','½','','','¾','','','¿','','',
'À','','','È','','','ß','','','Ä','','','ê','','','ö','','','Ø','','','Ð','','','Ý','','','ä','','','î','','','Œ','','',
'Ç','','','Ž','','','ÿ','','','Ú','','','É','','','Ê','','','Æ','','','Ë','','','Ù','','','Ü','','']

def getActiveWindow(window_title: str = "Rec Room") -> bool: #From Reny
    if window_title not in (pyautogui.getActiveWindowTitle() or ""): #If Rec Room is not the main window
        print("Waiting for Rec Room to be the active window... ")
        while window_title not in (pyautogui.getActiveWindowTitle() or ""): #While Rec Room is not main window
            sleep(0.1)
        sleep(0.5)
    return(True)

def rgbToHex(rgb): #Converts RBG to hex
    return('#%02x%02x%02x' % rgb) #Converts the RGB values to hex

def hexToRGB(hex): #Converts hex to RGB
    hex = str(hex)
    hex = hex.replace('#','')
    return(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))

def printBreak(number): #Prints a break (multiple blank lines for clarity)
    for i in range(number): #Loop to print the specified number of times
        print("")

def hexinsert(list,delay): #Inserts hex colors into Rec Room
    getActiveWindow()
    sleep(1)
    win32api.SetCursorPos((0,0))
    xxx = 167
    yyy = 324
    custom_x = 1389
    custom_y = 877
    cfield_x = 1341
    cfield_y = 671
    done_x = 1357
    done_y = 775
    for i in enumerate(list):
        (index,string) = i
        getActiveWindow()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleep(delay)
        win32api.SetCursorPos((xxx,yyy))
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleep(delay)
        pc.copy(string)
        sleep(delay)
        win32api.SetCursorPos((custom_x,custom_y))
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleep(delay)
        win32api.SetCursorPos((cfield_x,cfield_y))
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleep(delay)
        pyautogui.hotkey('ctrl','v')
        sleep(delay)
        win32api.SetCursorPos((done_x,done_y))
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        sleep(delay)
        pyautogui.keyDown('f')
        pyautogui.keyUp('f')
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        sleep(delay)

def dilate(cycles, image):
    for i in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
        return image

def erode(cycles, image):
    for i in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
        return image

print("")
Tk().withdraw() #Keeps the root window closed
print(str(name) + " " + str(version))
print("   'i' to input a color file")
print("   'c' to compile colors")
selection = str(input("Enter value: "))
if (selection == 'c'):
    print("  Select image file to compile")
elif (selection == 'i'):
    print("  Select text file to import")
    strings = askopenfilename() #Opens file explorer
    strings = open(strings, "r")
    try: #File error detection
        try:
            segments = strings.readlines()
        except:
            print("")
            print("Invalid file type - only use text files")
            print("")
            quit()
    except AttributeError: #Error when you close the window
        print("Error - file window closed")
        print("")
        quit()
    print("")
    print("File found.")
    print("")
    print("Colors obtained, " + str(len(segments)) + " colors found.")
    print("")
    delay = float(input("Enter import delay in seconds from 0 to 1 second: "))
    print("Delay set to " + str(delay) + " seconds")
    print("")
    print("  Import will being three seconds after you press enter and will check if 'Rec Room' is the active window")
    input("Press enter to start the import process: ")
    sleep(3)
    hexinsert(segments,delay)
    print("")
    quit()
else:
    print("Enter valid option")
    print("")
    quit()

fileName = askopenfilename() #Opens file explorer
try: #File error detection
    try:
        img = Image.open(fileName) #Gets image in program
    except:
        print("")
        print("Invalid image type - only use PNG, JPEG, or JFIF")
        print("")
        quit()
except AttributeError: #Error when you close the window
    print("Error - file window closed")
    print("")
    quit()

img = img.convert('RGB')
FileName = str(fileName)
FileName = FileName.split('/')
FileName = FileName[len(FileName)-1]
try:
    FileName = FileName.replace('.png','')
except:
    try:
        FileName = FileName.replace('.jpg','')
    except:
        try:
            FileName = FileName.replace('.jfif','')
        except:
            try:
                FileName = FileName.replace('.jpeg','')
            except:
                pass
print("   'c' to compile colors")
print("   'e' to edit image")
choice = str(input("Enter value: "))
if (choice == 'c'):
    pass
elif (choice == 'e'):
        editList = []
        print("")
        while('Color Compiler' != 'Amazing'):
            print("  'e' to emboss                  'i' to invert colors")
            print("  'b' to blur                    'p' to posterize")
            print("  'c' to contour image           'l' to solarize")
            print("  'g' to convert to gray-scale   'z' to resize (expands and compresses image to size)")
            print("  's' to sharpen                 'm' to smooth")
            print("  'ee' to edge enhance           'k' to remove background (special input)")
            print("  'se' to shape enhance          'f' to find edges")
            print("  'v' to flip (vertically)       'h' to mirror (horizontally)")
            print("  'w' to make black and white    'r' to rotate")
            print("  'ec' to enhance contrast       'es' to enhance sharpness")
            print("  'eb' to enhance brightnes")
            print("  'x' to skip")
            filterchoice = str(input("Enter value: "))
#Watermark, textures, paintbrush, watercolor, sepia, dither, glitch
            if (filterchoice == 'e'): #Emboss
                img = img.filter(ImageFilter.EMBOSS)
                img.show()
                editList.append("Emboss")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'eb'): #Enhance Brightness
                print("")
                print("  Standard brightness enhance factor is 1.5")
                Benhance = float(input("Enter brightness enhance factor: "))
                img = ImageEnhance.Brightness(img)
                img = img.enhance(Benhance)
                img.show()
                editList.append("Enhance Brightness")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'es'): #Enhance Sharpness
                print("")
                print("  Standard sharpness enhance factor is 5.0")
                Senhance = float(input("Enter sharpness enhance factor: "))
                img = ImageEnhance.Sharpness(img)
                img = img.enhance(Senhance)
                img.show()
                editList.append("Enhance Sharpness")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'ec'): #Enhance Contrast
                print("")
                print("  Standard contrast enhance factor is 5.0")
                Cenhance = float(input("Enter contrast enhance factor: "))
                img = ImageEnhance.Contrast(img)
                img = img.enhance(Cenhance)
                img.show()
                editList.append("Enhance Contrast")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'b'): #Blur
                print("")
                print("  'b' = box blur - blurs in a radius")
                print("  'g' = Gaussian blur")
                print("  'c' = center blur")
                blurselection = str(input("Enter a value: "))
                if (blurselection == 'b' or blurselection == 'B'):
                    Bradius = int(input("Enter box blur radius as an integer: "))
                    if (Bradius < 1):
                        print("Invalid radius")
                        break
                    else:
                        img = img.filter(ImageFilter.BoxBlur(Bradius))
                    editList.append("Box Blur")
                elif (blurselection == 'g'):
                    Gradius = int(input("Enter Gaussian blur radius as an integer: "))
                    if (Gradius < 1):
                        print("Invalid radius")
                        break
                    else:
                        img = img.filter(ImageFilter.GaussianBlur(Gradius))
                    editList.append("Gaussian Blur")
                elif (blurselection == 'c'):
                    img = img.filter(ImageFilter.BLUR)
                    editList.append("Blur")
                else:
                    print("Invalid selection")
                    break
                img.show()
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'c'): #Contour
                img = img.filter(ImageFilter.CONTOUR)
                img.show()
                editList.append("Contour")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'ee'): #Edge Enhance
                img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
                img.show()
                editList.append("Edge Enhance")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'w'): #Black and White
                img = img.convert('1')
                img.show()
                editList.append("Black/White")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'g'): #Gray-Scale
                img = img.convert('L')
                img.show()
                editList.append("Gray-Scale")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'i'): #Invert
                img = ImageOps.invert(img)
                img.show()
                editList.append("Invert")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'p'): #Posterize
                print("Color count changes depending on prior edits")
                print("   1 bit = 8 to 12 colors")
                print(   "2 bits = 40 to 60")
                print(   "3 bits = 212 to 255 colors")
                Bit = int(input("Enter amount of bits to posterize: "))
                if (Bit > 3): #Check value for validity
                    print("")
                    print("Invalid value - 3 bits is maximum")
                    print("")
                elif (Bit < 1):
                    print("")
                    print("Invalid value - 1 bit is minimum")
                    print("")
                else:
                    pass
                img = ImageOps.posterize(img, Bit)
                img.show()
                editList.append("Posterize")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'l'): #Solarize
                solar = 192 #Brightness cutoff
                img = ImageOps.solarize(img, solar)
                img.show()
                editList.append("Solarize")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'v'): #Flip
                img = ImageOps.flip(img) #Flips image from top to bottom
                img.show()
                editList.append("Flip")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'h'): #Mirror
                img = ImageOps.mirror(img) #Mirrors image from left to right
                img.show()
                editList.append("Mirror")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'z'): #Resize
                imgX, imgY = img.size
                while('Color Compiler' != 'Amazing'):
                    print("   Original image size: " + str(imgX) + " x " + str(imgY))
                    print("Enter 'sq' to fit to square canvas or 'rc' to fit to rectangular canvas")
                    sizeSelection = str(input("Enter 'c' to resize to a custom size, 's' to make square, or 'r' to make rectangle: "))
                    if (sizeSelection == 'sq'):
                        if (imgX < 1024 or imgY < 1024):
                            if (imgX < imgY):
                                size = (imgY,imgY)
                                img = img.resize(size)
                                break
                            else:
                                size = (imgX,imgX)
                                img = img.resize(size)
                                break
                        else:
                            size = (1024,1024)
                            img = img.resize(size)
                            break
                    elif (sizeSelection == 'rc'):
                        if (imgX > imgY):
                            if (imgX >= 1429 and imgY >= 1024):
                                size = (1429,1024)
                                img = img.resize(size)
                                break
                            else:
                                size = (imgX,int(imgX*(1024/1429)))
                                img = img.resize(size)
                                break
                        else:
                            if (imgY >= 1429 and imgX >= 1024):
                                size = (1024,1429)
                                img = img.resize(size)
                                break
                            else:
                                size = (int(imgY*(1429/1024)),imgY)
                                img = img.resize(size)
                                break

                    elif (sizeSelection == 'c'):
                        x = int(input("Enter new width: "))
                        if (x >= imgX):
                            print("Width greater than or equal to the original images width - enter valid width")
                        else:
                            pass
                        y = int(input("Enter new height: "))
                        if (y >= imgY):
                            print("Height greater than or equal to the original images height - enter valid height")
                        else:
                            size = (x,y)
                            img = img.resize(size)
                            break
                    elif (sizeSelection == 's'):
                        if (imgX > imgY):
                            size = (imgY,imgY)
                            img = img.resize(size)
                            break
                        else:
                            size = (imgX,imgX)
                            img = img.resize(size)
                            break
                    elif (sizeSelection == 'r'):
                        if (imgX > imgY):
                            size = (imgX,int(imgX*(1024/1429)))
                            img = img.resize(size)
                            break
                        else:
                            size = (int(imgY*(1429/1024)),imgY)
                            img = img.resize(size)
                            break
                    else:
                        print("Enter valid option")
                        print("")
                img.show()
                editList.append("Resize")
                print("")
                print(editList)
                print("")
                NimgX, NimgY = img.size
                print("New image size: " + str(NimgX) + " x " + str(NimgY))
            elif (filterchoice == 'x'): #Skip
                pass
            elif (filterchoice == 's'): #Sharpen
                img = img.filter(ImageFilter.SHARPEN)
                img.show()
                editList.append("Sharpen")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'm'): #Smooth
                print("")
                print("  's' for smooth")
                print("  'x' for extra smooth")
                smoothselection = str(input("Enter a value: "))
                if (smoothselection == 's'):
                    img = img.filter(ImageFilter.SMOOTH)
                    editList.append("Smooth")
                elif (smoothselection == 'x'):
                    img = img.filter(ImageFilter.SMOOTH_MORE)
                    editList.append("Extra Smooth")
                else:
                    print("Invalid selection")
                    break
                img.show()
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'xs'): #Shape Enhance
                img = img.filter(ImageFilter.EDGE_ENHANCE)
                img.show()
                editList.append("Shape Enhance")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'f'): #Find Edges
                img = img.filter(ImageFilter.FIND_EDGES)
                img.show()
                editList.append("Find Edges")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'k'): #Remove background
                print("")
                Threshold = int(input("Enter threshold value (30 to 80): "))
                ecycles = int(input("Enter erosion cycles (10 to 40): "))
                dcycles = int(input("Enter dialation cycles (20 to 80): "))
                eecycles = int(input("Enter second erosion cycles (15 to 60): "))
                bvalue = int(input("Enter blur value (10 to 50): "))
                blank = img.point(lambda _: 0) #Creates an identical image of the same color
                red, green, blue = img.split()
                imgThreshold = blue.point(lambda x: 255 if x > Threshold else 0)
                imgThreshold = imgThreshold.convert("1")
                mask = erode(ecycles, imgThreshold) #Erode image
                mask = dilate(dcycles, mask) #Dialate the mask
                mask = erode(eecycles, mask) #Erode the mask
                mask = mask.convert("L") #Convert mask to black and white
                mask = mask.filter(ImageFilter.BoxBlur(bvalue)) #Blur mask (smoothen it)
                img = Image.composite(img, blank, mask) #Removes background
                img.show()
                editList.append("Background Remove")
                print("")
                print(editList)
                print("")
            elif (filterchoice == 'r'): #Rotate
                print("")
                angle = float(input("Enter rotation in degrees: "))
                img = img.rotate(angle, Image.NEAREST, expand = 0)
                img.show()
                editList.append("Rotate")
                print("")
                print(editList)
                print("")
            else:
                print("")
                print("Enter valid option")
            print("   'e' to add more effects")
            print("   'c' to compile colors")
            print("   'x' to undo last effect")
            effectoption = str(input("Enter value: "))
            if (effectoption == 'e'):
                pass
            elif (effectoption == 'c'):
                break
            elif (effectoption == 'x'):
                try:
                    editList.pop() #Remove last element of list
                    editListLength = len(editList) #Get length of edit list
                    img = Image.open(fileName) #Gets new image
                    for i in range(editListLength): #Apply all edits to image
                        if (editList[i] == 'Emboss'):
                            img = img.filter(ImageFilter.EMBOSS)
                        elif (editList[i] == 'Background Remove'):
                            blank = img.point(lambda _: 0) #Creates an identical image of the same color
                            red, green, blue = img.split()
                            imgThreshold = blue.point(lambda x: 255 if x > Threshold else 0)
                            imgThreshold = imgThreshold.convert("1")
                            mask = erode(ecycles, imgThreshold) #Erode image
                            mask = dilate(dcycles, mask) #Dialate the mask
                            mask = erode(eecycles, mask) #Erode the mask
                            mask = mask.convert("L") #Convert mask to black and white
                            mask = mask.filter(ImageFilter.BoxBlur(bvalue)) #Blur mask (smoothen it)
                            img = Image.composite(img, blank, mask) #Removes background
                            img = Image.composite(img, blank, mask)
                        elif (editList[i] == 'Enhance Contrast'):
                            img = ImageEnhance.Contrast(img)
                            img = img.enhance(Cenhance)
                        elif (editList[i] == 'Enhance Brightness'):
                            img = ImageEnhance.Brightness(img)
                            img = img.enhance(Benhance)
                        elif (editList[i] == 'Enhance Sharpness'):
                            img = ImageEnhance.Sharpness(img)
                            img = img.enhance(Senhance)
                        elif (editList[i] == 'Blur'):
                            img = img.filter(ImageFilter.BLUR)
                        elif (editList[i] == 'Box Blur'):
                            img = img.filter(ImageFilter.BoxBlur(Bradius))
                        elif (editList[i] == 'Gaussian Blur'):
                            img = img.filter(ImageFilter.GaussianBlur(Gradius))
                        elif (editList[i] == 'Contour'):
                            img = img.filter(ImageFilter.CONTOUR)
                        elif (editList[i] == 'Edge Enhance'):
                            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
                        elif (editList[i] == 'Gray-Scale'):
                            img = img.convert('L')
                        elif (editList[i] == 'Invert'):
                            img = ImageOps.invert(img)
                        elif (editList[i] == 'Posterize'):
                            img = ImageOps.posterize(img, Bit)
                        elif (editList[i] == 'Solarize'):
                            img = ImageOps.solarize(img, solar)
                        elif (editList[i] == 'Resize'):
                            img.resize(size)
                        elif (editList[i] == 'Sharpen'):
                            img = img.filter(ImageFilter.SHARPEN)
                        elif (editList[i] == 'Smooth'):
                            img = img.filter(ImageFilter.SMOOTH)
                        elif (editList[i] == 'Extra Smooth'):
                            img = img.filter(ImageFilter.SMOOTH_MORE)
                        elif (editList[i] == 'Shape Enhance'):
                            img = img.filter(ImageFilter.EDGE_ENHANCE)
                        elif (editList[i] == 'Find Edges'):
                            img = img.filter(ImageFilter.FIND_EDGES)
                        elif (editList[i] == 'Flip'):
                            img = ImageOps.flip(img)
                        elif (editList[i] == 'Mirror'):
                            img = ImageOps.mirror(img)
                        elif (editList[i] == 'Black/White'):
                            img = img.convert('1')
                        elif (editList[i] == 'Rotate'):
                            img = img.rotate(angle, Image.NEAREST, expand = 0)
                    ImageX, ImageY = img.size #Gets size of image
                    print("   Image reverted one edit")
                    print(editList)
                    print("   Current image size: " + str(ImageX) + " x " + str(ImageY))
                    print("Current image shown")
                    print("")
                    img.show()
                except IndexError:
                    print("")
                    print("Edit revert failed - no edits to revert")
                    print("")
            else:
                print("")
                print("Enter valid option")
        print("")
        print("  png")
        print("  jpg")
        fileType = str(input("Enter file type to save as: "))
        if (fileType == 'png' or fileType == 'jpg'):
            pass
        else:
            print("  Invalid file type - saving as .png")
            fileType = 'png'

        imageName = FileName + "-Image." + str(fileType)
        print("Saving final image as " + str(imageName))
        print("Showing final image")
        img.show()
        img.save(imageName)
        print("")
else:
    print("Enter valid choice - try again")
    print("")
    quit()

print("  60 markers is standard - 255 is maximum")
img.load()
coloramount = int(input("Enter amount of colors: ")) #Get amount of colors - 256 is maximum
if (coloramount < 1):
    print("")
    print("Color amount too small - 1 is minmum amount")
    print("")
    quit()
elif (coloramount > 255):
    print("")
    print("Color amount too large - 255 is maximum amount")
    print("")
    quit()
else:
    pass
print("   0 = Median Cut - most CPU intensive, has best color detection")
print("   1 = Maximum Coverage - poor color detection, for special circumstances")
print("   2 = Fast Octree - fastest method, has decent color detection")
colortype = int(input("Enter type of quantization: ")) #Get amount of colors - 256 is maximum
try:
    quant = img.quantize(colors=coloramount,method=colortype) #Quantize image using 'Fast Octree' method
except ValueError:
    print("")
    print("Quantization method not recognized - enter valid integer")
    print("")
    quit()

#Method 0 is Median Cut - gets average colors, good ratio of colors to time, moderate time to quantize - Best for coloration
#Method 1 is Maximum Coverage - very few colors detected, details hard to make out, quick time to quantize - Best for special images (probably nothing you'd use in this)
#Method 2 is 'Fast Octree' - moderate amount of colors detected, details are still visible but has some noise, quickest time to quantize - Fastest

count = coloramount*3 #Color count length
palette = (quant.getpalette()[:count]) #Gets colors into a list
maximum = int(len(palette)-2) #Calculate what value to iterate until
hexcolors = [] #Create blank list to accumulate hex colors
rgbcolors = [] #Create another blank list to accumulate RGB colors
i = 0 #Initialize the iteration variable
if (coloramount > 0 and coloramount <= 80):
    for i in (range(maximum)):
        if (i%3 == 0):
            rgb = palette[i],palette[i+1],palette[i+2]
            hexcolor = str(rgbToHex(rgb))
            rgbcolors.append(str(rgb) + ': "' + str(symbols[i]) + '",')
            hexcolors.append(hexcolor)
            i += 1
        else:
            i += 1
else:
    for i in (range(maximum)):
        if (i%3 == 0):
            rgb = palette[i],palette[i+1],palette[i+2]
            hexcolor = str(rgbToHex(rgb))
            rgbcolors.append(str(rgb))
            hexcolors.append(hexcolor)
            i += 1
        else:
            i += 1
print(str(coloramount) + " colors compiled")
print("")
hexFileName = FileName + "-Hex.txt" #Format hex file name
with open(hexFileName, 'w') as file1: #Create and open blank text file to write in
    file1.write('\n'.join(hexcolors)) #Write list onto text file
RGBfileName = FileName + "-RGB.txt" #Format RGB file name
with open(RGBfileName, 'w') as file2: #Create and open blank text file to write in
    file2.write('\n'.join(rgbcolors)) #Write list onto text file
print("Text files written")
print("  Run program again to import colors")
