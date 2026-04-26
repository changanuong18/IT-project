import tensorflow as tf
import numpy as np
import os

# Prediction
def predict_pet(model_path, img_path):
    #Check that image exist
    if not os.path.exists(img_path):
        print(f"❌ Lỗi: Không tìm thấy file ảnh tại: {img_path}")
        return

    #Load model
    model = tf.keras.models.load_model(model_path)
    
    #Load and Process the image
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = img_array / 255.0
    img_array = tf.expand_dims(img_array, 0)  

    #Predict
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    #List
    class_names = ['Abyssinian', 'American_Bulldog', 'American_pit_bull_terrier', 'Basset_hound', 'Beagle', 'Bengal', 'Birman', 'Bombay', 'Boxer', 'British_Shorthair', 'Chihuahua', 'Egyptian_Mau',
                   'English_cocker_spaniel', 'English_setter','German_shorthaired', 'Great_pyrenees', 'Havanese', 'Japanese_chin', 'Keeshond', 'Maine_Coon', 'Persian', 'Ragdoll', 'Russian_Blue', 'Siamese', 'Sphynx',
                   'Leonberger', 'Miniature_pinscher', 'Newfoundland', 'Pomeranian', 'Pug', 'Saint_bernard', 'Samoyed', 'Scottish_terrier', 'Shiba', 'Staffordshire_bull_terrier']
    
    index_ket_qua = np.argmax(score)
    ten_loai = class_names[index_ket_qua]
    do_tin_tuong = 100 * np.max(score)

    print("\n" + "="*30)
    print(f"🐾 KẾT QUẢ: {ten_loai}")
    print(f"📊 Độ tin tưởng: {do_tin_tuong:.2f}%")
    print("="*30)
    

    print("\nChi tiết bảng điểm:")
    for i, name in enumerate(class_names):
        print(f" - {name}: {score[i]*100:.2f}%")

#Run
if __name__ == "__main__":
    MODEL_FILE = r"models/pet_breed_model.keras" 
    IMAGE_TO_TEST = r"test_images/img.jpg"
    
    predict_pet(MODEL_FILE, IMAGE_TO_TEST)