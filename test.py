import os
import requests
from urllib.parse import urlparse

# Список URL изображений (копируешь из DevTools или собираешь скриптом)
image_urls = [
    "https://framerusercontent.com/images/1E8ITXxK2hLzaQdTJsnSwfveGao.png?scale-down-to=512",
    "https://framerusercontent.com/images/1SegmZwfxhbcI6pAEfIrlE5b1xs.jpeg",
    "https://framerusercontent.com/images/1ji9y1b4oenI1yVOT3mNwdx7Agw.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/2nKWK66tFbw9GfV7t4pPow1YoMA.png",
    "https://framerusercontent.com/images/2s6tWDf6zxddxijMBvuaI0OY.png?scale-down-to=512",
    "https://framerusercontent.com/images/4ZMs5JRU1ZA5teoQEsytFBrP0A.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/5grriBxPunNbAmrozECg2OKuv4.png",
    "https://framerusercontent.com/images/5nEBgENqTwGxVG8L9t2iKuI4.png",
    "https://framerusercontent.com/images/7G6r8G6eJWaDXnogcmGWxsDFtM.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/8TZkcVm8ogVXOIfsPlJ7EdGGhwQ.png?scale-down-to=1024",
    "https://framerusercontent.com/images/8l2M4cJXu1xLi4kE53cQprMom7c.png",
    "https://framerusercontent.com/images/9ZJBOMfkfFK6oNnmzKRDFc0RE.jpg?scale-down-to=512",
    "https://framerusercontent.com/images/9vHhhN0vHSrQdYZt2VxcZLmDzU.png",
    "https://framerusercontent.com/images/675LMvLV223KmvE4kikkYLu08.webp",
    "https://framerusercontent.com/images/CcTigO4GNUKTG91WcPrqoopDc.png",
    "https://framerusercontent.com/images/F4N1eyNH2sJk4FvgMaaM66nrEM.png?scale-down-to=1024",
    "https://framerusercontent.com/images/HWDZa2dTx2Sm9pSNVbGhYS846k.webp",
    "https://framerusercontent.com/images/HnIkL8VVbulgYfUWg4ZqdcnRt1Y.png?scale-down-to=512",
    "https://framerusercontent.com/images/IQyXqggTtdTP8cFd3G4PavFrw.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/L9Y5otZgeO1tMAOi28I8x3nmxc.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/OR8ZUhhL7JmRC8HZYjl81lWD6iU.png",
    "https://framerusercontent.com/images/P9FhkVovXR7HzUpAnQTrEV4c.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/POu4hrlc3BxtdmWaPo75wGeUrw.png",
    "https://framerusercontent.com/images/RyobSGjQEA1oYaV2lRRG4TKlQo.png",
    "https://framerusercontent.com/images/RyobSGjQEA1oYaV2lRRG4TKlQo.png?scale-down-to=512",
    "https://framerusercontent.com/images/S6wGw2Hl1WVZG7BYKZIXN1c0M.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/TIWblW77kJKfYEAGsFva3HDPdE.jpeg",
    "https://framerusercontent.com/images/VTn52ydC4wfOXN6T6OS5vNigeFs.png?scale-down-to=1024",
    "https://framerusercontent.com/images/VbyKOCuFhDC9rG1LEL3pySKQMP4.png",
    "https://framerusercontent.com/images/W84LV5PrXKoXnUdiplrb982zDDw.png",
    "https://framerusercontent.com/images/WwVztsZG3L4iTEDn6TDM6uaqU.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/WyqY4NkXvKTQdtSMpH56jgJCNc.jpeg",
    "https://framerusercontent.com/images/XNhdfpHdOoCYjqaq7Nqz5atp2Dw.png",
    "https://framerusercontent.com/images/XQU0I8Kvk8HelpdZUsMI1yPGpc.webp",
    "https://framerusercontent.com/images/YGiKXtO1I3zBS71vUWA0CANenQ.webp",
    "https://framerusercontent.com/images/Yel5AJKm6nlJJr0xZUgju185w.webp",
    "https://framerusercontent.com/images/ZSDyodLszVy6J5ooLRYLhobkpQ.png",
    "https://framerusercontent.com/images/bPTyxyCrT7bGLpVmplO2lLpE19w.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/d4XdxyeFPmMn577US5DwEfbQNA.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/eTdF4XZa8s8cuby7S5FRVF65GZg.png?scale-down-to=512",
    "https://framerusercontent.com/images/fTmfy8hsM7l4HeuBrKhePF6VqE.png",
    "https://framerusercontent.com/images/fTmfy8hsM7l4HeuBrKhePF6VqE.png?scale-down-to=512",
    "https://framerusercontent.com/images/foWlXHiV7rw8FxI7akNX9rVS8.png?scale-down-to=512",
    "https://framerusercontent.com/images/h0Dx7MsVRP6yEQMSFhS0hJ7EeE.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/hCH60IG9RsD6E39IJTNkJSq22o.webp",
    "https://framerusercontent.com/images/hYCMPp3a22xSpqcX7QhAmTgHH0.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/i7nX29boPiHjbwxiILRu7syuB8.webp",
    "https://framerusercontent.com/images/jHPeYpsuOP3mYrF8F8UzyFc4cU.jpg?scale-down-to=512",
    "https://framerusercontent.com/images/jjtbQM13TjKZFOfBaoY69dJbE.png",
    "https://framerusercontent.com/images/k36ScfdJ7mxizXdpEAL34z9LSt8.png",
    "https://framerusercontent.com/images/lekjxtOFEO5kRmtWapcuGSyOuYg.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/mG0rF44ou30glZvO9RsgZx7114.png",
    "https://framerusercontent.com/images/mG0rF44ou30glZvO9RsgZx7114.png?scale-down-to=512",
    "https://framerusercontent.com/images/nHikCsWK4EXrcafPH8fwrlz4W0.png",
    "https://framerusercontent.com/images/oRJQ3U1Zj60jpcEUy6WMh70kGP0.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/onGFFiNy1K68rCwItMgD7JmlUHA.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/otWHZ40V8UYGDvEYhV1b8qYQ9E.png",
    "https://framerusercontent.com/images/q2ljljrzCoUnyWK2I0C1FCBx4k.webp",
    "https://framerusercontent.com/images/qF78aXyjJCb2hsnpX2BcclOXZxA.jpeg?scale-down-to=512",
    "https://framerusercontent.com/images/qkjDHxbgI4j7ElnSGPFsKYF07E.png",
    "https://framerusercontent.com/images/rMbEPUlQUQcdHfrGtjN4l67DNY.webp",
    "https://framerusercontent.com/images/rZ9ysjgrBANuqtoLfEY0s8zeUg.webp",
    "https://framerusercontent.com/images/v66UNbtwy7PelDU8N5T4beWcW4.png?scale-down-to=512",
    "https://framerusercontent.com/images/wOlK6ik5pv77zVtHT5RKMlVCrX4.jpg?scale-down-to=1024",
    "https://framerusercontent.com/images/x8Y32HrErVsHbcOiz20pqjX6Nhs.png",
    "https://framerusercontent.com/images/x8Y32HrErVsHbcOiz20pqjX6Nhs.png?scale-down-to=512",
    "https://framerusercontent.com/images/zP6caalLjvVnuf7GSq0cxdXYvNQ.webp",
    "https://framerusercontent.com/images/zXWWmz0fV2SY8uCosfudAASiqA.png",
    "https://framerusercontent.com/images/zqf3jy9eFLtDPTPWprfpQH7nGs.png",

]

# Локальная папка для сохранения
LOCAL_DIR = "nfactorial/static/framerusercontent.com/sites/7yghCMT8Lg3FqlbLLafjE0"
os.makedirs(LOCAL_DIR, exist_ok=True)

for url in image_urls:
    file_name = os.path.basename(urlparse(url).path)  # имя файла из URL
    local_path = os.path.join(LOCAL_DIR, file_name)
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(r.content)
        print(f"[DOWNLOADED] {file_name}")
    except Exception as e:
        print(f"[FAILED] {file_name} -> {e}")
