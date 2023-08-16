# Speech-to-text AI Examples

Generative AI models offer capabilities for transcribing audio to text at an incredibly great accuracy, stepping in to field where traditionally niche players offered pricey services. Medical and legal fields are in a good position to leverage these new capabilities.

This example shows two simple ways of transcribing an audio file to text:

- Using Whisper model from [Huggingface Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index), allowing the AWS PrivateLink deployments
- Using public API from [OpenAI](https://platform.openai.com/docs/guides/speech-to-text)

## Setup

The example provides a small `flac` and `m4a` source file, and uses Robocorp Control Room's Vault for storing the access credentials. These are the names of required Vaults and keys for each use case:

- Huggingface Inference Endpoints
  - Vault named `Huggingface`
  - Key named `whisper-url` that has the URL of a deployed inference endpoint (which you need to create)
  - Key named `api-token` has the API token from your HF account
- OpenAI
  - Vault named `OpenAI`
  - Key named `key` that has the API key
 
## Ideas for further development

Both of the examples are covering only a basic use case, and can be expanded. Feel free to leave a PR! Here are some ideas:

- [Handle inputs over 25 MB](https://platform.openai.com/docs/guides/speech-to-text/longer-inputs)
- [Improve reliability by introducing correct spelling in prompt](https://platform.openai.com/docs/guides/speech-to-text/improving-reliability)
- Expand file format support
- Add exception handling
