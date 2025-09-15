import cv2
import os
import time

# ========= Configs de caminho =========
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CASCADE_PATH = os.path.join(BASE_DIR, 'assets', 'haarcascade_frontalface_default.xml')
OUTPUT_PATH  = os.path.join(BASE_DIR, 'saida_anotada.mp4')

# ========= Carrega Haar Cascade =========
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
if face_cascade.empty():
    print("Erro: haarcascade_frontalface_default.xml não foi carregado. Verifique se está em assets/.")
    raise SystemExit

# ========= Abre webcam com tentativa de múltiplos backends =========
def open_camera():
    # Tenta vários índices e backends (útil no Windows)
    candidates = [
        (0, cv2.CAP_DSHOW), (1, cv2.CAP_DSHOW), (2, cv2.CAP_DSHOW),
        (0, cv2.CAP_MSMF),  (1, cv2.CAP_MSMF),  (2, cv2.CAP_MSMF),
        (0, cv2.CAP_ANY),   (1, cv2.CAP_ANY),   (2, cv2.CAP_ANY),
    ]
    for idx, backend in candidates:
        cap = cv2.VideoCapture(idx, backend)
        if cap.isOpened():
            # tenta setar resolução (opcional)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            # pequena espera para estabilizar
            time.sleep(0.2)
            if cap.isOpened():
                return cap
        cap.release()
    return None

cap = open_camera()
if cap is None or not cap.isOpened():
    print("Erro: Não foi possível abrir a webcam. Feche apps que a estejam usando e verifique permissões.")
    raise SystemExit

# ========= Janela + Trackbars =========
cv2.namedWindow('FaceDetect')

def _noop(x): pass

cv2.createTrackbar('scale x100',   'FaceDetect', 110, 200, _noop)  # 1.10–2.00
cv2.createTrackbar('minNeighbors', 'FaceDetect',   5,  20, _noop)  # 1–20
cv2.createTrackbar('minSize',      'FaceDetect',  40, 300, _noop)  # 20–300 px

# ========= Writer de vídeo de saída =========
w  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  or 1280
h  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 720
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (w, h))

# ========= Loop principal =========
prev_t = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Aviso: frame não lido da webcam. Encerrando.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lê parâmetros
    sf = max(1.01, cv2.getTrackbarPos('scale x100', 'FaceDetect') / 100.0)
    mn = max(1,    cv2.getTrackbarPos('minNeighbors', 'FaceDetect'))
    ms = max(20,   cv2.getTrackbarPos('minSize', 'FaceDetect'))

    # Detecção
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=sf,
        minNeighbors=mn,
        minSize=(ms, ms)
    )

    # Desenho
    for (x, y, w0, h0) in faces:
        cv2.rectangle(frame, (x, y), (x + w0, y + h0), (0, 0, 255), 2)
        cv2.putText(frame, "Rosto Detectado", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # FPS simples
    now = time.time()
    fps_est = 1.0 / max(1e-6, (now - prev_t))
    prev_t = now

    # Overlay de parâmetros + FPS
    cv2.putText(frame, f'scale={sf:.2f}  neighbors={mn}  minSize={ms}px  FPS={fps_est:.1f}',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2, cv2.LINE_AA)

    # Mostra e grava
    cv2.imshow('FaceDetect', frame)
    out.write(frame)

    # Sair com 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ========= Finalização =========
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"Vídeo anotado salvo em: {OUTPUT_PATH}")
