#!/usr/bin/env bash
set -e

echo "🌐 Updating cloud systems and installing GUI desktop elements..."
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc wget curl unzip

echo "📦 Downloading and installing stable Google Chrome binaries..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# We add || true here so set -e doesn't crash the script when dependencies are missing
sudo dpkg -i google-chrome-stable_current_amd64.deb || true
sudo apt-get install -f -y

echo "🧹 Cleaning up installation packages..."
rm google-chrome-stable_current_amd64.deb

echo "🐍 Installing Python automation modules..."
pip install selenium

echo "🖥️ Initializing the Virtual Display Matrix (Screen :1)..."
Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1
fluxbox &

echo "📡 Launching web proxy stream on Port 6080..."
websockify --web=/usr/share/novnc 6080 localhost:5900 &
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 &

echo ""
echo "================================================================="
echo "🎉 CLOUD INTERFACE READY!"
echo "1. Go to the PORTS tab at the bottom of Codespaces."
echo "2. Find Port 6080, right-click 'Private' and switch it to PUBLIC."
echo "3. Tap the browser icon (Local Address) for 6080 to open your display panel!"
echo "4. Return here and type: python bot.py"
echo "================================================================="
