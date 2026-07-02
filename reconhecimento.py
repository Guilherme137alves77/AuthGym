import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision 

# Configura o detector de rostos usando a nova API 
BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions

# Criando o detector (usa o modelo padrão  embutido na biblioteca)
options = FaceDetectorOptions(  base_options=BaseOptions(model_asset_path='detector.tflite'))
# Inicializa o detector de rostos oficial com base nas opçoes que configura acima 
detector = FaceDetector.create_from_options(options)

# Inicializa um loop que continuará rodando enquanto a wabcam conseguir enviar 
webcam = cv2.VideoCapture(0)

# Inicia um loop que continua rodando enquanto a webcam conseguir enviar com sucesso 
while webcam.isOpened():
    
    # Le o grame atual da webcam.. 'validaçao' é um booleano (true/false) e 'frame' é a imagem em si 
    validacao, frame = webcam.read()

    #Se o sistema nao conseguir ler a imagem da câmera, exibe um aviso e encerra o loop 
    if not validacao:
        print("Erro ao carregar o fram da câmera.")
        break

    # O OpenCV lé imagens em formato BGR, mas o MediaPipe precisa do formato RGB. Aqui fazemos a conversao 
    # O OpenCV lê imagens em formato BGR, mas o MediaPipe precisa do formato RGB. Aqui fazemos a conversão.
    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Converte a matriz de pixels do OpenCV para o formato de imagem nativo exigido pelo MediaPipe
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imagem_rgb)
    
    # Executa a inteligência artificial para detectar os rostos presentes na imagem convertida
    detection_result = detector.detect(mp_image)

    # Verifica se a inteligência artificial encontrou pelo menos um rosto na imagem
    if detection_result.detections:
        
        # Percorre cada um dos rostos detectados na imagem (caso haja mais de um)
        for detection in detection_result.detections:
            
            # Extrai as coordenadas da caixa delimitadora (caixa que envolve o rosto detectado)
            bbox = detection.bounding_box
            
            # Desenha um retângulo verde na imagem original (frame) usando as coordenadas do rosto
            # (int(bbox.origin_x), int(bbox.origin_y)) é o ponto superior esquerdo da caixa do rosto
            # (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height)) é o ponto inferior direito
            # (0, 255, 0) define a cor verde no padrão BGR do OpenCV
            # O número 2 define a espessura da linha do retângulo em pixels
            cv2.rectangle(frame, 
                          (int(bbox.origin_x), int(bbox.origin_y)), 
                          (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height)), 
                          (0, 255, 0), 2)

    # Abre uma janela no computador exibindo a imagem da webcam com os retângulos desenhados
    cv2.imshow("Rostos na sua webcam", frame)
    
    # Aguarda 5 milissegundos pela pressão de uma tecla. Se a tecla pressionada for 'ESC' (código 27), fecha o programa
    if cv2.waitKey(5) == 27:
        break


# Desliga e libera a webcam para que outros aplicativos do computador possam usá-la
webcam.release()

# Fecha todas as janelas criadas pelo OpenCV na tela do seu computador
cv2.destroyAllWindows()