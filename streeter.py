import json
import requests
import jieba

# 逸凡的小世界：https://fu1fan.cn


KEY = "在这里填写你的key"
CITY = "宁波"


def AmapLBS(service="v3/geocode/geo", para=None):
    if para is None:
        para = {}
    paradic = {"key": KEY}
    paradic.update(para)
    responese = requests.get(f"https://restapi.amap.com/{service}", params=paradic)
    responese.raise_for_status()
    data = json.loads(responese.text)
    if data["status"] != "1":
        raise Exception("LBS错误")
    return data


def get_street(address):
    data = AmapLBS(para={"address": address, "city": CITY})
    location = data["geocodes"][0]["location"]

    data = AmapLBS("v5/place/around", {"keywords": "街道办事处", "location": location})
    streets = []
    for poi in data["pois"]:
        name = poi["name"]
        if "街道办事处" in name:
            cut = jieba.lcut(name)
            i = cut.index("街道")
            street_name = f"{cut[i - 1]}{cut[i]}"
            streets.append(street_name)
            if len(cut[i - 1]) == 1:
                streets = []
                deep = min(i - 1, 3)
            else:
                deep = min(i - 1, 2)
            for j in range(1, deep + 1):
                for ch in cut[i - j - 1]:
                    if not '\u4e00' <= ch <= '\u9fff':
                        break
                else:
                    street_name = cut[i - 1 - j] + street_name
                    streets.append(street_name)
                    continue
                break
            break
    if streets:
        return streets
    else:
        raise Exception("无结果")


if __name__ == "__main__":
    print(get_street(input("请输入地址：")))
