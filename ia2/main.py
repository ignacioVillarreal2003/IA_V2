import replicate

output = replicate.run(
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
  input={
    "debug": False,
    "top_k": 50,
    "top_p": 1,
    "prompt": "Escribime una descripcion de los humanos en 50 palabras.",
    "temperature": 0.5,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 500,
    "min_new_tokens": -1
  }
)

output = replicate.run(
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
  input={
    "debug": False,
    "top_k": 50,
    "top_p": 1,
    "prompt": "En base a lo anterior escribime un resumen en 20 palabras.",
    "temperature": 0.5,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 500,
    "min_new_tokens": -1
  }
)

result = ""
for e in output:
    result += e
print(result)