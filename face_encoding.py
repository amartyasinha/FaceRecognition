import face_recognition

img = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')

encoded_img = face_recognition.face_encodings(img)

print('It has', len(encoded_img), 'face(s)')

for each_face in range(len(encoded_img)):
    print("Encoding of face [{}]: ".format(each_face+1))
    print(encoded_img[each_face])
