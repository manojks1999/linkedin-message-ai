class AiModel:

    def __init__(self, llm, model):
        self.__llm = llm
        self.__model = model

    def chat_completion(self, message):
        print("jkdsfdsfs", message, self.__llm.memory)
        self.__llm.memory.append({
            'role': 'user',
            'content': message
        })
        print("kjdsoisdfsd", self.__llm.memory)
        completion = self.__llm.chat_completion(self.__llm.memory, self.__model)
        if completion is None or len(completion.choices) < 1:
            print(f"No response choice given")
            content = ""
        elif completion.choices[0].finish_reason == "length":
            if self.allow_truncated:
                content = completion.choices[0].message.content
            else:
                print(
                    f"Response truncated because of finish reason = length."
                    f" Use --allow_truncated option to process truncated responses."
                )
                content = ""
        else:
            content = completion.choices[0].message.content
            print(f"Response received: \n{content}")
        return content
        