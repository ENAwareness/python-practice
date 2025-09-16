#!/usr/bin/env python3
"""
Load environment variables from .env file
"""
import os
from pathlib import Path

def load_env():
    """Load environment variables from .env file"""
    env_file = Path(__file__).parent / '.env'

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value
        print(f"Loaded environment variables from {env_file}")
    else:
        print(f".env file not found at {env_file}")

if __name__ == "__main__":
    load_env()
    print(f"GOOGLE_CLOUD_PROJECT: {os.getenv('GOOGLE_CLOUD_PROJECT')}")