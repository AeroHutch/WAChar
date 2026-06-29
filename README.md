# Installing
## Prerequisites

Before setting up **WAChar**, ensure your system has **Python 3.8 to 3.11** installed. 
*(Note: `webrtcvad` may occasionally face compilation hurdles on Python 3.12+ on certain operating systems without extra build tools).*

### Cross-Platform Core Requirement: FFmpeg
Because this script utilizes `moviepy` to render video assets, **FFmpeg** must be installed on your system[cite: 1]. 

* **macOS:** `brew install ffmpeg`
* **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`
* **Windows:** Download from the [official FFmpeg site](https://ffmpeg.org/download.html) and add its `bin` folder to your System PATH variables.

---

## Installation & Setup

### macOS & Linux

1. **Clone or download** this repository to your local machine.
2. Open your Terminal and navigate to the project directory:
```bash
cd path/to/WAChar
```

3. Create a virtual environment to keep your global system clean:
```bash
python3 -m venv venv
source venv/bin/activate
```


4. Install the required Python packages:
```bash
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```



### Windows

1. **Clone or download** this repository to your local machine.
2. Open **Command Prompt** or **PowerShell** and navigate to the project directory:
```cmd
cd path\to\WAChar
```


3. Create a virtual environment and activate it:
```cmd
python -m venv venv
.\venv\Scripts\activate
```


4. Install the required Python packages:
```cmd
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```

*(Note: If you run into a `Microsoft Visual C++ 14.0 or greater is required` error while installing `webrtcvad`, download and install the Visual Studio Build Tools and check the "Desktop development with C++" workload).*

---

## Preparing Assets

Before running the script, make sure your workspace looks like this:

```
WAChar/
├── new.py             # The main python script
├── silent.png         # Image shown when NO speech is detected
├── talking.png        # Image shown WHEN speech is detected
└── recordings/        # Directory containing your audio files
    └── episode1.mp3
```

> **Important:** Ensure you place your `silent.png` and `talking.png` directly in the root directory alongside `new.py`. The script will automatically generate the `recordings/` directory on its first run if it doesn't already exist.
> 
> 

---

## Usage

1. Activate your virtual environment if it isn't already (`source venv/bin/activate` or `.\venv\Scripts\activate`).
2. Run the main script:
```bash
python new.py
```
3. The interactive command-line interface will display a list of all `.mp3` files found inside the `recordings/` folder.
4. Type the number corresponding to your chosen file and hit **Enter**.
5. The program will analyze any sound (make sure your background audio is as quiet as possible), sync the frames, and export your finished file as `output_video.mp4` in the root folder.
