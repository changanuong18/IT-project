import os
from icrawler.builtin import BingImageCrawler

BASE_PATH = "dataset"


pet_targets = {
    "Abyssinian": ["Abyssinian cat", "Abyssinian cat breed", "Abyssinian cat kitten", "Abyssinian cat photo", "Abyssinian"],
    "Bengal": ["Bengal cat", "Bengal cat breed", "Bengal cat", "Bengal cat kitten", "Bengal"],
    "Birman": ["Birman cat", "Birman cat breed", "Birman cat kitten", "Birman cat photo", "Birman"],
    "Bombay": ["Bombay cat", "Bombay cat breed", "Bombay cat kitten", "Bombay cat photo", "Bombay Shorthair"],
    "British_Shorthair": ["British_Shorthair cat", "British_Shorthair cat breed", "British_Shorthair cat kitten", "British_Shorthair cat photo", "British_Shorthair"],
    "Egyptian_Mau": ["Egyptian_Mau cat", "Egyptian_Mau cat breed", "Egyptian_Mau cat kitten", "Egyptian_Mau cat photo", "Egyptian_Mau"],
    "Maine_Coon": ["Maine_Coon cat", "Maine_Coon cat breed", "Maine_Coon cat kitten", "Maine_Coon cat photo", "Maine_Coon"],
    "Persian": ["Persian cat", "Persian cat breed", "Persian cat kitten", "Persian cat photo", "Persian"],
    "Ragdoll": ["Ragdoll cat", "Ragdoll cat breed", "Ragdoll cat kitten", "Ragdoll cat photo", "Ragdoll"],
    "Russian_Blue": ["Russian_Blue cat", "Russian_Blue cat breed", "Russian_Blue cat kitten", "Russian_Blue cat photo", "Russian_Blue"],
    "Siamese": ["Siamese cat", "Siamese cat breed", "Siamese cat kitten", "Siamese cat photo", "Siamese"],
    "Sphynx": ["Sphynx cat", "Sphynx cat breed", "Sphynx cat kitten", "Sphynx cat photo", "Sphynx"],
    "American_Bulldog": ["American_Bulldog dog", "American_Bulldog dog breed", "American_Bulldog dog kitten", "American_Bulldog dog photo", "American_Bulldog"],
    "American_pit_bull_terrier": ["American_pit_bull_terrier dog", "American_pit_bull_terrier dog breed", "American_pit_bull_terrier dog kitten", "American_pit_bull_terrier dog photo", "American_pit_bull_terrier"],
    "Basset_hound": ["Basset_hound dog", "Basset_hound dog breed", "Basset_hound dog kitten", "Basset_hound dog photo", "Basset_hound"],
    "Beagle": ["Beagle dog", "Beagle dog breed", "Beagle dog kitten", "Beagle dog photo", "Beagle"],
    "Boxer": ["Boxer dog", "Boxer dog breed", "Boxer dog kitten", "Boxer dog photo", "Boxer"],
    "Chihuahua": ["Chihuahua dog", "Chihuahua dog breed", "Chihuahua dog kitten", "Chihuahua dog photo", "Chihuahua"],
    "English_cocker_spaniel": ["English_cocker_spaniel dog", "English_cocker_spaniel dog breed", "English_cocker_spaniel dog kitten", "English_cocker_spaniel dog photo", "English_cocker_spaniel"],
    "English_setter": ["English_setter dog", "English_setter dog breed", "English_setter dog kitten", "English_setter dog photo", "English_setter"],
    "German_shorthaired": ["German_shorthaired dog", "German_shorthaired dog breed", "German_shorthaired dog kitten", "German_shorthaired dog photo", "German_shorthaired"],
    "Great_pyrenees": ["Great_pyrenees dog", "Great_pyrenees dog breed", "Great_pyrenees dog kitten", "Great_pyrenees dog photo", "Great_pyrenees"],
    "Havanese": ["Havanese dog", "Havanese dog breed", "Havanese dog kitten", "Havanese dog photo", "Havanese"],
    "Japanese_chin": ["Japanese_chin dog", "Japanese_chin dog breed", "Japanese_chin dog kitten", "Japanese_chin dog photo", "Japanese_chin"],
    "Keeshond": ["Keeshond dog", "Keeshond dog breed", "Keeshond dog kitten", "Keeshond dog photo", "Keeshond"],
    "Leonberger": ["Leonberger dog", "Leonberger dog breed", "Leonberger dog kitten", "Leonberger dog photo", "Leonberger"],
    "Miniature_pinscher": ["Miniature_pinscher dog", "Miniature_pinscher dog breed", "Miniature_pinscher dog kitten", "Miniature_pinscher dog photo", "Miniature_pinscher"],
    "Newfoundland": ["Newfoundland dog", "Newfoundland dog breed", "Newfoundland dog kitten", "Newfoundland dog photo", "Newfoundland"],
    "Pomeranian": ["Pomeranian dog", "Pomeranian dog breed", "Pomeranian dog kitten", "Pomeranian dog photo", "Pomeranian"],
    "Pug": ["Pug dog", "Pug dog breed", "Pug dog kitten", "Pug dog photo", "Pug"],
    "Saint_bernard": ["Saint_bernard dog", "Saint_bernard dog breed", "Saint_bernard dog kitten", "Saint_bernard dog photo", "Saint_bernard"],
    "Samoyed": ["Samoyed dog", "Samoyed dog breed", "Samoyed dog kitten", "Samoyed dog photo", "Samoyed"],
    "Scottish_terrier": ["Scottish_terrier dog", "Scottish_terrier dog breed", "Scottish_terrier dog kitten", "Scottish_terrier dog photo", "Scottish_terrier"],
    "Shiba": ["Shiba dog", "Shiba dog breed", "Shiba dog kitten", "Shiba dog photo", "Shiba"],
    "Staffordshire_bull_terrier": ["Staffordshire_bull_terrier dog", "Staffordshire_bull_terrier dog breed", "Staffordshire_bull_terrier dog kitten", "Staffordshire_bull_terrier dog photo", "Staffordshire_bull_terrier"],
}

def download_images():
    cats = ["Abyssinian", "Bengal", "Birman", "Bombay", "British_Shorthair", "Egyptian_Mau", "Maine_Coon", "Persian", "Ragdoll", "Russian_Blue", "Siamese", "Sphynx"]
    dogs = ["American_Bulldog", "American_pit_bull_terrier", "Basset_hound", "Beagle", "Boxer", "Chihuahua", "English_cocker_spaniel", "English_setter","German_shorthaired", "Great_pyrenees", "Havanese", 
            "Japanese_chin", "Keeshond", "Leonberger", "Miniature_pinscher", "Newfoundland", "Pomeranian", "Pug", "Saint_bernard", "Samoyed", "Scottish_terrier", "Shiba", "Staffordshire_bull_terrier"]

    for breed_name, keywords in pet_targets.items():
        parent_folder = "cat" if breed_name in cats else "dog"
        
        save_directory = os.path.join(BASE_PATH, parent_folder, breed_name)
        
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
            print(f"Đã tạo thư mục: {save_directory}")

        print(f"\n Đang xử lý giống: {breed_name} (Thuộc nhóm: {parent_folder.upper()}) ---")

        for word in keywords:
            print(f"Đang tải từ khóa: '{word}'...")
            crawler = BingImageCrawler(
                storage={'root_dir': save_directory},
                downloader_threads=4
            )
            crawler.crawl(keyword=word, max_num=200)

    print(f"\n Xong!")

if __name__ == "__main__":
    download_images()