from g4f.client import Client
from .config_message import MEMORY_MESSAGE

class NotGiven:
    ...

    @staticmethod
    def remove_not_given(obj):
        if isinstance(obj, NotGiven):
            return None
        if isinstance(obj, dict):
            return {k: NotGiven.remove_not_given(v) for k, v in obj.items() if v is not NOT_GIVEN}
        if isinstance(obj, list):
            return [NotGiven.remove_not_given(v) for v in obj if v is not NOT_GIVEN]
        return obj


NOT_GIVEN = NotGiven()


class OpenAiLlmClient:
    def __init__(self):
        # self.client = OpenAI(api_key=api_key)
        self.client = Client()
        self.memory = MEMORY_MESSAGE
        
    def get_models(self):
        pass

    def chat_completion(
        self,
        messages,
        model,
        frequency_penalty = NOT_GIVEN,
        logit_bias = NOT_GIVEN,
        logprobs = NOT_GIVEN,
        max_tokens = NOT_GIVEN,
        n = NOT_GIVEN,
        presence_penalty = NOT_GIVEN,
        response_format = NOT_GIVEN,
        stop = NOT_GIVEN,
        temperature = NOT_GIVEN,
        top_logprobs = NOT_GIVEN,
        top_p = NOT_GIVEN,
    ):
        input_kwargs = dict(
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            stop=stop,
            temperature=temperature,
            top_logprobs=top_logprobs,
            top_p=top_p,
        )
        return self.client.chat.completions.create(**NotGiven.remove_not_given(input_kwargs))
