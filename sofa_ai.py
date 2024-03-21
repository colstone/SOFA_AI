import os
import re
from pathlib import Path
from funasr import AutoModel
import pypinyin
import subprocess
import shutil

# 用户输入
wav_path = input("请输入wav文件或文件夹路径: ")
sofa_model_path = input("请输入SOFA模型路径: ")
dictionary_path = input("请输入词典路径: ")
annotation_format = input("请输入音素标注格式（TextGrid或HTK lab）: ")

# 确定是单个文件还是文件夹
if os.path.isfile(wav_path):
    wav_files = [wav_path]
    print(f"已找到wav文件 | {wav_path}")
elif os.path.isdir(wav_path):
    wav_files = [str(path) for path in Path(wav_path).rglob('*.wav')]
    for file in wav_files:
        print(f"已找到wav文件 | {file}")

# 加载FunASR模型
#model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc")
model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad")
print(f"已加载FunASR权重")

# 创建输出文件夹
character_dir = Path("characters")
character_dir.mkdir(exist_ok=True)
pinyin_dir = Path("pinyin")
pinyin_dir.mkdir(exist_ok=True)

# 对每个wav文件处理
for wav_file in wav_files:
    print(f"开始推理 | {wav_file}")
    results = model.generate(input=wav_file)  # 这里假设`model.generate`返回一个字典列表
    
    # 新增：假定每个结果字典中都有'text'键，我们将这些文本内容拼接起来
    full_text = ''.join([result['text'] for result in results])
    
    # 过滤获取汉字，这里使用修改后的full_text变量
    characters = re.sub(r'[a-zA-Z\s]', '', full_text)
    lab_file_name = Path(wav_file).stem + ".lab"
    
    # 保存语音识别结果
    with open(character_dir / lab_file_name, 'w', encoding='utf-8') as f:
        f.write(characters)
    print(f"已保存语音识别结果 | {character_dir / lab_file_name}")
    
    # 转换为拼音并保存
    pinyin_content = ' '.join(pypinyin.lazy_pinyin(characters, style=pypinyin.Style.NORMAL))
    with open(pinyin_dir / lab_file_name, 'w', encoding='utf-8') as f:
        f.write(pinyin_content)
    print(f"已保存拼音 | {pinyin_dir / lab_file_name}")

# 将pinyin文件复制到wav文件所在目录
for pinyin_file in pinyin_dir.iterdir():
    target_path = Path(wav_path) / pinyin_file.name if Path(wav_path).is_dir() else Path(wav_path).parent / pinyin_file.name
    shutil.copy(pinyin_file, target_path)
    print(f"已复制拼音文件到 | {target_path}")

# 调用SOFA进行推理
def run_sofa_inference(sofa_script_path, ckpt, folder, dictionary, out_format):
    
    cmd = [
        'python', sofa_script_path,
        '--ckpt', ckpt,
        '--folder', folder,
        '--dictionary', dictionary,
        '--out_formats', out_format
    ]
    subprocess.run(cmd, check=True)

# SOFA infer.py脚本的路径
sofa_script_path = 'infer.py'  # 请根据实际路径进行修改

# 执行SOFA音素标注
run_sofa_inference(
    sofa_script_path=sofa_script_path,
    ckpt=sofa_model_path,  # 此前已由用户输入
    folder=wav_path,  # 用户指定的wav文件或文件夹路径
    dictionary=dictionary_path,  # 此前已由用户输入
    out_format=annotation_format  # 此前已由用户输入
)

print("SOFA推理完成，全流程结束。")

