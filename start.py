import downloader
import main

main = main.Main()
downloader = downloader.Downloader()

downloader.start()
if downloader.destroy():
    main.start()

        