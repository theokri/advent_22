def io_to_string(filename: str) -> str:
    with open('packets.txt') as text_io:
        data_parsed = text_io.read()
        return data_parsed

def determine_start_of_packet_markers(message: str, marker_length: int) -> list[int]:
    buffer = []
    start_of_packet_markers = []
    for i in range (len(message)):
        char = message[i]
        if len(set(buffer)) == len(buffer) and len(buffer) == marker_length:
            start_of_packet_markers.append(i+1)
        if len(buffer) < marker_length:
            buffer.append(char)
        else:
            buffer.pop(0)
            buffer.append(char)
    return start_of_packet_markers
        

def main() -> None:
    message = io_to_string('packets.txt')
    # print(determine_start_of_packet_markers(message, marker_length = 4)) # for first challenge
    # print(determine_start_of_packet_markers(message, marker_length = 14)) # for second challenge
        
if __name__ == '__main__':
    main()
