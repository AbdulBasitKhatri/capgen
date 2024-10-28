# capgen
	A simple and highly customizable CAPTCHA generator written in Python using Pillow.

## Features
	Generates CAPTCHAs with random text (letters and digits)
	Customizable length of CAPTCHA text
	Random noise and distortion for added security
	Easy to integrate into existing applications
	Fast generation time
	
## Installation
	Python 3.x
	Pillow library (pip install pillow)

## Usage
Generating a CAPTCHA and saving

Python

    import capgen
    image, text = capgen.generate(length=6) # Generate a CAPTCHA with 6 characters
    image.save('captcha.png') # Save the CAPTCHA image
    print(text) # Print the CAPTCHA text
 
## Integration

 1. Call the generate function to generate a CAPTCHA image and text.
 2. Store the CAPTCHA text with hash of the image as unique id in your application's session or database.
 3. Display the CAPTCHA image to the user. 
 4. Verify the user's input against the stored CAPTCHA text identified by the hash.

## Example Use Cases

 1. **Web applications:** Use capgen to prevent automated sign-ups or form submissions.
 2. **Mobile applications:** Integrate capgen to secure user registration or login processes.
 3. **APIs:** Use capgen to protect API endpoints from automated requests.

## Why Choose capgen?

**Easy to integrate:** Simple API and minimal dependencies make integration a breeze.
**High-quality CAPTCHAs:** Random noise and distortion make CAPTCHAs difficult for bots to recognize.
**Customizable:** Adjust the length of the CAPTCHA text to suit your needs.

## Contributing

Pull requests and issues are welcome! If you'd like to contribute to this project or report a bug, please open an issue.

## License

MIT License. See LICENSE for details.
