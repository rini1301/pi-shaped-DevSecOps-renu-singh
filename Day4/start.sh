#!/usr/bin/env bash
# Simple launcher used by CI when starting the app for dynamic scanning
set -e
python app.py &
# give some time to start
sleep 8
# keep script alive for workflow (nohup alternative is used in workflow too)
wait