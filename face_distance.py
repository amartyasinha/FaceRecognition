import face_recognition

img = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')

encoded_img = face_recognition.face_encodings(img)

print('It has', len(encoded_img), 'face(s)')

for each_face in range(len(encoded_img)):
    next_pic = each_face+1
    if each_face+1 >= len(encoded_img):
        next_pic = 0
    x = face_recognition.face_distance([encoded_img[each_face]], encoded_img[next_pic])
    print('Face distance of {0} and {1}: '.format(each_face, next_pic), x)
