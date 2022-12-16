FROM python:3.10-slim-bullseye AS base

HEALTHCHECK NONE
LABEL company="20tab" project="moralemeter" service="backend" stage="base"
ARG DEBIAN_FRONTEND=noninteractive
ARG USER=appuser
ENV APPUSER=$USER LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 WORKDIR=/app
WORKDIR $WORKDIR
RUN useradd --skel /dev/null --create-home $APPUSER
RUN chown $APPUSER:$APPUSER $WORKDIR
ENV PATH="/home/${APPUSER}/.local/bin:${PATH}"
ARG PACKAGES_PATH=/home/${APPUSER}/.local/lib/python3.10/site-packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        mime-support \
    && rm -rf /var/lib/apt/lists/*
COPY --chown=$APPUSER ./requirements/base.txt requirements/base.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
    && su $APPUSER -c "python3 -m pip install --user --no-cache-dir -r requirements/base.txt" \
    && rm -rf /var/lib/apt/lists/*
COPY --chown=$APPUSER ./requirements/common.txt requirements/common.txt
RUN su $APPUSER -c "python3 -m pip install --user --no-cache-dir -r requirements/common.txt"

FROM base AS test

HEALTHCHECK NONE
LABEL company="20tab" project="moralemeter" service="backend" stage="test"
USER $APPUSER
COPY --chown=$APPUSER ./requirements/test.txt requirements/test.txt
RUN python3 -m pip install --user --no-cache-dir -r requirements/test.txt
COPY --chown=$APPUSER . .
CMD ./scripts/test.sh

FROM base AS remote

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
    CMD curl --fail http://localhost:8000/api/ || exit 1
LABEL company="20tab" project="moralemeter" service="backend" stage="remote"
USER $APPUSER
ARG PACKAGES_PATH=/home/${APPUSER}/.local/lib/python3.10/site-packages
COPY --chown=$APPUSER ./requirements/remote.txt requirements/remote.txt
RUN python3 -m pip install --user --no-cache-dir -r requirements/remote.txt
COPY --chown=$APPUSER . .
ENTRYPOINT ["./scripts/entrypoint.sh"]
CMD gunicorn app.main:app

FROM base AS local

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
    CMD curl --fail http://localhost:8000/api/ || exit 0
LABEL company="20tab" project="moralemeter" service="backend" stage="local"
ENV PYTHONDEVMODE=1 PYTHONTRACEMALLOC=1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        make
USER $APPUSER
COPY --chown=$APPUSER ./requirements/local.txt requirements/local.txt
RUN python3 -m pip install --no-cache-dir -r requirements/local.txt
COPY --chown=$APPUSER . .
ENTRYPOINT ["./scripts/entrypoint.sh"]
CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
