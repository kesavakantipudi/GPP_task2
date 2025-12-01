import json
import requests

def request_seed(student_id: str, github_repo_url: str, api_url: str):
    # Step 1: Read public key from PEM file
    with open("student_public.pem", "r") as f:
        public_key = f.read()

    # Replace real line breaks with \n for JSON
    public_key_one_line = public_key

    # Step 2: Prepare JSON payload
    payload = {
        "student_id": student_id,
        "github_repo_url": github_repo_url,
        "public_key": public_key_one_line
    }

    headers = {"Content-Type": "application/json"}

    # Step 3: Send POST request
    response = requests.post(api_url, headers=headers, json=payload, timeout=10)

    # If error
    if response.status_code != 200:
        print("❌ API Error:", response.text)
        return

    # Step 4: Parse JSON
    data = response.json()
    encrypted_seed = data.get("encrypted_seed")

    if not encrypted_seed:
        print("❌ No encrypted seed returned")
        return

    # Step 5: Save encrypted seed to file
    with open("encrypted_seed.txt", "w") as f:
        f.write(encrypted_seed)

    print("✅ Encrypted seed saved to encrypted_seed.txt")


# Example usage:
if __name__ == "__main__":
    request_seed(
        student_id="23MH1A4224",
        github_repo_url="https://github.com/kesavakantipudi/GPP_task2.git",
        api_url="https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"
    )
