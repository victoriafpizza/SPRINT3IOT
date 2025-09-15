import cv2
import os

# Caminho do Haar Cascade (arquivo XML dentro da pasta assets)
CASCADE_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(os.path.abspath(CASCADE_PATH))

if face_cascade.empty():
    print("Erro: haarcascade_frontalface_default.xml não foi carregado.")
    raise SystemExit

# Caminho do vídeo de teste (ou use 0 para webcam)
VIDEO_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'video.mp4')
cap = cv2.VideoCapture(VIDEO_PATH)  # troque por 0 para usar webcam

if not cap.isOpened():
    print("Erro: Não foi possível abrir a fonte de vídeo.")
    raise SystemExit

# Cria janela e trackbars para ajustar parâmetros
cv2.namedWindow('FaceDetect')

def nada(x): 
    pass

cv2.createTrackbar('scale x100', 'FaceDetect', 110, 200, nada)   # 1.10 – 2.00
cv2.createTrackbar('minNeighbors', 'FaceDetect', 5, 20, nada)
cv2.createTrackbar('minSize', 'FaceDetect', 30, 300, nada)

# Configura saída de vídeo anotado
w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(os.path.join(os.path.dirname(__file__), '..', 'saida_anotada.mp4'), fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lê valores das trackbars
    sf = max(1.01, cv2.getTrackbarPos('scale x100', 'FaceDetect') / 100.0)
    mn = max(1, cv2.getTrackbarPos('minNeighbors', 'FaceDetect'))
    ms = max(20, cv2.getTrackbarPos('minSize', 'FaceDetect'))

    # Detecta rostos
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=sf,
        minNeighbors=mn,
        minSize=(ms, ms)
    )

    # Desenha retângulo e texto
    for (x, y, w0, h0) in faces:
        cv2.rectangle(frame, (x, y), (x + w0, y + h0), (0, 0, 255), 2)
        cv2.putText(frame, "Rosto Detectado", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostra parâmetros atuais na tela
    cv2.putText(frame, f'scale={sf:.2f} neighbors={mn} minSize={ms}px',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('FaceDetect', frame)
    out.write(frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
