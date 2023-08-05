import easyocr
import cv2

reader = easyocr.Reader(['en'])  # English only

window_position = (100, 100)
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
cv2.moveWindow('Webcam', window_position[0], window_position[1])

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    # Check if the frame is successfully captured
    if not success:
        print("Error: Unable to capture frame.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    results = reader.readtext(imgS, detail=1, paragraph=False)
    for (bbox, text, prob) in results:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        
        cv2.rectangle(img, tl, br, (0, 255, 0), 2)
        cv2.putText(img, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        print(text)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
