# Models

## Overview

The OpenAI API is powered by a diverse set of models with different capabilities and price points. You can also make limited customizations to our original base models for your specific use case with fine-tuning.

| MODELS | DESCRIPTION |
| --- | --- |
| GPT-3.5 | A set of models that improve on GPT-3 and can understand as well as generate natural language or code |
| DALL·E | A model that can generate and edit images given a natural language prompt |
| Whisper | A model that can convert audio into text |
| Embeddings | A set of models that can convert text into a numerical form |
| Codex (Limited beta) | A set of models that can understand and generate code, including translating natural language to code |
| Moderation | A fine-tuned model that can detect whether text may be sensitive or unsafe |
| GPT-3 | A set of models that can understand and generate natural language |

We have also published open source models including Point-E, Whisper, Jukebox, and CLIP.

Visit our model index for researchers to learn more about which models have been featured in our research papers and the differences between model series like InstructGPT and GPT-3.5.

## GPT-3.5

GPT-3.5 models can understand and generate natural language or code. Our most capable and cost effective model is gpt-3.5-turbo which is optimized for chat but works well for traditional completions tasks as well.

| LATEST MODEL | DESCRIPTION | MAX REQUEST | TRAINING DATA |
| --- | --- | --- | --- |
| gpt-3.5-turbo | Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003. Will be updated with our latest model iteration. | 4,096 tokens | Up to Sep 2021 |
| gpt-3.5-turbo-0301 | Snapshot of gpt-3.5-turbo from March 1st 2023. Unlike gpt-3.5-turbo, this model will not receive updates, and will only be supported for a three month period ending on June 1st 2023. | 4,096 tokens | Up to Sep 2021 |
| text-davinci-003 | Can do any language task with better quality, longer output, and consistent instruction-following than the curie, babbage, or ada models. Also supports inserting completions within text. | 4,000 tokens | Up to Jun 2021 |
| text-davinci-002 | Similar capabilities to text-davinci-003 but trained with supervised fine-tuning instead of reinforcement learning | 4,000 tokens | Up to Jun 2021 |
| code-davinci-002 | Optimized for code-completion tasks | 4,000 tokens | Up to Jun 2021 |

We recommend using `gpt-3.5-turbo` while experimenting since it will yield the best results. Once you’ve got things working, we encourage trying the other models to see if you can get the same results with lower latency or cost.

    Note: OpenAI models are non-deterministic, meaning that identical inputs can yield different outputs. Setting temperature to 0 will make the outputs mostly deterministic, but a small amount of variability may remain.

### Feature-specific models

While the new `gpt-3.5-turbo` model is optimized for chat, it works very well for traditional completion tasks. The original GPT-3.5 models are optimized for text completion.

Our endpoints for creating embeddings and editing text use their own sets of specialized models.

### Turbo

Turbo is the same model family that powers ChatGPT. It is optimized for conversational chat input and output but does equally well on completions when compared with the Davinci model family. Any use case that can be done well in ChatGPT should perform well with the Turbo model family in the API.

The Turbo model family is also the first to receive regular model updates like ChatGPT.

Good at: **Conversation and text generation**

### Davinci

Davinci is the most capable model family and can perform any task the other models (ada, curie, and babbage) can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and creative content generation, Davinci will produce the best results. These increased capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other models.

Another area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.

Good at: **Complex intent, cause and effect, summarization for audience**

### Curie

Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.

Good at: **Language translation, complex classification, text sentiment, summarization**

### Babbage

Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.

Good at: **Moderate classification, semantic search classification**

### Ada

Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.

Good at: **Parsing text, simple classification, address correction, keywords**

    Note: Any task performed by a faster model like Ada can be performed by a more powerful model like Curie or Davinci.

## Finding the right model

Experimenting with gpt-3.5-turbo is a great way to find out what the API is capable of doing. After you have an idea of what you want to accomplish, you can stay with gpt-3.5-turbo or another model and try to optimize around its capabilities.

