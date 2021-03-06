# python
此仓库始于用python来做数字货币和量化  
现在拓展了方向，更多来用于整体的学习与练习  
**注：在win上markdown用Typroa**

## 注意事项：
Python 3最重要的新特性大概要算是对文本和二进制数据作了更为清晰的区分。文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。  
Python 3不会以任意隐式的方式混用str和bytes，正是这使得两者的区分特别清晰。  
你不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然），也不能将字符串传入参数为字节包的函数（反之亦然）.  
gb18030 和 utf-8 的区别。utf-8 是国际通用字符编码，gb18030是新出的国家标准，不仅包括了简体和繁体，也包括了一些不常见的中文，容错率更高

## 关于提升效率
默认类object不仅是str类的容器，而且不能齐整的适用于某一种数据类型。字符串str类型的日期在数据处理中是非常低效的，同时内存效率也是低下的  
1. 所以**时间尽量改为datetime**,如：pd.to_datetime★参数里加上format = '%Y-%m-%d %H:%M:%S"会更快
2. **使用了timing装饰器**，装饰器称为@timeit, 这个装饰器模仿了Python标准库中的timeit.repeat() 方法，  
   但是它可以返回函数的结果，并且打印多次重复调试的平均运行时间。  
   将装饰器@timeit放在函数上方，每次运行函数时可以同时打印该函数的运行时间。  
3. **用.itertuples()和.iterrow()遍历**  
   .itertuples()为每行生成一个nametuple类，行的索引值作为nametuple类的第一个元素  
   nametuple是来自Python的collections模块的数据结构，该结构和Python中的元组类似，但是可以通过属性查找可访问字段。  
   .iterrows()为DataFrame的每行生成一组由索引和序列组成的元组。  
   与.iterrows()相比，.itertuples()运行速度会更快一些。
4. **df.apply()** ，但这仍然不够快，原因是.apply()内部尝试在Cython迭代器上完成循环。  
   但是在这种情况下，lambda中传递了一些无法在Cython中处理的输入  
5. **.isin()筛选** ,如：定义每个时段的布尔型数组(Boolean)  

 ``` 
  peak_hours = df.index.hour.isin(range(17, 24))  
  shoulder_hours = df.index.hour.isin(range(7, 17))
  off_peak_hours = df.index.hour.isin(range(0, 7)) 

  # 计算不同时段的电费  

  df.loc[peak_hours, 'cost_cents'] = df.loc[peak_hours, 'energy_kwh'] * 28
  df.loc[shoulder_hours,'cost_cents'] = df.loc[shoulder_hours, 'energy_kwh'] * 20
  df.loc[off_peak_hours,'cost_cents'] = df.loc[off_peak_hours, 'energy_kwh'] * 12

  ```
   比.iterrows()方法，比.apply()方法快  
6. **df.cut()**  
7. **HDFstore**  
   Pandas的HDFstore方法可以将DataFrame存储在HDF5文件中，可以有效读写，同时仍然保留DataFrame各列的数据类型和其他元数据。  
   它是一个类似字典的类，因此可以像Python中的dict类一样读写
   
   ```
   # 创建存储类文件并命名 `processed_data`
   data_store = pd.HDFStore('processed_data.h5')

   #将DataFrame写入存储文件中，并设置键（key） 'preprocessed_df'
   data_store['preprocessed_df'] = df
   data_store.close()
   ```
8. **Numpy Vectorization**  
   访问局部性（locality of reference）
   在计算机科学中，访问局部性，也称为局部性原理，是取决于存储器访问模式频繁访问相同值或相关存储位置的现象的术语。
   访问局部性有两种基本类型——时间和空间局部性。时间局部性是指在相对较小的持续时间内对特定数据和/或资源的重用。空间局部性是指在
   相对靠近的存储位置内使用数据元素。当数据元素被线性地排列和访问时，例如遍历一维数组中的元素，发生顺序局部性，即空间局部性的特殊情况。  
## 总结
1、如果确定需要使用循环，则应始终选择apply方法。
2、否则，vectorization总是更好的，因为它更快！
