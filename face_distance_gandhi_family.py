import face_recognition

img_indira = face_recognition.load_image_file('/home/amartya/Pictures/indira.jpg')
img_sonia = face_recognition.load_image_file('/home/amartya/Pictures/sonia.jpg')
img_priyanka = face_recognition.load_image_file('/home/amartya/Pictures/priyanka.jpeg')

sign_indira = face_recognition.face_encodings(img_indira)[0]
sign_sonia = face_recognition.face_encodings(img_sonia)[0]
sign_priyanka = face_recognition.face_encodings(img_priyanka)[0]

x = face_recognition.face_distance([sign_indira], sign_sonia)
y = face_recognition.face_distance([sign_sonia], sign_priyanka)
z = face_recognition.face_distance([sign_priyanka], sign_indira)
print('Face distance of Indira and Sonia: ', x)
print('Face distance of Sonia and Priyanka: ', y)
print('Face distance of Priyanka and Indira: ', z)
