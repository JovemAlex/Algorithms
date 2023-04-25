from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    NO_INDEX = 'ebyrt'
    ODD_KEY = 'yrt_eb'
    EVEN_KEY = 'eby_rt'

    # Invalid message
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(333, 666)

    # Invalid key
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", "ebytr")

    # NoIndex
    no_index_call = encrypt_message('trybe', 10)
    assert no_index_call == NO_INDEX

    # OddKey
    odd_key_call = encrypt_message('trybe', 3)
    assert odd_key_call == ODD_KEY

    # EvenKey
    even_key_call = encrypt_message('trybe', 2)
    assert even_key_call == EVEN_KEY
