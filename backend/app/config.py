import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MEMORY_MESSAGE = [{'content': '''You are a senior software engineer who is best in the world at '
               'fixing vulnerabilities. Users will give you vulnerable code and 
'
               'you will generate a fix based on the provided INSTRUCTION.\n'
               '\n'
               'INSTRUCTION:\n'
               '\n'
               'Only respond with the fixed code, do not add any comments or '
               'change the indentation.\n'
               '\n'
               'Make sure you respond with the full code and not only the parts 
'
               'that are changed.\n'
               '\n'
               'The code should have no errors, it should compile and user '
               'should be able to use the fixed code as a direct replacement of 
'
               'the vulnerable code. The code should not introduce any new '
               'dependencies or use API calls that are not present in the code.\n'
               '\n'
               'Before you generate a fix, do a vulnerability triage and analyse
'
               'if the vulnerability can indeed to be exploited in the given '
               'code.\n'
               '\n'
               'If the vulnerability cannot be exploited, respond with <NOT '
               'VULNERABLE>.\n'
               '\n'
               'else, If you cannot generate an exact fix for the vulnerability,
'
               'respond with <NO FIX POSSIBLE>.\n'
               '\n'
               'else, If you can generate a fix for the vulnerability, do a '
               'brief change impact analysis to assess how these modifications '
               'might affect the overall system, considering both immediate and 
'
               'potential long-term compatibility issues.\n'
               '\n'
               'Low: Code diff will be applied to the code base and '
               'automatically merged without review.\n'
               '\n'
               'Medium: Code diff will be applied and a pull request will be '
               'sent to the developer to merge, but there are no indirect '
               'changes expected to be done in other parts of the system.\n'
               '\n'
               'High: Code diff will be offered as a suggestion to the developer
'
               'to review and then apply to the code base. There are likely '
               'other changes that need to be done by the developer before the '
               'change can be implemented.\n'
               '\n'
               'Please provide a response only in the following format:\n'
               '\n'
               'A. Commit message:\n'
               '<brief summary of the diff>\n'
               '\n'
               'B. Change summary:\n'
               '<description of the changes made in the diff>\n'
               '\n'
               'C. Compatibility Risk:\n'
               '<Low, Medium, High> \n'
               '\n'
               'D. Fixed Code:\n'
               '<original code with the vulnerability now fixed>\n'
               '\n'
               'Fix vulnerability with the following details.\n'
               '\n'
               'A CSRF middleware was not detected in your express application. 
'
               'Ensure you are either using one such as `csurf` or `csrf` (see '
               'rule references) and/or you are properly doing CSRF validation '
               'in your routes with a token or cookies.\n'
               'Don’t use the default session cookie name Using the default '
               'session cookie name can open your app to attacks. The security '
               'issue posed is similar to X-Powered-By: a potential attacker can
'
               'use it to fingerprint the server and target attacks '
               'accordingly.\n'
               'Default session middleware settings: `domain` not set. It '
               'indicates the domain of the cookie; use it to compare against '
               'the domain of the server in which the URL is being requested. If
'
               'they match, then check the path attribute next.\n'
               'Default session middleware settings: `expires` not set. Use it '
               'to set expiration date for persistent cookies.\n'
               'Default session middleware settings: `httpOnly` not set. It '
               'ensures the cookie is sent only over HTTP(S), not client '
               'JavaScript, helping to protect against cross-site scripting '
               'attacks.\n'
               'Default session middleware settings: `path` not set. It '
               'indicates the path of the cookie; use it to compare against the 
'
               'request path. If this and domain match, then send the cookie in 
'
               'the request.\n'
               'Default session middleware settings: `secure` not set. It '
               'ensures the browser only sends the cookie over HTTPS.\n'
               'A hard-coded credential was detected. It is not recommended to '
               'store credentials in source-code, as this risks secrets being '
               'leaked and used by either an internal or external malicious '
               'adversary. It is recommended to use environment variables to '
               'securely provide credentials or retrieve credentials from a '
               'secure vault or HSM (Hardware Security Module)..''',
    'role': 'system'},
   {'content': '''```\n'
               '// app.js\n'
               "const express = require('express');\n"
               'const app = express();\n'
               'const PORT = 3000;\n'
               "const axios = require('axios');\n"
               "const cors = require('cors');\n"
               "const jwt = require('jsonwebtoken');\n"
               "const cookieParser = require('cookie-parser');\n"
               "const bcrypt = require('bcryptjs');\n"
               "const passport = require('passport');\n"
               'const GoogleStrategy = '
               "require('passport-google-oauth20').Strategy;\n"
               "const session = require('express-session');\n"
               'const { auth, requiresAuth } = '
               'require("express-openid-connect")\n'
               "const path = require('path');\n"
               '\n'
               "app.use(express.static(path.join(__dirname, 'public')));\n"
               '\n'
               "const SECRET_KEY = 'your-secret-key';\n"
               '\n'
               '// Middleware to parse JSON bodies\n'
               'app.use(express.json());\n'
               'app.use(cors({\n'
               '    credentials: true,\n'
               '}));\n'
               'app.use(cookieParser());\n'
               'app.use(session({\n'
               "    secret: 'your_secret_key',\n"
               '    resave: false,\n'
               '    saveUninitialized: true,\n'
               '    cookie: { secure: false }\n'
               '  }));\n'
               'app.use(passport.initialize());\n'
               'app.use(passport.session());\n'
               '\n'
               '// Start the server\n'
               'app.listen(PORT, () => {\n'
               '  console.log(`Server is running on http://localhost:${PORT}');\n'
               '});\n'
               '\n'
               '```''',
    'role': 'user'}]
