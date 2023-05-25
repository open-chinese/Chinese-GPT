# 关于Chinese-GPT
中文GPT项目包括了从数据准备、模型训练再到模型推理的完整流程。

该项目的目的是，让GPT模型的学习、训练、线上推理变得更简单。

我们的第一个版本，将以GPT-NeoX模型为基础，从零开始，一步一步训练一个诗歌版的中文GPT模型，这个模型并不是简单的生成诗歌，而是可以通过对话的方式进行交互。我们可以简单理解它是一个中文诗歌版的Chat GPT，之所以限定在中文诗歌，是因为目前仅仅是在消费级的显卡上进行训练以及推理。出于算力以及数据集的限制，我们先定一个可行一点的目标。

# 版本号 V1.0 LiBai
第一版的项目代号是诗人李白


# 项目结构

- config

  不同参数规模的model config文件
- vocab
  
  中文词表文件，文件命名统一为 vocab_{len-of-vocab}.txt
- training_data_process

  一般我们为了避免一次性load过多的训练数据，会将GB甚至是TB级别的数据切分为小文件
  
  training_data_process 是专门将大文件处理为我们训练所需的格式，不过这里并不会做tokenization。
- train.py
  
  训练文件，为了避免过于繁杂的参数输入，我们尽量将训练的参数设置在代码中，所以你只需要简单的运行
```
  # python train.py
```

- generate.py

  等训练完了之后，可以通过generate.py做一些实验

- evaluate.py

  这个文件是为了我们可以在训练完了之后，批量跑一些标准的测试集。

- util

  工具包

# TODO list

- Dataset prepare
- Training code
- Base model
- Alignment
- Inference
- Testing

