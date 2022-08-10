from views import downloader
from views import main

main = main.Main()
downloader = downloader.Downloader()

downloader.start()
if downloader.destroy():
    main.start()

        