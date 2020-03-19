import requests
import sys
import os
from urllib.parse import urlparse

pdf_files = [
  'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
]

def downloadFile(url, fileName):
  with open(fileName, "wb") as file:
    response = requests.get(url)
    file.write(response.content)

for pdf in pdf_files:
  scriptPath = sys.path[0]
  downloadPath = os.path.join(scriptPath, '')
  url = pdf
  fileName = os.path.basename(urlparse(url).path)
  print('path of the script: ' + scriptPath)
  print('downloading file to: ' + downloadPath)
  downloadFile(url, downloadPath + fileName)
  print('file downloaded!')


print('exiting program!')