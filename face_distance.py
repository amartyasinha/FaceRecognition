import face_recognition

img = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')

encoded_img = face_recognition.face_encodings(img)

print('It has', len(encoded_img), 'face(s)')

each_face = []
for i in range(1, len(encoded_img)):
    ele = encoded_img[i]
    each_face.append(ele)
x = face_recognition.face_distance(each_face, encoded_img[0])
print('Face distance of Face 0 with 1, 2, and 3: ', x)
