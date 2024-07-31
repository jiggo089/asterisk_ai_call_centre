# Asterisk AI Call Centre

This repository provides an AI-powered call center solution for a clinic, built using **Asterisk** and **OpenAI's GPT**. The system is capable of handling incoming calls, transcribing audio, generating responses using GPT models, and converting text to speech, all integrated within the Asterisk telephony system.

## Features

- **Incoming Call Handling**: Automatically answers incoming calls and plays a greeting message.
- **Interactive Voice Response (IVR)**: Provides menu options for users to interact with, allowing them to choose different actions.
- **Transcription**: Uses OpenAI's Whisper model to transcribe incoming audio messages.
- **AI-Driven Responses**: Integrates with OpenAI's GPT models to generate intelligent responses based on the transcription.
- **Text-to-Speech**: Converts AI-generated text responses to speech and plays them back to the caller.
- **Call Flow Management**: Fully customizable call flow with options for handling invalid inputs and timeouts.

## Prerequisites

- **Asterisk**: A software implementation of a telephone private branch exchange (PBX).
- **Python 3.6+**
- **OpenAI API Key**: For integrating with OpenAI's Whisper, GPT, and TTS models.
- **SoX**: A command-line utility that can convert audio files to different formats.
- **Ubuntu Server**: The server environment to host Asterisk and run Python scripts.
- **SIP Telephone**: Required for interacting with the Asterisk system.

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/asterisk_ai_call_centre.git
cd asterisk_ai_call_centre
```
### 2. Install Dependencies

Install the necessary packages for Asterisk and Python:

```sh
Copy code
sudo apt-get update
sudo apt-get install asterisk python3-pip sox
pip3 install openai
```
### 3. Configure Asterisk
Update your Asterisk dial plan 

### 4. Configure OpenAI API
Create a .env file in the root directory with the following content:
```env
OPENAI_API_KEY=your_openai_api_key_here
```
### 5. Set Up Python Scripts
Place your Python scripts (e.g., record_and_hangup.py, gpt1_doc.py, gpt2_record.py) in the /var/lib/asterisk/agi-bin/ directory. Ensure they have execute permissions:

```sh
sudo chmod +x /var/lib/asterisk/agi-bin/*.py
```
### 6. Test the Setup
Start Asterisk:
```sh
sudo asterisk -rvvv
```
Make a call to the configured extension and interact with the IVR.
### Usage
- Incoming Call Handling: When a call comes in, the system plays a welcome message and prompts the user for input.
- Transcription: The system records audio and uses Whisper for transcription.
- AI Response: GPT generates a response based on the transcription.
- Text-to-Speech: The response is converted to speech using the OpenAI TTS model and played back to the caller.
