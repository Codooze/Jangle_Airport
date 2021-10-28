from app import app
import os
from socket import gethostname

# - podemos crear más files "view" por ejemplo "adm_views", "usuario_views" "userAutorización_view"etc
secret = os.urandom(16)
app.secret_key = secret
app.config['SESSION_TYPE'] = 'filesystem'
if __name__ == "__main__":
    if 'liveconsole' not in gethostname():
        app.run()
    else: app.run(debug=True)
