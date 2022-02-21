wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg-deb -xv google-chrome-stable_current_amd64.deb .
rm google-chrome-stable_current_amd64.deb

alias google-chrome="opt/google/chrome/chrome"

apt install -y xvfb

gunicorn app:app --timeout 600