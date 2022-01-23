# Face Recognition based Attendance System

Attendance System based on Siamese model that validates by estimating similarity of test imaages to those in the database. Uses MTCNN for Face Bounding Box extraction and FaceNet for Embedding extraction. Implementation in TensorFlow. 

- Training

    - Build database of known and required faces
    - Collect images
    - Face Recognition using MTCNN
    - Cropping of face
    - Embeddings extracted using FaceNet
    - Database formulation

- Testing

    - Test image loaded
    - Images in face identified
    - Embeddings extracted for test image faces
    - Compared with database for similarity
    - Identified
    - Export attendance by validation of members in the image

![alt text](https://github.com/sam189239/face_attendance/blob/main/Documents/train_images.jpg?raw=true)

![alt text](https://github.com/sam189239/face_attendance/blob/main/Documents/test1.jpg?raw=true)

![alt text](https://github.com/sam189239/face_attendance/blob/main/Documents/test2.jpg?raw=true)


Project PPT link: 

https://www.canva.com/design/DAE2RE3mjj8/SzGshzEI0ZJeSLPBOKuT_Q/view?utm_content=DAE2RE3mjj8&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent
