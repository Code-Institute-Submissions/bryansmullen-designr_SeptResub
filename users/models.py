from django.db import models

'''    
- User - Individual users
    - Id [INT] (unique, PK)
    - Name [STR]
    - Email [STR] (unique, used for authentication)
    - Password [STR] (hashed)
'''