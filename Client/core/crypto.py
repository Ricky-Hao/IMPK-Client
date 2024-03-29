import os
import datetime
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography import x509, exceptions
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from Client.util import KEY_ROOT


def getUserPath(username):
    path = os.path.join(KEY_ROOT, username)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def getUserFilePath(username, file_type):
    return os.path.join(getUserPath(username), '{0}.{1}'.format(username, file_type))

def checkUserPrivateKey(username):
    key_path = getUserFilePath(username, 'key')
    if os.path.exists(key_path):
        return True
    return False

def checkUserCertKey(username):
    cert_path = getUserFilePath(username, 'crt')
    if os.path.exists(cert_path):
        return True
    return False

def generatePrivate(username, password):
    key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 2048,
        backend = default_backend()
    )

    key_path = getUserFilePath(username, 'key')

    with open(key_path, 'wb') as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode()),
        ))

    return key

def generateCSR(username, key, country_name, state_name, locality_name, organization_name, unit_name, common_name):
    csr = x509.CertificateSigningRequestBuilder()
    csr = csr.subject_name(
        x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_name),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, unit_name),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            ])
    )
    csr = csr.sign(key, hashes.SHA256(), default_backend())

    path = getUserFilePath(username, 'csr')

    with open(path, 'wb') as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

    return csr.public_bytes(serialization.Encoding.PEM).decode()

def signCSR(ca, ca_key, csr, timedelta, path):
    cert = x509.CertificateBuilder()
    cert = cert.subject_name(csr.subject)
    cert = cert.issuer_name(ca.issuer)
    cert = cert.public_key(csr.public_key())
    cert = cert.serial_number(x509.random_serial_number())
    cert = cert.not_valid_before(datetime.datetime.utcnow())
    cert = cert.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=timedelta))
    cert = cert.sign(ca_key, hashes.SHA256(), default_backend())

    return cert.public_bytes(serialization.Encoding.PEM)

def loadPrivate(key_data, password):
    if not isinstance(key_data, bytes):
        key_data = key_data.encode()

    if password is not None:
        password = password.encode()

    return serialization.load_pem_private_key(key_data, password, default_backend())

def loadPrivateFromFile(key_path, password):
    with open(key_path, 'rb') as f:
        key_data = f.read()

    return loadPrivate(key_data, password)

def loadPrivateFromUser(username, password):
    key_path = os.path.join(getUserPath(username), '{0}.key'.format(username))
    with open(key_path, 'rb') as f:
        key_data = f.read()

    return loadPrivate(key_data, password)

def loadCert(cert_data):
    if not isinstance(cert_data, bytes):
        cert_data = cert_data.encode()

    return x509.load_pem_x509_certificate(cert_data, default_backend())

def loadCertFromFile(cert_path):
    with open(cert_path, 'rb') as f:
        cert_data = f.read()

    return loadCert(cert_data)

def loadCertFromUser(username):
    cert_path = os.path.join(getUserPath(username), '{0}.crt'.format(username))
    with open(cert_path, 'rb') as f:
        cert_data = f.read()

    return loadCert(cert_data)

def installCertForUser(username, cert_data):
    if not isinstance(cert_data, bytes):
        cert_data = cert_data.encode()

    cert_path = os.path.join(getUserPath(username), '{0}.crt'.format(username))

    with open(cert_path, 'wb') as f:
        f.write(cert_data)

    return loadCert(cert_data)

def signWithPrivate(message, private_key):
    if not isinstance(message, bytes):
        message = message.encode()

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature

def verifyWithPublic(message, signature, public_key):
    if not isinstance(message, bytes):
        message = message.encode()

    if not isinstance(signature, bytes):
        signature = signature.encode()

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return True
    except exceptions.InvalidSignature:
        return False

def encryptWithPublic(message, public_key):
    if not isinstance(message, bytes):
        message = message.encode()

    cipertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return cipertext

def decryptWithPrivate(ciphertext, private_key):
    if not isinstance(ciphertext, bytes):
        ciphertext = ciphertext.encode()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext

def encryptAndSign(plaintext, public_key, private_key):
    ciphertext = encryptWithPublic(plaintext, public_key)
    signature = signWithPrivate(ciphertext, private_key)

    ciphertext = base64.b64encode(ciphertext).decode()
    signature = base64.b64encode(signature).decode()

    return ciphertext, signature

def decryptAndVerify(ciphertext, signature, public_key, private_key):
    ciphertext = base64.b64decode(ciphertext)
    signature = base64.b64decode(signature)
    if verifyWithPublic(ciphertext, signature, public_key):
        plaintext = decryptWithPrivate(ciphertext, private_key).decode()
        return plaintext
    else:
        return ''

