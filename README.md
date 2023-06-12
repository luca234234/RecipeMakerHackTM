# Project RecipeMakerHackTM README.md

## Overview

Project RecipeMakerHackTM is a powerful tool leveraging OpenAI's latest language model technology. This document provides a detailed step-by-step guide on how to set up Project RecipeMakerHackTM for use.

## Requirements

To run Project RecipeMakerHackTM, you will need:

- An OpenAI API token. You can obtain this from your [OpenAI account](https://beta.openai.com/signup/).
- The Project yolov5_food.pt model, which you can download from the specified Google Drive link.

## Installation

Follow these steps to install and configure Project RecipeMakerHackTM.

### Step 1: Download the Model

1. Go to this Google Drive [link](https://drive.google.com/file/d/1CG5IqXh-d-RITVYtS9oJMSWnfiM_MLv0/view?usp=sharing).
2. Download the model file `yolov5_food.pt`.
3. Save the model file in your local project directory.

### Step 2: OpenAI API Key Configuration

1. Login into your [OpenAI account](https://beta.openai.com/signup/).
2. Navigate to the API section to get your OpenAI API key.
3. Save your API key in an environment variable named `OPENAI_API_KEY`.

**On Unix/Linux/macOS:**

Open your terminal and enter the following command:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

**On Windows:**

For cmd:

```cmd
setx OPENAI_API_KEY "your-api-key-here"
```

For PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

Remember to replace `your-api-key-here` with your actual OpenAI API key.

## Running Project RecipeMakerHackTM

Once you have followed the above steps, you can now run Project RecipeMakerHackTM as per the instructions.

**Note:** Ensure that you always have the `OPENAI_API_KEY` environment variable set with your OpenAI API key whenever you're running this project.

---

For any further queries or issues, feel free to raise an issue in the project's GitHub repository.

Happy coding!
