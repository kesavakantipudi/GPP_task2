from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_keypair(key_size: int = 4096):
    """
    Generate RSA key pair.

    Returns:
        (private_key, public_key)
    """

    # Generate RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )

    # Get public key from private key
    public_key = private_key.public_key()

    # Serialize private key to PEM (no password)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    # Serialize public key to PEM
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # Save to files required by assignment
    with open("student_private.pem", "wb") as f:
        f.write(private_pem)

    with open("student_public.pem", "wb") as f:
        f.write(public_pem)

    return private_key, public_key


if __name__ == "__main__":
    generate_rsa_keypair()
    print("✅ Generated student_private.pem and student_public.pem")
