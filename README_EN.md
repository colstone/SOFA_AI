# SOFA_AI: Singing-Oriented Forced Aligner for Automatic Inference

---

 English | [简体中文](https://github.com/colstone/SOFA_AI/blob/main/README.md)

---

## Introduction

SOFA_AI (Singing-Oriented Forced Aligner for Automatic Inference) utilizes [FunASR](https://github.com/alibaba-damo-academy/FunASR) and [SOFA](https://github.com/qiuqiao/SOFA) to achieve the task of directly obtaining phoneme-level labels for target dry vocals in the absence of lyric annotations or speech transcription labels. __This tool can to some extent optimize the phoneme labeling process for DiffSinger, reducing the burden of phoneme labeling.__

__Note:__

__The current code is assisted and corrected by ChatGPT-4, which may contain potential bugs and recognition errors. If any issues are found, you are welcome to raise an issue.__

__This project has plans to integrate with the [openai/whisper](https://github.com/openai/whisper) project, as well as to add ideas about combining ASR with SOFA for confidence level assessment. Stay tuned.__

---

## How to Use

### Environment Setup

- Create and enter a Python 3.10 environment:
  
  ```bash
  conda create -n SOFA_AI python=3.10 -y
  conda activate SOFA_AI
  ```

- Visit the [Pytorch official website](http://www.pytorch.org) and download torch for your device.

- (Optional, to avoid downloading multiple versions of the same library) Install pytorch-lightning separately:
  
  ```bash
  pip install lightning
  ```

- Clone the repository and enter the code directory:
  
  ```bash
  git clone https://github.com/colstone/SOFA_AI.git
  cd SOFA_AI
  ```

- Install the remaining libraries:
  
  ```bash
  pip install -r requirements.txt
  ```

### Inference

- Run the code:
  
  ```bash
  python SOFA_AI.py
  ```
  
  After the code runs, it will download the FunASR model from Modelscope. Once the model is downloaded, the code will ask for:
  
  - __WAV file or folder path__: Drag and drop the WAV file or folder into the command line window.
  
  - __SOFA model path__: Drag and drop the SOFA model into the command line window.
  
  - __Dictionary path__: Drag and drop the dictionary path into the command line window.
  
  - __Phoneme label format (TextGrid or HTK lab)__: Enter `textgrid` or `htk`.

Then, simply wait for the code to finish running.

If you need the text labs or pinyin labs inferred by FunASR for correcting labels or for inference with MFA/SOFA, please go to the `character` or `pinyin` folder and proceed accordingly.

---

## Open Source Projects Used in This Project

[qiuqiao/SOFA: SOFA: Singing-Oriented Forced Aligner](https://github.com/qiuqiao/SOFA)

[alibaba-damo-academy/FunASR: A Fundamental End-to-End Speech Recognition Toolkit and Open Source SOTA Pretrained Models.](https://github.com/alibaba-damo-academy/FunASR)

We sincerely thank the developers/development teams of the above projects.
