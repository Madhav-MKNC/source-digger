# GitHub Analyzer

Welcome to GitHub Analyzer, a program that scans GitHub repositories to offer insights and answer questions about the source code. This tool leverages the power of Langchain and OpenAI's GPT models to understand, interpret, and provide rich analysis of source code.

## Overview

GitHub Analyzer scans the source code of a specified GitHub repository. It processes the code using Langchain frameworks, interpreting the syntax and structures within. Following this, it leverages OpenAI's GPT models to understand and encode the code semantics. The interpreted data is then stored in a vector database, enabling easy retrieval for later question-answering.

## Features

- **Code Analysis:** GitHub Analyzer scans and understands the syntax and semantics of the source code in a GitHub repository.
- **QnA Mechanism:** The tool offers a question-answering system for you to query specifics about the scanned source code.

## Setup & Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/Madhav-MKNC/source-digger.git
   cd source-digger
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI GPT key and GitHub Personal Access Token to a `.env` file in the root of your project.
   ```
   GPT_KEY=your-gpt-key
   GH_TOKEN=your-personal-access-token
   ```

## Usage

Provide the necessary details in the command line arguments. For example:

```bash
python main.py "<owner>/<repo>"
```

Replace `<owner>/<repo>` with the username and repository name.

## License

This project is licensed under the terms of the MIT license.
