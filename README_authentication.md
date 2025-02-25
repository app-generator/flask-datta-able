# Flask-Dance Google OAuth Configuration

This documentation outlines the setup and usage of Google OAuth authentication in a Flask application using Flask-Dance.

## Prerequisites
1. Install necessary dependencies:
   ```sh
   pip install flask-dance flask-login flask-sqlalchemy
   ```
2. Set up Google OAuth credentials:
   - Go to [Google Cloud Console](https://console.developers.google.com/).
   - Create a new project and navigate to **APIs & Services > Credentials**.
   - Create OAuth 2.0 credentials and obtain the `Client ID` and `Client Secret`.
   - Add `http://127.0.0.1:5000/login/google/authorized` as an authorized redirect URI.

## Configuration

### `oauth.py`
This file sets up Google OAuth using Flask-Dance and integrates it with Flask-Login.

```python
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import login_user, current_user
from sqlalchemy.orm.exc import NoResultFound
from apps.config import Config 
from models import db, Users, OAuth

# Google OAuth Blueprint
google_blueprint = make_google_blueprint(
    client_id=Config.GOOGLE_ID,
    client_secret=Config.GOOGLE_SECRET,
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
    storage=SQLAlchemyStorage(
        OAuth, db.session, user=current_user, user_required=False,
    ),
)

# OAuth Authorized Signal Handler
@oauth_authorized.connect_via(google_blueprint)
def google_logged_in(blueprint, token):
    info = google.get("/oauth2/v1/userinfo")
    if info.ok:
        account_info = info.json()
        username = account_info["given_name"]
        email = account_info["email"]

        query = Users.query.filter_by(oauth_google=username)
        try:
            user = query.one()
            login_user(user)
        except NoResultFound:
            user = Users()
            user.username = f"(google){username}"
            user.oauth_google = username
            user.email = email
            db.session.add(user)
            db.session.commit()
            login_user(user)
```

### `routes.py`
Defines the Google login route.

```python
from flask import Blueprint, redirect, url_for
from flask_dance.contrib.google import google
from apps.authentication import blueprint

@blueprint.route("/google")
def login_google():
    """Google login route."""
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for('home_blueprint.index'))
```

### `login.html`
Adds a Google login button to the template.

```html
<div class="text-center mt-4">
    <a href="{{ url_for('google.login') }}" class="d-inline-block p-2 rounded border text-secondary">
        <span class="pc-micon">
            <i class="fab fa-google"></i>
        </span>
    </a>
</div>
```

