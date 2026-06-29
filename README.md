# English
## Prerequisites

Before setting up **WAChar**, ensure your system has **Python 3.8 to 3.11** installed. 
*(Note: `webrtcvad` may occasionally face compilation hurdles on Python 3.12+ on certain operating systems without extra build tools).*

### Cross-Platform Core Requirement: FFmpeg
Because this script utilizes `moviepy` to render video assets, **FFmpeg** must be installed on your system. 

* **macOS:** `brew install ffmpeg`
* **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`
* **Windows:** Download from the [official FFmpeg site](https://ffmpeg.org/download.html) and add its `bin` folder to your System PATH variables.

---

## Installation & Setup

### macOS & Linux

1. **Download** the newest version to your local machine.
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

1. **Download** the newest version to your local machine.
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
├── silent.png         # Image shown when NO sound is detected
├── talking.png        # Image shown WHEN sound is detected
└── recordings/        # Directory containing your audio files
    └── episode1.mp3
```

> **Important:** Ensure you place your `silent.png` and `talking.png` directly in the root directory alongside `new.py`. The script will automatically generate the `recordings/` directory on its first run if it doesn't already exist.

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

# Nederlands
## Vereisten

Voordat u **WAChar** instelt, moet u ervoor zorgen dat **Python 3.8 tot en met 3.11** op uw systeem is geïnstalleerd.

*(Opmerking: `webrtcvad` kan soms compilatieproblemen ondervinden op Python 3.12+ op bepaalde besturingssystemen zonder extra buildtools).*

### Vereiste voor platformonafhankelijke compatibiliteit: FFmpeg
Omdat dit script `moviepy` gebruikt om videobestanden te renderen, moet **FFmpeg** op uw systeem zijn geïnstalleerd.

* **macOS:** `brew install ffmpeg`
* **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`
* **Windows:** Download het van de [officiële FFmpeg-website](https://ffmpeg.org/download.html) en voeg de `bin`-map toe aan uw systeemvariabelen (PATH).

---

## Installatie en configuratie

### macOS & Linux

1. **Download** de nieuwste versie naar uw lokale computer.
2. Open uw Terminal en navigeer naar de projectmap:
```bash
cd path/to/WAChar
```

3. Maak een virtuele omgeving aan om uw globale systeem schoon te houden:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Installeer de benodigde Python-pakketten:
```bash
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```

### Windows

1. **Download** de nieuwste versie naar uw lokale computer.
2. Open **Opdrachtprompt** of **PowerShell** en navigeer naar de projectmap:
```cmd
cd pad\naar\WAChar
```

3. Maak een virtuele omgeving aan en activeer deze:

```cmd
python -m venv venv

.\venv\Scripts\activate
```
4. Installeer de benodigde Python-pakketten:
```cmd
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```

*(Opmerking: Als u de foutmelding `Microsoft Visual C++ 14.0 of hoger is vereist` krijgt tijdens de installatie van `webrtcvad`, download en installeer dan de Visual Studio Build Tools en controleer de workload "Desktopontwikkeling met C++").*

---

## Assets voorbereiden
Zorg ervoor dat uw werkruimte er als volgt uitziet voordat u het script uitvoert:

```
WAChar/
├── new.py # Het hoofdscript in Python
├── silent.png # Afbeelding die wordt weergegeven wanneer er GEEN geluid wordt gedetecteerd
├── talking.png # Afbeelding die wordt weergegeven WANNEER er geluid wordt gedetecteerd
└── recordings/ # Map met je audiobestanden
    └── episode1.mp3
