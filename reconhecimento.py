import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Erro: haarcascade_frontalface_default.xml não foi carregado.")
    raise SystemExit

cap = cv2.VideoCapture('video.mp4')  # troque por 0 para webcam
if not cap.isOpened():
    print("Erro: Não foi possível abrir a fonte de vídeo.")
    raise SystemExit

cv2.namedWindow('FaceDetect')
def nada(x): pass
cv2.createTrackbar('scale x100', 'FaceDetect', 110, 200, nada)   # 1.10–2.00
cv2.createTrackbar('minNeighbors', 'FaceDetect', 5, 20, nada)
cv2.createTrackbar('minSize', 'FaceDetect', 30, 300, nada)

w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('saida_anotada.mp4', fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret: break

    gr
