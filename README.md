# SOFA_AI: Singing-Oriented Forced Aligner for Automatic Inference

---

[English](https://github.com/colstone/SOFA_AI/blob/main/README_EN.md) | 简体中文

---

## 介绍

SOFA_AI（Singing-Oriented Forced Aligner for Automatic Inference）是利用[FunASR](https://github.com/alibaba-damo-academy/FunASR)和[SOFA](https://github.com/qiuqiao/SOFA)，以达到目标干声在无歌词标注或者无语音转写标注的情况下，直接获取目标干声音素级别标注的任务。__此工具能一定程度上优化DiffSinger的音素标注流程，减轻一定的音素标注压力。__

__注意：__

__目前的代码由ChatGPT-4辅助提供以及改正，可能会存在潜在的Bug，且会存在潜在的识别错误。如果发现任何问题，欢迎提出issue。__

__此项目已有缝合[openai/whisper](https://github.com/openai/whisper)项目，以及添加ASR与SOFA结合的置信度的想法，敬请期待。__

---

## 使用方法

### 环境配置

- 创建一个python 3.10的环境并进入：
  
  ```bash
  conda create -n SOFA_AI python=3.10 -y
  conda activate SOFA_AI
  ```

- 访问[Pytorch官网](http://www.pytorch.org)，下载适用于你的设备的torch。

- （可选择，以防止下载一堆版本号不同的相同库）单独安装pytorch-lightning：
  
  ```bash
  pip install lightning
  ```

- 克隆仓库，进入代码目录：
  
  ```bash
  git clone https://github.com/colstone/SOFA_AI.git
  cd SOFA_AI
  ```

- 安装剩下的库：
  
  ```bash
  pip install -r requirements.txt
  ```

### 推理

- 运行代码：
  
  ```bash
  python SOFA_AI.py
  ```
  
  代码运行后，将会从Modelscope下载FunASR模型。当模型下载完毕，代码将询问：
  
  - __WAV文件或者文件夹路径__：将WAV文件或者文件夹拖拽进命令行窗口；
  
  - __SOFA模型路径__：将SOFA模型拖拽进命令行窗口；
  
  - __词典路径__：将词典路径拖拽进命令行窗口；
  
  - __音素标注格式（TextGrid或HTK lab）__：输入`textgrid`或者`htk`。

然后什么都不用管，等代码跑完就行。

如果你需要FunASR推理出来的文字lab或者拼音lab，以修正标注或者给MFA/SOFA进行推理，请到`character`或者`pinyin`文件夹，进行操作。

---

## 本项目所使用的开源项目

[qiuqiao/SOFA: SOFA: Singing-Oriented Forced Aligner](https://github.com/qiuqiao/SOFA)

[alibaba-damo-academy/FunASR: A Fundamental End-to-End Speech Recognition Toolkit and Open Source SOTA Pretrained Models.](https://github.com/alibaba-damo-academy/FunASR)

由衷感谢以上项目的开发者/开发团队。
