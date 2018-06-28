
def image_crop(path, x1, y1, x2, y2):
    from PIL import Image
    im = Image.open(path)
    img_size = im.size
    if x1>x2 or y1>y2 or x2>img_size[0] or y2>img_size[1]:
        raise ValueError("传入截取范围不符合规范或超出原图片大小")
    region = im.crop((x1, y1, x2, y2))
    region.save(path.split('.png')[0]+'_crop.png')
    return path.split('.png')[0]+'_crop.png'

def face_recog(img=''):
    import face_recognition
    import os
    a = os.path.dirname(os.path.dirname(os.path.abspath('begin.py')))
    image_path = a + '/detection/media/cover/'  # 需要改成类似'media/cover'
    image_list = os.listdir(image_path)
    encoding_list = []
    labels = []

    for i in range(len(image_list)):
        image = face_recognition.load_image_file(image_path+image_list[i])
        encoding = face_recognition.face_encodings(image)[0]
        encoding_list.append(encoding)

    test_image = face_recognition.load_image_file(img)
    test_encoding = face_recognition.face_encodings(test_image)[0]

    results = face_recognition.compare_faces(encoding_list, test_encoding)
    for i in range(len(image_list)):
        labels.append(image_list[i].split('.')[-2])

    for i in range(0, len(results)):
        if results[i]:
            return labels[i]
    

def detection(img):    
    from darkflow.net.build import TFNet
    import cv2
    import os
    a = os.path.dirname(os.path.dirname(os.path.abspath('begin.py')))
    # options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.5}
    options = {"pbLoad": a + "/built_graph/yolo.pb", "metaLoad": a + "/built_graph/yolo.meta", "threshold": 0.5}
    tfnet = TFNet(options)

    imgcv = cv2.imread(img)
    result = tfnet.return_predict(imgcv)
    
    for i in result:
        if i['label'] == 'person':
            topleft_x=i['topleft']['x']
            topleft_y=i['topleft']['y']
            bottomright_x=i['bottomright']['x']
            bottomright_y=i['bottomright']['y']
            break
    a = image_crop(img,topleft_x,topleft_y,bottomright_x,bottomright_y)
    b = face_recog(a)
    return b 


