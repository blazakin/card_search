import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5553")


while True:
    message = socket.recv().decode()

    if message == 'Exit':
        break

    search_term = message.split(';')[0]
    card_list = message.split(';')[1:-1]
    found = False
    for card in card_list:
        if search_term in card:
            socket.send_string(card)
            found = True
            break
    if not found:
        socket.send_string("Card not found.")
