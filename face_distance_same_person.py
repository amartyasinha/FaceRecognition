import face_recognition

img = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')
img1 = face_recognition.load_image_file('/home/amartya/Pictures/amartya1.jpg')
img2 = face_recognition.load_image_file('/home/amartya/Pictures/amartya2.jpg')

encoded_img = face_recognition.face_encodings(img)[0]
encoded_img1 = face_recognition.face_encodings(img1)[0]
encoded_img2 = face_recognition.face_encodings(img2)[0]

x = face_recognition.face_distance([encoded_img], encoded_img1)
y = face_recognition.face_distance([encoded_img1], encoded_img2)
z = face_recognition.face_distance([encoded_img2], encoded_img)
print('Face distance of 0 and 1: ', x)
print('Face distance of 1 and 2: ', y)
print('Face distance of 2 and 0: ', z)
