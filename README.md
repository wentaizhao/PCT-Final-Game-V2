# PCT Final Game
***Note: These instructions are for Mac. Windows should be similar.***

## Setup 

1. **Download Python**
   - Open the Terminal app.
   - Check if Python is already installed on your computer by typing:
     ```bash
     python --version
     ```
   - If you see Python and a version number, skip this section.
   - Otherwise, download Python from [https://www.python.org/](https://www.python.org/) and follow the instructions.
   - Open Terminal and type:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
     to confirm that Python is installed.

2. **Downloading the Game**
   - Visit the GitHub repository: [https://github.com/wentaizhao/PCT-Final-Game-V2](https://github.com/wentaizhao/PCT-Final-Game-V2).
   - Click the green **Code** button in the top-right corner and select **Download ZIP**.
   - Double-click the ZIP file in Finder to extract the `PCT-Final-Game-V2-main` folder.
   - Move this folder to a safe location.

## Running the Game

1. Open the `PCT-Final-Game-V2-main` folder.
2. Right-click on the `gui.py` file and select **Get Info**.
3. Under **General**, in the **Where** field, right-click the path and select **Copy as Pathname**.
4. Open the Terminal app.
5. Type `cd` followed by a `space` and the path you copied and hit enter (e.g. `cd /Users/wentaizhao/projects/PCT-Final-Game-V2-main`)
6. Type `python ./gui.py` and hit enter (or `python3 ./gui.py`)

## Notes
- Only type in lowercase letters
- If they don’t have a minor, type `none`
- Some majors and minors are abbreviated. Common abbreviations include
    - bba
    - cs
    - econ
    - stats
    - ioe
    - ux
- Check the `f24.csv` file to see all abbreviations
- You can press the **Show Stats** button to see what you missed. You must close and reopen the window to refresh.
