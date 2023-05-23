import openai
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

openai.api_key = "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"

nltk.download('stopwords')
nltk.download('punkt')


def process_transcript(transcript):
    text_tokens = word_tokenize(transcript)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    tokens_without_sw = " ".join(tokens_without_sw)

    characters_to_remove = [";", "'s", "@", "&", "*",
                            "(", ")", "#", "!", "%", "=",
                            "+", "-", "_", ":", "’"]
    for item in characters_to_remove:
        tokens_without_sw = tokens_without_sw.replace(item, "")

    characters_to_replace = ["?"]

    for item in characters_to_replace:
        tokens_without_sw = tokens_without_sw.replace(item, ".")

    tokens_without_sw = tokens_without_sw.replace(" .", ".")
    tokens_without_sw = tokens_without_sw.replace(" ,", ",")

    return tokens_without_sw


def generate_module(transcript) -> str:
    prompt = f"""
    Your task is help teachers of a college 
    create new, easily understandable study materials
    from the lecture transcript.

    Give me detailed easily understandable 
    module for that particular lecture,
    based on the transcript of that lecture provided in the transcript
    delemited by triple backticks,
    the module should contain all the points and topics
    covered in the transcript explained, 
    you can add in details in the module for
    what you think is required to for the student 
    to understand the topic easily and effectively.

    transcript: ```{transcript}```

    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    res = completion["choices"][0]["message"]["content"]
    return res


def generate_keypoints(transcript) -> str:
    prompt = f"""
    Your task is help teachers of a college 
    create new, easily understandable study materials
    from the lecture transcript.

    Give me all the related key points,
    based on the transcript of that lecture provided in the transcript
    delemited by triple backticks,
    the key points should contain all the points and topics
    covered in the transcript, 
    you can add in details in the keypoints for
    what you think is required to for the student 
    to understand the topic easily and effectively.
    These key points should allow the user to 
    get an overview of all the topics covered in the lecture.

    The keypoints should contain explanation 
    to help with last minute preparations

    transcript: ```{transcript}```

    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    res = completion["choices"][0]["message"]["content"]
    return res
