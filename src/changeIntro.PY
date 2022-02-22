'''
 代码修改说明
'''

'''
1、xrange
xrange是python2.0的用法
python3.0+改成了range
'''

'''
2、print
print"Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test)是python2.0的用法
python3.0+改成了print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
'''

'''
3、digit_counts.iteritems()
iteritems改成items
'''

'''
4、cPickle
cPickle是python2.0的用法
python3.0+pickle
'''

'''
5、mnist.pkl.gz路径
f = gzip.open('../data/mnist.pkl.gz', 'rb')
改为f = gzip.open('./data/mnist.pkl.gz', 'rb')
'''

'''
6、pickle默认参数
python3里的pickle的load的参数中默认encoding是ASCII
training_data, validation_data, test_data = pickle.load(f,encoding="bytes")
'''

'''
7、object of type 'zip' has no len()
在python3中，zip生成的是一个迭代器，所以不能直接用len来得到其长度。
将load_data_wrapper()里的有用到zip语句，都将zip(...)改为list(zip(...))
如  training_data = zip(training_inputs, training_results)
改为training_data = list(zip(training_inputs, training_results))
'''