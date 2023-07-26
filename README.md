# ClassGPT

> ChatGPT for my lecture slides

<img width="1251" alt="SCR-20230307-isgj" src="https://user-images.githubusercontent.com/49143413/223467346-473681e4-6203-4f31-a1f1-253829d4768a.png">

Built with [Streamlit](https://github.com/streamlit/streamlit), powered by [LlamaIndex](https://github.com/jerryjliu/gpt_index) and [LangChain](https://github.com/hwchase17/langchain).

Uses the latest [ChatGPT API](https://platform.openai.com/docs/guides/chat) from [OpenAI](https://openai.com/).

Inspired by [AthensGPT](http://athensgpt.com/)

## App Demo

https://user-images.githubusercontent.com/49143413/222878151-42354446-5234-41fa-ad36-002dd74a5408.mp4

## How this works

1. Parses pdf with [pypdf](https://pypi.org/project/pypdf/)
2. Index Construction with LlamaIndex's `GPTSimpleVectorIndex`
   - the `text-embedding-ada-002` model is used to create embeddings
   - see [vector store index](https://gpt-index.readthedocs.io/en/latest/guides/index_guide.html#vector-store-index) page to learn more
   - here's a [sample index](notebooks/index.json)
3. indexes and files are stored on s3
4. Query the index
   - uses the latest ChatGPT model `gpt-3.5-turbo`

## Usage

### Configuration and secrets

1. configure aws ([quickstart](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html))

```bash
    aws configure
```

2. create an s3 bucket with a unique name

3. Change the bucket name in the codebase (look for `bucket_name = "classgpt"` to whatever you created.

4. rename [.env.local.example] to `.env` and add your openai credentials

### Locally

1. create python env

```bash
    conda create -n classgpt python=3.9
    conda activate classgpt
```

2. install dependencies

```bash
    pip install -r requirements.txt
```

3. run streamlit app

```bash
    cd app/
    streamlit run app/01_❓_Ask.py
```

### Docker

Alternative, you can use Docker

```bash
    docker compose up
```

Then open up a new tab and navigate to <http://localhost:8501/>

## TODO

- [ ] local mode for app (no s3)
  - [ ] global variable use_s3 to toggle between local and s3 mode
- [ ] deploy app to streamlit cloud
  - [ ] have input box for openai key
  - [ ] uses pyarrow local FS to store files
- [ ] update code for new langchain update
- [ ] Custom prompts and tweak settings
  - [ ] create a settings page for tweaking model parameters and provide custom prompts [example](https://github.com/hayabhay/whisper-ui)
- [ ] Add ability to query on multiple files
  - [ ] Compose indices of multiple lectures and query on all of them
  - [ ] loop through all existing index, create the ones that haven't been created, and compose them together
  - references
    - [Composability — LlamaIndex documentation](https://gpt-index.readthedocs.io/en/latest/how_to/composability.html)
    - [gpt_index/ComposableIndices.ipynb](https://github.com/jerryjliu/gpt_index/blob/main/examples/composable_indices/ComposableIndices.ipynb)
    - [Test Complex Queries over Multiple Documents](https://colab.research.google.com/drive/1IJAKd1HIe-LvFRQmd3BCDDIsq6CpOwBj?usp=sharing)

## FAQ

### Tokens

Tokens can be thought of as pieces of words. Before the API processes the prompts, the input is broken down into tokens. These tokens are not cut up exactly where the words start or end - tokens can include trailing spaces and even sub-words. Here are some helpful rules of thumb for understanding tokens in terms of lengths:

- 1 token ~= 4 chars in English
- 1 token ~= ¾ words
- 100 tokens ~= 75 words
- 1-2 sentence ~= 30 tokens
- 1 paragraph ~= 100 tokens
- 1,500 words ~= 2048 tokens

Try the [OpenAI Tokenizer tool](https://platform.openai.com/tokenizer)

[Source](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

### Embeddings

An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

For `text-embedding-ada-002`, cost is $0.0004 / 1k tokens or 3000 pages/dollar

- [Embeddings - OpenAI API](https://platform.openai.com/docs/guides/embeddings/use-cases)
- [What Are Word and Sentence Embeddings?](https://txt.cohere.ai/sentence-word-embeddings/)

### Models

For `gpt-3.5-turbo` model (ChatGPTAPI) cost is `$0.002 / 1K tokens`

For `text-davinci-003` model, cost is `$0.02 / 1K tokens`

- [Chat completion - OpenAI API](https://platform.openai.com/docs/guides/chat)

## References

### Streamlit

- [Increase upload limit of st.file_uploader](https://docs.streamlit.io/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
- [st.cache_resource - Streamlit Docs](https://docs.streamlit.io/library/api-reference/performance/st.cache_resource)
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [hayabhay/whisper-ui: Streamlit UI for OpenAI's Whisper](https://github.com/hayabhay/whisper-ui)

### Deplyoment

- [Streamlit Deployment Guide (wiki) - 🚀 Deployment - Streamlit](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)
- [How to Deploy a streamlit application to AWS? Part-3](https://www.youtube.com/watch?v=Jc5GI3v2jtE)

### LlamaIndex

- [LlamaIndex Usage Pattern](https://gpt-index.readthedocs.io/en/latest/guides/usage_pattern.html#)
- [Saving index](https://gpt-index.readthedocs.io/en/latest/guides/usage_pattern.html#optional-save-the-index-for-future-use)

Loading data

- [PDF Loader](https://llamahub.ai/l/file-pdf)
- [llama-hub github repo](https://github.com/emptycrown/llama-hub/tree/main)
- [document class](https://github.com/jerryjliu/gpt_index/blob/f07050b84309d53842a3552d3546e765012d168c/gpt_index/readers/schema/base.py#L4)
- [PDFReader class](https://github.com/emptycrown/llama-hub/blob/main/loader_hub/file/pdf/base.py)

multimodal

- [llama_index/Multimodal.ipynb at main](https://github.com/jerryjliu/llama_index/blob/main/examples/multimodal/Multimodal.ipynb)

ChatGPT

- [gpt_index/SimpleIndexDemo-ChatGPT.ipynb](https://github.com/jerryjliu/gpt_index/blob/main/examples/vector_indices/SimpleIndexDemo-ChatGPT.ipynb)

### Langchain

- [gpt_index/LangchainDemo.ipynb](https://github.com/jerryjliu/gpt_index/blob/main/examples/langchain_demo/LangchainDemo.ipynb)
- [OpenAIChat](https://langchain.readthedocs.io/en/latest/modules/llms/integrations/openaichat.html)

### Boto3

- [boto3 file_upload does it check if file exists](https://stackoverflow.com/questions/44978426/boto3-file-upload-does-it-check-if-file-exists)
- [Boto 3: Resource vs Client](https://www.learnaws.org/2021/02/24/boto3-resource-client/)
- [Writing json to file in s3 bucket](https://stackoverflow.com/questions/46844263/writing-json-to-file-in-s3-bucket)

### Docker stuff

- [amazon web services - What is the best way to pass AWS credentials to a Docker container?](https://stackoverflow.com/questions/36354423/what-is-the-best-way-to-pass-aws-credentials-to-a-docker-container)
- [docker-compose up failing due to: error: can't find Rust compiler · Issue #572 · acheong08/ChatGPT](https://github.com/acheong08/ChatGPT/issues/572)
- [linux - When installing Rust toolchain in Docker, Bash `source` command doesn't work](https://stackoverflow.com/questions/49676490/when-installing-rust-toolchain-in-docker-bash-source-command-doesnt-work)
- [software installation - How to install a package with apt without the "Do you want to continue [Y/n]?" prompt? - Ask Ubuntu](https://askubuntu.com/questions/523962/how-to-install-a-package-with-apt-without-the-do-you-want-to-continue-y-n-p)
- [How to use sudo inside a docker container?](https://stackoverflow.com/questions/25845538/how-to-use-sudo-inside-a-docker-container)
