import tensorflow as tf
import sys
import os
import csv
from scipy import misc

image_path = sys.argv[1]

regionNr = os.path.splitext(os.path.basename(image_path))[0].lstrip("0")
print(regionNr)
im = misc.imread(image_path)
images_placeholder = tf.placeholder(tf.int32)
label_lines = [line.rstrip() for line
               in tf.gfile.GFile("C:\\tmp\\output_labels.txt")]

with tf.gfile.FastGFile("C:\\tmp\\output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor, {'DecodeJpeg:0': im})
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    human_string = label_lines[top_k[0]]
    cover_type = {
        'udens':    1,
        'koki':     2,
        'zaliens':  3,
        'lauks':    4,
        'cits':     5
    }[human_string]

    with open('missing.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([regionNr, cover_type])
