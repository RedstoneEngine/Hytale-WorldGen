
import time
# This is a downloaded library using the pip installer
import pyautogui

# ---User Input---

# Instructions
defineInterpolations = [{"name": "Wave1 Slider", "value": "SlideX", "initial": 0, "speed": -0.9},
                        {"name": "Wave2 Slider", "value": "SlideX", "initial": 0, "speed": -2.4},
                        {"name": "Wave3 Slider", "value": "SlideX", "initial": 0, "speed": -1.5},
                        {"name": "Wave4 Slider", "value": "SlideX", "initial": 0, "speed": 3},
                        {"name": "WaveBreakup Slider", "value": "SlideY", "initial": 0, "speed": 0.75},
                        {"name": "OceanHeight Slider", "value": "SlideX", "initial": 0, "speed": -2},
                        {"name": "Branch Wind Slider", "value": "SlideX", "initial": 0, "speed": -5},
                        {"name": "LeafColor Slider", "value": "SlideX", "initial": 0, "speed": -0.15},
                        {"name": "_Outer Leaf Chance", "value": "Seed", "initial": "LeafChance"}]

# Frame Controls
start = 0
step = 1
end = 10

# File Location
hytaleLocation = "" # Find the location on your own computer and add it here!
fileLocation = "data/pre-release/Saves/WORLD GEN/mods/RedEngDev.NewWorldGen/Server/HytaleGenerator/Biomes/PreRelease/Tree_On_A_Cliff"
outputLocation = "" # Add where you would like to save your Screenshotted Frames to




# ---Automation---


biomeFile = ""

# Read Base File
def readFile():
    file = open(hytaleLocation + fileLocation + ".json", "r")
    return file.read()

# Modify Biome File to Specific Frame and Save
def runFrame(frameNum):
    newBiomeFile = ""

    case = -1

    for line in biomeFile.splitlines():
        # Switch Contents
        if case != -1 and defineInterpolations[case]["value"] in line:
            splitLine = line.split('	')
            for word in splitLine:
                if ',' in word:
                    # Seed Value
                    if type(defineInterpolations[case]["initial"]) is str:
                        newBiomeFile += '	"' + defineInterpolations[case]["initial"] + str(frameNum) + '",'
                    # Number Value
                    else:
                        newBiomeFile += '	' + str(defineInterpolations[case]["initial"] + defineInterpolations[case]["speed"] * frameNum) + ","
                else:
                    newBiomeFile += '	' + word
            newBiomeFile += '\n'
            case = -1
        # Check for Case
        else:
            for i in range(len(defineInterpolations)):
                if defineInterpolations[i]["name"] in line:
                    case = i
                    break
            newBiomeFile += line + '\n'

    # Write Contents
    file = open(hytaleLocation + fileLocation + "_Animated.json", "w")
    file.write(newBiomeFile)
    

# Initialize
biomeFile = readFile()
# Run all frames
for f in range(start, end, step):
    runFrame(f)
    time.sleep(30)
    pyautogui.screenshot(outputLocation + 'frame_' + str(f) + '.png')
    print("Finished Frame: " + str(f))