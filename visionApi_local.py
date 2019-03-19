import requests
import json
import base64  # 画像はbase64でエンコードする必要があるため

API_KEY = "AIzaSyCFi4VPFjzVhKpl2x1pDh7AqbpDyruK0dw"


def text_detection(image_path):
    api_url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_KEY)
    with open(image_path, "rb") as img:
        image_content = base64.b64encode(img.read())
        req_body = json.dumps({
            'requests': [{
                'image': {
                    'content': image_content.decode('utf-8')  # base64でエンコードしたものjsonにするためdecodeする
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        res = requests.post(api_url, data=req_body)
        return res.json()


if __name__ == "__main__":
    img_path = "/Users/taishumatsubayashi/Desktop/test/nike.PNG"
    res_json = text_detection(img_path)
    res_text = res_json["responses"][0]["labelAnnotations"]
    for value in res_text:
        print (value ['description'])