```

> **Belangrijk:** Zorg ervoor dat je je `silent.png` en `talking.png` rechtstreeks in de hoofdmap plaatst, naast `new.py`. Het script maakt automatisch de map `recordings/` aan bij de eerste keer uitvoeren, als deze nog niet bestaat.

---

## Gebruik

1. Activeer je virtuele omgeving als deze nog niet is geactiveerd (`source venv/bin/activate` of `.\venv\Scripts\activate`).
2. Voer het hoofdscript uit:
```bash
python new.py
```
3. De interactieve opdrachtregelinterface toont een lijst met alle `.mp3`-bestanden in de map `recordings/`.
4. Typ het nummer van het gewenste bestand en druk op **Enter**.
5. Het programma analyseert het geluid (zorg ervoor dat de achtergrondgeluiden zo zacht mogelijk zijn), synchroniseert de frames en exporteert het voltooide bestand als `output_video.mp4` naar de hoofdmap.

# Türkçe
## Önkoşullar

**WAChar**'ı kurmadan önce, sisteminizde **Python 3.8 ila 3.11** kurulu olduğundan emin olun.
*(Not: `webrtcvad`, bazı işletim sistemlerinde ek derleme araçları olmadan Python 3.12+ sürümlerinde zaman zaman derleme sorunlarıyla karşılaşabilir.)*
### Çapraz Platform Temel Gereksinimi: FFmpeg
Bu betik video varlıklarını işlemek için `moviepy` kullandığından, sisteminizde **FFmpeg** kurulu olmalıdır.

* **macOS:** `brew install ffmpeg`
* **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`
* **Windows:** [Resmi FFmpeg sitesinden](https://ffmpeg.org/download.html) indirin ve `bin` klasörünü Sistem PATH değişkenlerinize ekleyin.

---

## Kurulum ve Ayarlar
### macOS ve Linux

1. En yeni sürümü yerel makinenize **indirin**.
2. Terminalinizi açın ve proje dizinine gidin:
```bash
cd path/to/WAChar
```
3. Genel sisteminizi temiz tutmak için sanal bir ortam oluşturun:
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Gerekli Python paketlerini yükleyin:
```bash
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```

### Windows

1. En yeni sürümü yerel makinenize **indirin**.
2. **Komut İstemi** veya **PowerShell**'i açın ve proje dizinine gidin:
```cmd
cd path\to\WAChar
```
3. Sanal bir ortam oluşturun ve etkinleştirin:
```cmd
python -m venv venv
.\venv\Scripts\activate
```
4. Gerekli Python paketlerini yükleyin:
```cmd
pip install --upgrade pip
pip install numpy soundfile webrtcvad moviepy scipy
```
*(Not: `webrtcvad` yüklerken `Microsoft Visual C++ 14.0 veya üstü gereklidir` hatasıyla karşılaşırsanız, Visual Studio Build Tools'u indirip yükleyin ve "C++ ile masaüstü geliştirme" iş yükünü işaretleyin.)*

---

## Varlıkların Hazırlanması
Komut dosyasını çalıştırmadan önce, çalışma alanınızın şu şekilde göründüğünden emin olun: Bu:
```
WAChar/
├── new.py # Ana Python betiği
├── silent.png # Ses algılanmadığında gösterilen resim
├── talking.png # Ses algılandığında gösterilen resim
└── recordings/ # Ses dosyalarınızı içeren dizin
    └── episode1.mp3
```

> **Önemli:** `silent.png` ve `talking.png` dosyalarınızı `new.py` ile birlikte doğrudan kök dizine yerleştirdiğinizden emin olun. Betik, `recordings/` dizinini ilk çalıştırıldığında otomatik olarak oluşturacaktır, eğer zaten mevcut değilse.

---

## Kullanım

1. Sanal ortamınızı zaten etkin değilse etkinleştirin (`source venv/bin/activate` veya `.\venv\Scripts\activate`).
2. Ana betiği çalıştırın:
```bash
python new.py
```
3. Etkileşimli komut satırı arayüzü, `recordings/` klasöründe bulunan tüm `.mp3` dosyalarının bir listesini gösterecektir.
4. Seçtiğiniz dosyaya karşılık gelen numarayı yazın ve **Enter** tuşuna basın.
5. Program, herhangi bir sesi analiz edecek (arka plan sesinizin mümkün olduğunca sessiz olduğundan emin olun), kareleri senkronize edecek ve bitmiş dosyanızı kök klasöre `output_video.mp4` olarak dışa aktaracaktır.
