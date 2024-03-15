# Evaluation Pricing
Variabili:
- Modello / API
- Dataset
- Request Settings

## Modello / API
Anthropic:
- modello `claude-3-opus`   -   closed source
- modello `claude-3-sonnet`
- modello `claude-3-haiku`

OpenAI:
- modello `gpt-4-1106-vision-preview`   -   closed source

LLaVA-1.6 on Hugging Face
- modello `liuhaotian/llava-v1.6-34b`
- modello `liuhaotian/llava-v1.6-vicuna-13b`
- modello `liuhaotian/llava-v1.6-mistral-7b`

KOSMOS-2 on Hugging Face
- modello `microsoft/kosmos-2-patch14-224` - 1.66B parameters

## Request Settings
### Request Settings OpenAI: modello `claude-3-haiku`
Input: $`0.25` per million tokens
Output: $`1.25` per million tokens

Image pricing:
> tokens = (width px * height px)/750

words: 1 token ~= 3.5 english characters


### Request Settings OpenAI: modello `gpt-4-1106-vision-preview`
Funzionamento $ / tokens, in input e in output.
- Input: $0.01 / 1K tokens
- Output: $0.03 / 1K tokens

Image options:
- low_resolution: 85 tokens
- high_resolution: up to 512px x 512px => 255 tokens

### Request Settings HF: LLaVA `liuhaotian/llava-v1.6-mistral-7b`
Funzionamento: dedicated Inference Endpoint
- need 24GB of GPU: `1.3 $/h`


### Request Settings HF: LLaVA `liuhaotian/llava-v1.6-vicuna-13b`
Funzionamento: dedicated Inference Endpoint
- need 24GB of GPU: `4.5 $/h`


### Request Settings HF: LLaVA `liuhaotian/llava-v1.6-34b`
Funzionamento: dedicated Inference Endpoint
- need 64GB of GPU: renting: `4.5 $/h`


## Dataset
- MiniImageNet:
    10k images in 100 labels

- Caltech 101
    9k images in  102 labels



# Pricing options

## Kosmos-2: option 0
Price / request: 0

=> Dataset: _Caltech 101_ => [done]
=> Dataset: _Mini Image Net - 10k validation set_ => [work_in_progress]


## GPT4-V: option1
Dataset: _Mini Image Net - 10k validation set_

Tokens per request:
- 85 tokens: input image on low resolution
- 20 tokens: input text
- 20 tokens: output text

= 125 token / entry

10000 (entries) * 125 (tokens) / 1 (entry) * 0.01$ / 1000 (tokens)
    = $12.5
+ some margin for testing. => $`15`                 =>      [work_in_progress]


## LLaVA 7B: option2
Difficult to evaluate "a priori" the time needed for the model to compute. Considering the work done with kosmos2 on caltech_101:

Around 48 computing hours to complete 9000 images.

48 h * 1.3 $/h = $`62.4`


## Claude Api
Tokens per request:
- Input: 560 tokens
- Ouput: 40 tokens

(560 * 0.25 / 1'000'000 + 40 * 1.25 / 1'000'000) * 10000 = $`1.9`

=> Dataset: _Mini Image Net - 10k validation set_ => [work_in_progress]