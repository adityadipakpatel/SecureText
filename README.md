# SecureText

SecureText is a simple tool that allows users to encrypt and decrypt text using a two-step process. The encryption script generates two passcodes, which are required to retrieve the original text using the decryption script.

## Features

- **Encryption**: Converts a piece of text into two long numeric strings.
- **Decryption**: Restores the original text using the two numeric strings in the correct order.

## Use Cases

- **Security**: Use SecureText to safely encrypt sensitive information before sharing it over insecure channels.
- **Data Integrity**: Ensure that your text data is not tampered with during transmission by decrypting with the original passcodes.
- **Privacy**: Protect personal messages or confidential information by encrypting text before storing or sending.


## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. This project uses Python 3.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/adityadipakpatel/SecureText.git
    ```
    ```bash
    cd SecureText
    ```

2. (Optional) Create a virtual environment and activate it:

    ```bash
    python -m venv env
    ```
    ```bash
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Encrypting Text

To encrypt a piece of text, run the `encrypt.py` script:

```bash
python encrypt.py
```

You will be prompted to enter the text you wish to encrypt. The script will output two long strings of numbers, referred to as `Pass1` and `Pass2`.

### Decrypting Text

To decrypt the text, run the `decrypt.py` script:

```bash
python decrypt.py
```

You will be prompted to enter `Pass1` and `Pass2`. If entered correctly, the script will return the original text.

## Example

```bash
$ python encrypt.py
Enter the text to encrypt: HelloWorld
Pass1: 355863463932494276804378914434
Pass2: 639625819756877466497643720768

$ python decrypt.py
Enter Pass1: 355863463932494276804378914434
Enter Pass2: 639625819756877466497643720768
Original text: HelloWorld
```

## Contributing

Feel free to fork this project, submit issues, and make pull requests. Contributions are always welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions, please contact [Aditya Patel](mailto:adityapatel09112004@gamil.com).
