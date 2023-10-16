disallow_list = [
      "!rm -rf /",
      "!rm -rf *",
      "!find / -delete",
      "!> /dev/sda",
      "!dd if=/dev/random of=/dev/sda",
      "!mkfs.ext4 /dev/sda",
      "!mv ~ /dev/null",
      "!shutdown -h now",
      "!reboot",
      "!halt",
      "!poweroff",
      "!passwd root",
      "!init 0",
      "!dd if=/dev/zero of=/dev/sda",
      "!mkfs.ext3 /dev/sda1",
      "!mv directory_to_destroy /dev/null",
      "!openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt",
      "!del /F /S /Q C:\\*.*",  # Windows command
      "!rd /S /Q C:\\",  # Windows command
      "!format C: /y",  # Windows command
      "!format /FS:NTFS /Q /Y C:",  # Windows command
      "!schtasks /create /sc minute /mo 1 /tn \"My task\" /tr \"C:\\Windows\\System32\\shutdown.exe /s\"",  # Windows command
      "!reg delete HKCR\\*",  # Windows command
      "!reg delete HKCU\\*",  # Windows command
      "!reg delete HKLM\\*",  # Windows command
      "!reg delete HKU\\*",  # Windows command
      "!reg delete HKCC\\*",  # Windows command
      "os.system('rm -rf /')",  # Python command
      "os.system('rm -rf *')",  # Python command
      "os.system('shutdown -h now')",  # Python command
      "shutil.rmtree('/')",  # Python command
      "os.rmdir('/')",  # Python command
      "os.unlink('/')",  # Python command
      "os.system('find / -delete')",  # Python command
      "os.system('> /dev/sda')",  # Python command
      "os.system('dd if=/dev/random of=/dev/sda')",  # Python command
      "os.system('mkfs.ext4 /dev/sda')",  # Python command
      "os.system('mv ~ /dev/null')",  # Python command
      "os.system('shutdown -h now')",  # Python command
      "os.system('reboot')",  # Python command
      "os.system('halt')",  # Python command
      "os.system('poweroff')",  # Python command
      "os.system('passwd root')",  # Python command
      "os.system('init 0')",  # Python command
      "os.system('dd if=/dev/zero of=/dev/sda')",  # Python command
      "os.system('mkfs.ext3 /dev/sda1')",  # Python command
      "os.system('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt')",  # Python command
    ]