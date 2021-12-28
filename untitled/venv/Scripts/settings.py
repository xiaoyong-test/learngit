TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS' : False,
        'OPTIONS' : {
            'environment' : "scripts.scripts.jinja2.environment",
            'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.antu.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'app.wsgi.application'