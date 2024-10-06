import cv2
from pyzbar.pyzbar import decode
import webbrowser


def decode_qr(frame):
    
    decoded_objects = decode(frame)
    for obj in decoded_objects:
      
        qr_data = obj.data.decode('utf-8')
        
        if qr_data.startswith('http://') or qr_data.startswith('https://'):
            print(f"Opening URL: {qr_data}")
            webbrowser.open(qr_data)  
        
        elif ',' in qr_data:
            coords = qr_data.split(',')
            if len(coords) == 2:
                try:
                    latitude = float(coords[0])
                    longitude = float(coords[1])
                    print(f"Opening coordinates: Latitude: {latitude}, Longitude: {longitude}")
                    
                    maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
                    webbrowser.open(maps_url)
                except ValueError:
                    print("Invalid coordinates format in QR code.")

       
        points = obj.polygon
        if len(points) == 4:
          
            for j in range(4):
                cv2.line(frame, (points[j].x, points[j].y), (points[(j + 1) % 4].x, points[(j + 1) % 4].y), (0, 255, 0), 3)

            
            cv2.putText(frame, qr_data, (points[0].x, points[0].y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while True:
    
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    frame = decode_qr(frame)
    
    cv2.imshow('QR Code Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
