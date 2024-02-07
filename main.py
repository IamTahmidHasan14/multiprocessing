#MULTIPROCESSING
import multiprocessing
import requests


def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")


# if __name__ == '__main__':   #this line is for windows
url = "https://picsum.photos/3840/2160"
pros = []
for i in range(5):
  # downloadFile(url, i)
  p = multiprocessing.Process(target=downloadFile, args=[url, i + 1])
  p.start()
  pros.append(p)

for p in pros:
  p.join()
