import tensorflow as tf
from tensorflow.keras import layers, models
import os
import pathlib

#Cấu hình thông số
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
BASE_PATH = "dataset"

#Thu thập tất cả đường dẫn ảnh và nhãn (Breed name)
data_dir = pathlib.Path(BASE_PATH)

# Quét tất cả file .jpg, .png trong các thư mục sâu nhất
# Cấu trúc: dataset/* (cat/dog)/* (breed)/*.jpg
all_image_paths = list(data_dir.glob('*/*/*')) 
all_image_paths = [str(path) for path in all_image_paths if path.suffix.lower() in ['.jpg', '.jpeg', '.png']]
label_names = sorted(list(set([os.path.basename(os.path.dirname(p)) for p in all_image_paths])))
label_to_index = dict((name, index) for index, name in enumerate(label_names))
all_image_labels = [label_to_index[os.path.basename(os.path.dirname(p))] for p in all_image_paths]

print(f"✅ Đã tìm thấy {len(all_image_paths)} ảnh thuộc về {len(label_names)} loài:")
print(f"🐾 Danh sách nhãn: {label_names}")

#Hàm xử lý ảnh chuyên sâu
def process_path(file_path, label):
    img = tf.io.read_file(file_path)
    img = tf.image.decode_image(img, channels=3, expand_animations=False)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, IMAGE_SIZE)
    img.set_shape([IMAGE_SIZE[0], IMAGE_SIZE[1], 3])
    
    return img, label

#Tạo Dataset từ danh sách file
ds = tf.data.Dataset.from_tensor_slices((all_image_paths, all_image_labels))
ds = ds.shuffle(buffer_size=len(all_image_paths))
ds = ds.map(process_path, num_parallel_calls=tf.data.AUTOTUNE)

#Chia Train/Validation (80/20)
train_count = int(0.8 * len(all_image_paths))
train_ds = ds.take(train_count).batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = ds.skip(train_count).batch(BATCH_SIZE).prefetch(buffer_size=tf.data.AUTOTUNE)

#Xây dựng Model (Sử dụng Transfer Learning + Data Augmentation)
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False #Đóng băng bộ não cũ

model = models.Sequential([
    layers.Input(shape=(224, 224, 3)),
    data_augmentation,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2), #Chống học vẹt
    layers.Dense(len(label_names), activation='softmax') #Đầu ra khớp với số giống pet
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#Huấn luyện
print("\n Bắt đầu huấn luyện...")
model.fit(train_ds, validation_data=val_ds, epochs=105)

#Lưu Model
if not os.path.exists("models"): os.makedirs("models")
model.save("models/pet_breed_model.keras")
print("\n Đã lưu thành công vào 'models/pet_breed_model.keras'")