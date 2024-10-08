# `AutoData`说明文档

## 简介

`AutoData`是一个用于生成特定数据集的项目，它通过读取 `input.json` 文件中的数据集，并根据预定义的系统提示和聊天历史生成新的数据集。该项目支持任何支持 OpenAI API 的模型。

## 功能

- 读取 `input.json` 文件中的数据集。
- 根据预定义的系统提示和聊天历史生成新的数据集。
- 支持任何支持 OpenAI API 的模型。

## 使用方法

1. 确保你已经安装了 Python 3.6 或更高版本。
2. 克隆或下载本项目到本地。
3. 在项目根目录下创建一个名为 `input.json` 的文件，并按照以下格式填充数据集(可以直接使用alpaca格式的数据集)：

```json
[
	{
        "instruction": "你好，今天天气怎么样？",
    },
	{
        "instruction": "我想去旅游，有什么推荐的地方吗？",
    }
]
```

4. 在项目根目录下运行以下命令：

```bash
python main.py
```

5. 等待程序运行完成，生成的数据集将保存在 `output.json` 文件中。

## 注意事项

- 请确保 `input.json` 文件中的数据集格式正确。
- 请确保你已经正确配置了 OpenAI API 的访问密钥。

## 贡献

如果你有任何改进意见或想要贡献代码，请随时提交 Pull Request 或创建 Issue。
