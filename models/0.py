from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Observaciones'
settings.subtitle = 'Astronomia'
settings.author = 'Lucho'
settings.author_email = 'luedugonzalez@gmail.com'
settings.keywords = None
settings.description = None
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'c29f4ff2-3008-469c-b7de-896bbfd6fe09'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
