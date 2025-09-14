# 🧠 PyJARVIS – Your Personal Voice Assistant  

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  ![Speech Recognition](https://img.shields.io/badge/Uses-speech__recognition-orange.svg)  ![Pyttsx3](https://img.shields.io/badge/Powered%20By-pyttsx3-green.svg)  ![Tkinter GUI](https://img.shields.io/badge/GUI-Tkinter-red.svg)  ![Weather API](https://img.shields.io/badge/Feature-Weather%20Reports-lightblue.svg)

PyJARVIS is a **Python-based AI Voice Assistant** with a **Tkinter-powered GUI**, capable of performing multiple desktop and internet tasks. It uses **speech recognition + text-to-speech** along with APIs to provide an interactive experience.

---

## ✨ Features

PyJARVIS is designed to be your personal digital assistant, capable of handling a variety of commands:

* **Voice Control:** Interact naturally using speech.
* **Web Automation:** Open popular websites (Google, YouTube, Facebook, etc.) and perform web searches.
* **Information Retrieval:** Query Wikipedia for quick summaries.
* **System Commands:** Open essential desktop applications like Notepad, Calculator, and Command Prompt.
* **Time & Date:** Get current time and date information.
* **Weather Updates:** Fetch real-time weather reports for specified cities (requires OpenWeather API key).
* **Entertainment:** Tell jokes.
* **Memory Function:** Remember and recall custom notes.
* **GUI:** Interactive desktop interface to view commands and responses.

---

## 🛠️ Technologies Used

* **Python 3.9+**
* **`pyttsx3`**: Text-to-speech conversion.
* **`SpeechRecognition`**: Voice recognition from microphone input.
* **`pywhatkit`**: YouTube control and general web searches.
* **`wikipedia`**: Integration with Wikipedia for information lookup.
* **`tkinter`**: For the graphical user interface.
* **`requests`**: For making API calls (e.g., OpenWeatherMap).
* **`python-dotenv`**: Securely loading API keys from `.env` files.
* `datetime`, `os`, `webbrowser`, `pyjokes`, `threading`, `time` (standard Python libraries)

---

## 🚀 Getting Started

Follow these steps to get PyJARVIS running on your local machine.

### Prerequisites

* Python 3.9 or higher
* A working microphone
* An [OpenWeatherMap API Key](https://openweathermap.org/api) (for weather functionality)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/OmKadane/PyJARVIS.git
    cd PyJARVIS
    ```

2.  **Create and activate a virtual environment:**
    * **Windows:**
        ```sh
        python -m venv myenv
        myenv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```sh
        python3 -m venv myenv
        source myenv/bin/activate
        ```

3.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your OpenWeatherMap API Key:**
    * Create a file named `.env` in the root of your project directory (the same level as `main.py`).
    * Add your OpenWeatherMap API key to this file:
        ```
        OPENWEATHER_API_KEY="your_new_api_key_here"
        ```
    * Ensure `.env` is listed in your `.gitignore` file to prevent accidental exposure.

### Usage

Once the setup is complete, run the main script from your terminal (with your virtual environment activated):

```sh
python main.py
```

The assistant's GUI will appear, and it will greet you and start listening. Click "Start Listening" if it doesn't begin automatically. You can give it commands like:

* "Open Notepad"
* "What time is it?"
* "Search for Python tutorials"
* "Tell me a joke"
* "Weather in London"
* "Remember this is my task list"
* "Exit"

---

## 🤝 How to Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
Made with ❤️ by Om Kadane
</div>
