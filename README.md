# Sky Brazil Cookie Checker

A Node.js tool to validate Sky Brazil cookies and extract user information from JWT tokens.

## Features

- ✅ Validate Sky Brazil cookies
- 📝 Extract user information from JWT tokens
- 🚀 Fast cookie checking with timeout protection
- 💾 Save valid cookies to file
- 🎨 Colorful console output

## Installation

1. Clone or download this repository
2. Install dependencies:
```bash
npm install
```

## Usage

### Check Cookies
```bash
node index.js
```

The tool will:
- Read cookies from `cookies.txt`
- Test each cookie against `https://www.sky.com.br/minha-sky`
- Extract user information from valid JWT tokens
- Save valid cookies to `valids.txt`

### Extract Tokens Only
```bash
python extrator.py
```
or
```bash
py extrator.py
```

This will:
- Extract `_tEsk_token` from `cookies.txt`
- Save clean tokens to `sky_tokens_extraidos.txt`

## File Structure

```
├── index.js              # Main cookie checker
├── extrator.py           # Token extractor
├── cookies.txt           # Input cookies (one per line)
├── package.json          # Dependencies
└── README.md            # This file
```

## Cookie Format

Cookies should be in standard format:
```
_tEsk_token=eyJhbGciOiJSUzI1NiJ9...;JSESSIONID=...;_tEsk_signature=...
```

## Essential Sky Cookies

For successful login, these cookies are required:
- `_tEsk_token` - Main JWT authentication token
- `P_uTk` - Secondary user token
- `JSESSIONID` - Session ID
- `_tEsk_signature` - Token signature
- `_tEsk_tokenEnv` - Environment (www.sky.com.br)
- `_tEsk_expTime` - Expiration time
- `P_expTime` - Secondary expiration time

## Output

### Successful Check
```
[+] _tEsk_token=eyJhbGciOiJSUzI1NiJ9... | UNICEF PAES (lala.pfeifer@gmail.com)
```

### Failed Check
```
[-] _tEsk_token=eyJhbGciOiJSUzI1NiJ9... (erro: 401)
```

## Dependencies

- `axios` - HTTP requests
- `colors` - Console colors
- `fs` - File system (built-in)

## Error Codes

- `401` - Unauthorized/Invalid cookie
- `403` - Forbidden
- `timeout` - Request timeout
- `token_invalid` - Invalid JWT format
- `no_token` - Missing _tEsk_token
- `error` - General error

## Security Notes

- This tool is for educational purposes only
- Cookies contain sensitive authentication data
- Store cookies securely and delete after use
- Respect privacy and terms of service

## License

MIT License
