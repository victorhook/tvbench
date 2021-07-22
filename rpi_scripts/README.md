These scripts helps running the Pi.

They are located in:

- `app` - Root of repo.
- `start` - Root of repo.
- `flask.service` - /etc/sytemd/system/ - This is used for systemd to run flask as a service.
- `environment` - /etx/xdg/openbox/ - Used to set env variable of what url to go to in kiosk.
- `autostart` - /etx/xdg/openbox/ - Used to configure and start chromium-browser.
- `.bash_profile` - ~/ - On home dir, used to start x-server on boot.
