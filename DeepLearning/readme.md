### 安装环境

使用conda命令安装环境

```python

conda env create --prefix="E:\hk\python\envs\pytorch" -f "用具体yaml文件路径替换"

```

'E:\hk\python\envs\pytorch'这个路径可以自定义，最后一个文件夹的名字就是环境的名字

之后在编译器中

```conda
conda activate pytorch
```

每个文件夹里的项目都如下操作：  
先运行data_preprocess.ipynb，再运行model_Training.ipynb

