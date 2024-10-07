from chat import *
from tqdm import tqdm
import json
import os
import random
from concurrent.futures import ThreadPoolExecutor

VERSION = "4.0"

def main():
    openai_base_url = input("请输入openai_base_url(default=http://127.0.0.1:11434/v1): ") or "http://127.0.0.1:11434/v1"
    openai_api_key = input("请输入openai_api_key(default=ollama): ") or "ollama"
    openai_model_name = input("请输入openai_model_name(default=Qwen2:14b): ") or "Qwen2:14b"
    prompt = [{"role": "system", "content": input("请输入system_prompt(default=You are a helpful assistant.): ") or "You are a helpful assistant."}]
    mun = 1

    while True:
        p = input(f"请输入第{mun}条问答对(格式: [问题,答案] 输入空字符结束): ")
        if p == "":
            break
        try:
            p = json.loads(p)
            prompt.append({"role": "user", "content": p[0]})
            prompt.append({"role": "assistant", "content": p[1]})

        except (IndexError,json.decoder.JSONDecodeError):
            print("输入格式错误，请重新输入")
            continue
        mun += 1
    chat = Chat(openai_base_url,openai_api_key,openai_model_name).chat

    # 读取可能存在的，未完成的输出
    try:
        with open("output.json","r",encoding="utf-8") as f:
            output_data = json.load(f)

    except (json.decoder.JSONDecodeError,FileNotFoundError):
        output_data = []

    flag = len(output_data)

    with open("input.json","r",encoding="utf-8") as f:
        data = json.load(f)

    print(openai_model_name)
    for dt in tqdm(data):
        # 跳过已完成的部分，去处理未完成的部分
        if flag == 0:
            # 格式化数据
            history1 = data[random.randint(0,len(data))]
            history2 = data[random.randint(0,len(data))]

            futures = []

            with ThreadPoolExecutor(max_workers=3) as executor:
                futures.append(executor.submit(chat,dt["instruction"],dt["input"]))
                futures.append(executor.submit(chat,history1["instruction"],history1["input"]))
                futures.append(executor.submit(chat,history2["instruction"],history2["input"]))

                results = []

                for future in futures:
                    results.append(future.result())

            dt["output"] = results[0]
            history1["output"] = results[1]
            history2["output"] = results[2]
            if history1["input"] != "":
                history1["input"] = "\n" + history1["input"]
            if history2["input"] != "":
                history2["input"] = "\n" + history2["input"]
            instruction_dict = {
            "instruction":dt["instruction"],
            "input":dt["input"],
            "output":dt["output"],
            "history":[
                [history1["instruction"] + history1["input"],history1["output"]],
                [history2["instruction"] + history2["input"],history2["output"]]
            ]
            }
            output_data.append(instruction_dict)
            json_data = json.dumps(output_data, indent=4,ensure_ascii=False)
            # 写入数据
            with open("output.json", "w",encoding="utf-8") as outfile:
                outfile.write(json_data)
        else:
            flag = flag - 1

    print("done.")
    os.system("pause")

if __name__ == "__main__":
    main()
