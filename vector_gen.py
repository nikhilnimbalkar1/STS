
import tensorflow as tf
import tensorflow_hub as hub

class embedText:
    def __init__(self):
        self.embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
        tf.get_logger().setLevel('INFO')
    def embed_text(self,txt1,txt2):
        with tf.Session() as session:
            session.run([tf.global_variables_initializer(), tf.tables_initializer()])
            self.vector1 = session.run(self.embed(txt1))
            self.vector2 = session.run(self.embed(txt2))
            session.close()
    def get_vec1(self):
        return self.vector1
    def get_vec2(self):
        return self.vector2

