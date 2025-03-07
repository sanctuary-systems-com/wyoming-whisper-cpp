# Wyoming Whisper.cpp

[Wyoming protocol](https://github.com/rhasspy/wyoming) server for the [whisper.cpp](https://github.com/ggerganov/whisper.cpp) speech to text system.

## Local Install

Install dependencies:

```sh
sudo apt-get install build-essential
```

Clone the repository and set up Python virtual environment:

``` sh
git clone https://github.com/rhasspy/wyoming-whisper-cpp.git
cd wyoming-whisper-cpp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install .
```

Run a server anyone can connect to:
```sh
wyoming-whisper-cpp \
  --model tiny.en-q5_1 \
  --language en \
  --uri 'tcp://0.0.0.0:10300' \
  --data-dir ./data \
  --download-dir ./data
```

## Docker Image

``` sh
docker run -it -p 10300:10300 -v /path/to/local/data:/data rhasspy/wyoming-whisper-cpp \
    --data-dir /data --model tiny.en-q5_1 --language en
```

[Source](https://github.com/rhasspy/wyoming-addons/tree/master/whisper-cpp)

## GPU Support

To build with GPU support, pass the relevant CMake flags to the install command:

``` sh
CMAKE_ARGS="-DGGML_VULKAN=1" pip install .
```
