	===============

CHATGTP on it's api parameters:

    - The "temperature" field in a ChatGPT API request is a parameter that determines the level of randomness or creativity in the generated response.

    Temperature is a measure of the entropy of the system, and in the context of natural language processing, it determines the level of variation in the model's responses. A higher temperature value will result in more varied and unpredictable responses, while a lower temperature value will produce more conservative and predictable responses.

    In the context of a ChatGPT API request, the temperature value can be set to a value between 0 and 1, with 0 being the most conservative and 1 being the most creative. A temperature value of around 0.5 is often used as a default, as it strikes a balance between creativity and coherence in the generated responses.

    Note that the actual temperature value used in generating the response can be slightly different from the value specified in the API request, as the model may adjust the temperature value based on the context and other factors.


    - The maxTokens parameter is important because it allows you to control the length and specificity of the model's output. If you set maxTokens to a low value, the generated text will be relatively short and focused on the most salient aspects of the prompt. If you set maxTokens to a high value, the generated text will be longer and more detailed, potentially covering a wider range of topics and ideas.

    However, setting maxTokens too high can also lead to the model generating text that is unfocused or irrelevant to the prompt. Therefore, it is important to experiment with different values of maxTokens to find the optimal balance between length and relevance for your specific application.

    It is worth noting that different engines may have different maximum values for maxTokens


    >Is there an equation that returns the number of api tokens consumed by the request, depending on the max_token input parameter of the api?

    Yes, there is an equation that can be used to estimate the number of tokens consumed by an API request to ChatGPT, based on the max_tokens parameter that you set in your request.

    The equation is:

        tokens = max(max_tokens, 4) + ceil(log2(num_samples))

        num_samples is the number of samples or responses that you request from the API

        It's worth noting that this equation is an estimate, and the actual number of tokens consumed by a request may vary depending on factors such as the length and complexity of the generated text, as well as the specific parameters and settings used in the request.



--------

Not entirely sure: GPT-4 is still inventing stuff, fixing it may be harder than they admit - for example you can still trick an ML vision model with a random image. (also: there must be *some* FUD in the marketing...) See:

https://www.youtube.com/watch?v=SjhIlw3Iffs&t=1068s

