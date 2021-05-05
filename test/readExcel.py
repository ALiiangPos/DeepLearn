import tensorflow as tf 



''' 
逐行读取数据并分离标签
'''
def read_data (file_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    key , value = reader.read(file_queue)
    defaults = [ [0] , [0] , [0] , [0] , [0],[0] ]
    cvscolumn = tf.decode_csv(value , defaults)
    featurecolumn = [ i for i in cvscolumn[0:-1] ]
    labelcolumn = cvscolumn[-1] 
    return tf.stack(featurecolumn) , labelcolumn

''' 
生成队列中的批次数据
'''
def create_pipeline( filename , batch_size , num_epochs=None):
    file_queue = tf.train.string_input_producer( [filename] ,num_epochs = num_epochs )
    feature , label = read_data(file_queue)
    min_after_dequeue = 1000 
    capacity = min_after_dequeue +batch_size 
    feature_batch  , label_batch = tf.train.shuffle_batch(
        [feature , label ] ,batch_size = batch_size ,capacity = capacity ,min_after_dequeue = min_after_dequeue 
    ) 
    return feature_batch , label_batch 
x_train_batch  , y_train_batch = create_pipeline('data.csv' , 32 , num_epochs=100)


