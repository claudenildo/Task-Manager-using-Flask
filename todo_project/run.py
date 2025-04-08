from todo_project import app
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

# Inicializa o Sentry para monitoramento de erros

sentry_sdk.init(
    dsn="https://<seu_dsn_aqui>@sentry.io/123456",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)

if __name__ == '__main__':
    app.run(debug=True)

