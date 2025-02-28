import os
import subprocess

# Set the schema path
SCHEMA_PATH = os.getenv("SCHEMA_PATH", "./snowflakescripts")

# Run schemachange
def run_schemachange():
    command = [
        "schemachange",
        "-f", SCHEMA_PATH,
        "-c", "SNOWFLAKE_SAMPLE_DATA.SCHEMACHANGE.CHANGE_HISTORY",
        "--create-change-history-table"
    ]
    
    print("🚀 Running schemachange...")
    try:
        subprocess.run(command, check=True)
        print("✅ schemachange executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ schemachange failed: {e}")
        exit(1)

if __name__ == "__main__":
    run_schemachange()
