from openai import OpenAI

VISSION = "4.0"

class Chat:
    def __init__(self,base_url,api_key,model,history: list = [{"role": "system", "content": "You are a helpful assistant."}]):
        self.client = OpenAI(api_key=api_key,base_url=base_url)
        self.history = history
        self.model = model

    def chat(self,instruction,input):
        self.history.append({"role": "user", "content": instruction + "\n" + input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            stream=False,
            temperature=1.5,
            top_p= 1
        )


        # 读取模型的回答
        message = response.choices[0].message.content

        # 去除多余的换行符并输出生成结果
        output = message.rstrip()
        print(f"\ninstruction:{instruction}\ninput:{input}\noutput:{output}")
        
        return output


if __name__ == "__main__":
    Chat(base_url="http://127.0.0.1:11434/v1", api_key="ollama", model="Qwen2:14b").chat("你好","")