You can use the GPT comparison tool that lets you run different models side-by-side to compare outputs, settings, and response times and then download the data into an Excel spreadsheet.

### DALL·E

DALL·E is a AI system that can create realistic images and art from a description in natural language. We currently support the ability, given a prommpt, to create a new image with a certain size, edit an existing image, or create variations of a user provided image.

The current DALL·E model available through our API is the 2nd iteration of DALL·E with more realistic, accurate, and 4x greater resolution images than the original model. You can try it through the our Labs interface or via the API.

### Whisper

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. The Whisper v2-large model is currently available through our API with the whisper-1 model name.

Currently, there is no difference between the open source version of Whisper and the version available through our API. However, through our API, we offer an optimized inference process which makes running Whisper through our API much faster than doing it through other means. For more technical details on Whisper, you can read the paper.

### Embeddings

Embeddings are a numerical representation of text that can be used to measure the relateness between two pieces of text. Our second generation embedding model, text-embedding-ada-002 is a designed to replace the previous 16 first-generation embedding models at a fraction of the cost. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about our latest embedding model in the announcement blog post.

### Codex (`Limited beta`)
The Codex models are descendants of our GPT-3 models that can understand and generate code. Their training data contains both natural language and billions of lines of public code from GitHub. Learn more.

They’re most capable in Python and proficient in over a dozen languages including JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, and even Shell.

We currently offer two Codex models:

| LATEST MODEL | DESCRIPTION | MAX REQUEST | TRAINING DATA |
| --- | --- | --- | --- |
| code-davinci-002 | Most capable Codex model. Particularly good at translating natural language to code. In addition to completing code, also supports inserting completions within code. | 8,000 tokens | Up to Jun 2021 |
| code-cushman-001 | Almost as capable as Davinci Codex, but slightly faster. This speed advantage may make it preferable for real-time applications. | Up to 2,048 tokens | n/a |

For more, visit our guide to working with Codex.

The Codex models are free to use during the limited beta, and are subject to reduced rate limits. As we learn about use, we'll look to offer pricing to enable a broad set of applications.

During this period, you're welcome to go live with your application as long as it follows our usage policies. We welcome any feedback on these models while in early use and look forward to engaging with the community.

### Feature-specific models
The main Codex models are meant to be used with the text completion endpoint. We also offer models that are specifically meant to be used with our endpoints for creating embeddings and editing code.

## Moderation

The Moderation models are designed to check whether content complies with OpenAI's usage policies. The models provide classification capabilities that look for content in the following categories: hate, hate/threatening, self-harm, sexual, sexual/minors, violence, and violence/graphic. You can find out more in our moderation guide.

| MODEL | DESCRIPTION |
| text-moderation-latest | Most capable moderation model. Accuracy will be slighlty higher than the stable model |
| text-moderation-stable | Almost as capable as the latest model, but slightly older. |

## GPT-3

GPT-3 models can understand and generate natural language. These models were superceded by the more powerful GPT-3.5 generation models. However, the original GPT-3 base models (`davinci`, `curie`, `ada`, and `babbage`) are current the only models that are available to fine-tune.

| LATEST MODEL | DESCRIPTION | MAX REQUEST | TRAINING DATA |
| --- | --- | --- | --- |
| text-curie-001 | Very capable, faster and lower cost than Davinci. | 2,048 tokens | Up to Oct 2019 |
| text-babbage-001 | Capable of straightforward tasks, very fast, and lower cost. | 2,048 tokens | Up to Oct 2019 |
| text-ada-001 | Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost. | 2,048 tokens | Up to Oct 2019 |
| davinci | Most capable GPT-3 model. Can do any task the other models can do, often with higher quality. | 2,048 tokens | Up to Oct 2019 |
| curie | Very capable, but faster and lower cost than Davinci. | 2,048 tokens | Up to Oct 2019 |
| babbage | Capable of straightforward tasks, very fast, and lower cost. | 2,048 tokens	| Up to Oct 2019 |
| ada | Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost. | 2,048 tokens | Up to Oct 2019 |