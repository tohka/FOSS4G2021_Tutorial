import time
import urllib.request

baseurl = r"https://cyberjapandata.gsi.go.jp/xyz/std/{}/{}/{}.png"

def main():
    tiles = [
        (4, 13, 5),
        (4, 13, 6),
        (4, 14, 5),
        (4, 14, 6)
    ]

    for zxy in tiles:
        z, x, y = zxy
        print(f"{z}/{x}/{y}.png をダウンロード")
        urllib.request.urlretrieve(baseurl.format(*zxy), f"{z}_{x}_{y}.png")
        generate_worldfile_for_tile(zxy)
        time.sleep(1) # サーバにやさしく




def generate_worldfile_for_tile(zxy):
    z, x, y = zxy

    # 対象ズームレベルのタイルの長さ（ EPSG:3857 ）
    s = 40075016.68557849 / (2**z)
    # 対象ズームレベルの解像度（ m / px ）
    r = s / 256.0

    # 左上の座標
    x_off =  (x - 2**(z-1)) * s
    y_off = -(y - 2**(z-1)) * s
    
    with open(f"{z}_{x}_{y}.pgw", mode="w") as f:
        f.write(f"{r:.9f}\n")
        f.write(f"{0:.9f}\n")
        f.write(f"{0:.9f}\n")
        f.write(f"{-r:.9f}\n")
        f.write(f"{x_off:.9f}\n")
        f.write(f"{y_off:.9f}\n")

    
main()


