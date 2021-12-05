import sys
import os
import glob


# 引数チェック
if len(sys.argv) == 1:
    print("引数が指定されていません。", file=sys.stderr)
    print("usage: python3 generate_metadata.py TILES_DIR", file=sys.stderr)
elif len(sys.argv) > 2:
    print("引数が多すぎます。")
    print("usage: python3 generate_metadata.py TILES_DIR", file=sys.stderr)
else:
    tiles_dir = sys.argv[1]

    if os.path.isdir(tiles_dir):
        zoom_dirs = [os.path.basename(f) for f \
                in glob.glob(f"./{tiles_dir}/*") if os.path.isdir(f)]
        zoom_dirs = sorted(map(int, zoom_dirs))

        with open(f"./{tiles_dir}/metadata.json", mode="w") as f:
            f.write('{\n')
            f.write('\t"name": "Natural Earth",\n')
            f.write('\t"format": "png",\n')
            f.write('\t"bounds": "-180.0,-85.051129,180.0,85.051129",\n')
            f.write(f'\t"minzoom": "{zoom_dirs[0]}",\n')
            f.write(f'\t"maxzoom": "{zoom_dirs[-1]}"\n')
            f.write('}')
    else:
        print("フォルダを指定してください", file=sys.stderr)
        print("usage: python3 generate_metadata.py TILES_DIR", file=sys.stderr)



