FOLDER="C:\\Users\\katri_000\\OneDrive\\MasterThesis\\jseg-python\\image_retraining\missing\\"
for file in $(ls $FOLDER); do
	python label_image.py "${FOLDER}${file}"
done
