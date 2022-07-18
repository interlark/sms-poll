<div align="center">
    <h1>
        <a href="#">
            <img alt="SMS Poll Logo" width="50%" src="https://user-images.githubusercontent.com/20641837/179410769-3f99bfed-6bd7-4564-9560-860dd8f33051.svg"/>
        </a>
    </h1>
</div>

<div align="center">
    <a href="https://github.com/interlark/sms-poll/edit/master/requirements.txt"><img alt="Built with FastAPI, ReactJS, P4A" src="https://badgen.net/badge/Built%20with/FastAPI,ReactJS,P4A?list=|"/></a>
    <a href="https://github.com/interlark/sms-poll/blob/master/LICENSE"><img alt="License GPL v3" src="https://badgen.net/badge/License/GPL v3?color=green"/></a>
    <a href="https://github.com/interlark/sms-poll"><img alt="Python versions" src="https://badgen.net/badge/Python/3.7,3.8,3.9,3.10?list=|"/></a>
</div><br>

**SMS Poll** is Android app that turns your phone into __SMS-based poll system__ which you can deploy for your audience during *competitions, conferences or any other meetings*.

<br />
<div align="center">
    <a href="#install-and-usage">
       <img alt="Workflow diagram" width="50%" src="https://user-images.githubusercontent.com/20641837/179417162-6b945784-454a-4007-9963-79c5db2424dd.svg" />
    </a>
</div>

## ✨ Features
- 📱 Single app in your pocket, no PC needed
- 🪐 No internet or third-party service dependencies
- [![](https://user-images.githubusercontent.com/20641837/173175879-aed31bd4-b188-4681-89df-5ffc3ea05a82.svg)](#) Dark and light themes included

## 🚀 Installation

You can download latest APK from [Releases](https://github.com/interlark/sms-poll/releases/latest).

## ⚙️ Usage


* Just edit your poll list and that's it!

   <img width="65%" src="https://user-images.githubusercontent.com/20641837/179471062-00505e89-6163-47c5-a050-1abf540ef4fd.gif" />


* Your poll web page is 🔗 `http://<wifi-ip>:5000/poll`

   <img width="85%" src="https://user-images.githubusercontent.com/20641837/179475097-f47e53e3-a06d-4640-ae7c-bd9eb9352e39.gif" />


<details>
  <summary>🖼️ <b>Screenshots</b></summary>

<img width="30%" src="https://user-images.githubusercontent.com/20641837/179479514-72826ff7-8320-4779-ad9f-3b3458825862.jpg" />

<img width="30%" src="https://user-images.githubusercontent.com/20641837/179479519-a0942d26-1205-41cb-a790-ee0cb0202e4f.jpg" />

<img width="30%" src="https://user-images.githubusercontent.com/20641837/179479522-0c71b70a-5c3e-4d7c-8d63-a428f3139837.jpg" />

<img width="30%" src="https://user-images.githubusercontent.com/20641837/179479523-50c27eda-4cd0-4dd5-841d-c512fbba1f54.jpg" />

<img width="30%" src="https://user-images.githubusercontent.com/20641837/179479524-a5f046bc-a196-48d7-bc90-eed1224ac65c.jpg" />
  

</details>

## 💡 IRL
<div align="center">
    <img width="75%" alt="Realworld screenshot" src="https://user-images.githubusercontent.com/20641837/179423895-52618b56-3210-4883-9f41-a41565733260.jpg" />
</div>

## 📱 Requirements
   * Minimum SDK 23 (Android 6.0 and later)

## 💻 Development
For development [p4a](https://github.com/kivy/python-for-android) and [npm](https://github.com/npm/cli) are required.

```bash
# Clone repo and install requirements
git clone https://github.com/interlark/sms-poll && cd sms-poll
pip -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Build JS static files
make build_static

# Desktop debug
make dev_server  # http://localhost:5000
make dev_client  # http://localhost:1234/admin | http://localhost:1234/poll

# Build APK for X86, X86_64, armeabi-v7a or arm64-v8a architecture
make build_x86
make build_x86_64
make build_armeabi-v7a 
make build_arm64-v8a

# Mobile debug
emulator -avd <AVD>  # Run emulator
adb install SMSPoll-debug.apk
adb logcat | grep python  # Follow logs
```
