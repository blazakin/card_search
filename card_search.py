import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5553")


while True:
    message = socket.recv().decode()

    print(f"Received: {message}")
    if message == 'Exit':
        break

    search_term = message.split(';')[0]
    card_list = message.split(';')[1:-1]
    found = False
    for card in card_list:
        if search_term in card:
            socket.send_string(card)
            print(f"Sent: {card}")
            found = True
            break
    if not found:
        socket.send_string("Card not found.")
        print(f"Sent: Card not found.")
