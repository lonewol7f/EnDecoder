import base64

def b64enc(st):
    b = st.encode("UTF-8")
    eb = base64.b64encode(b)
    es = eb.decode("UTF-8")

    print('Encoded :',es)

def b64dec(st):
    b = st.encode("UTF-8")
    eb = base64.b64decode(b)
    es = eb.decode("UTF-8")

    print('Decoded :',es)

def b32enc(st):
    b = st.encode("UTF-8")
    eb = base64.b32encode(b)
    es = eb.decode("UTF-8")

    print('Encoded :',es)

def b32dec(st):
    b = st.encode("UTF-8")
    eb = base64.b32decode(b)
    es = eb.decode("UTF-8")

    print('Decoded :',es)

def b16enc(st):
    b = st.encode("UTF-8")
    eb = base64.b16encode(b)
    es = eb.decode("UTF-8")

    print('Encoded :',es)

def b16dec(st):
    b = st.encode("UTF-8")
    eb = base64.b16decode(b)
    es = eb.decode("UTF-8")

    print('Decoded :',es)

def b85enc(st):
    b = st.encode("UTF-8")
    eb = base64.b85encode(b)
    es = eb.decode("UTF-8")

    print('Encoded :',es)

def b85dec(st):
    b = st.encode("UTF-8")
    eb = base64.b85decode(b)
    es = eb.decode("UTF-8")

    print('Decoded :',es)
