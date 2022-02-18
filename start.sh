
# Install Chrome.
sudo curl -sS -N -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | tac | tac | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

gunicorn app:app