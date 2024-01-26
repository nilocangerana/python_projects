## Leitor de chat na Twitch
import socket
import argparse
from emoji import demojize #pip install emoji

#Variáveis
@dataclass
class Config:
    def __init__(self, nickname, token, channel_name):
        self.server='irc.chat.twitch.tv'
        self.port = 6667
        self.nickname=nickname #'<your_twitch_nickname>' #o nome da conta na Twitch
        self.token=token #'<twitch_token>' #gerar no link: https://twitchapps.com/tmi/
        self.channel="#"+channel_name  #'#<channel_name>' #Nome do canal da twitch
       
       
def enable_connection(config):
    sock = socket.socket()
    sock.connect((config.server, config.port))
    sock.send(f"PASS {config.token}\n".encode('utf-8'))
    sock.send(f"NICK {config.nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {config.channel}\n".encode('utf-8'))
    
    resp = sock.recv(2048).decode('utf-8')
    print(resp)
    return sock
    
def parse_args(input_args=None):
    parser = argparse.ArgumentParser(description="Argumentos para conexão com a Twitch.")
    parser.add_argument(
        "--twitch_nickname",
        type=str,
        default=None,
        required=True,
        help="Nome de usuário da sua conta na Twitch.",
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        required=True,
        help="Token de autorização. Obtido em https://twitchapps.com/tmi/",
    )
    parser.add_argument(
        "--channel_name",
        type=str,
        default=None,
        required=True,
        help="Nome do canal para ler o chat.",
    )
    
    if input_args is not None:
        args = parser.parse_args(input_args)
    else:
        args = parser.parse_args()
        
    if args.twitch_nickname is None or args.token is None or args.channel_name is None:
        raise ValueError("Nenhum argumento pode ser nulo.")
    
    return args
    
def main(args):
    config = Config(args.twitch_nickname, args.token, args.channel_name)
    sock = enable_connection(config)
    try:
      while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
          sock.send("PONG\n".encode('utf-8'))
        elif len(resp) > 0:
          demote_resp = demojize(resp)
          raw_text = demote_resp.split(f"#{args.channel_name} :")
          print("Chat: ",raw_text[1])
    
    except KeyboardInterrupt:
        sock.close()
        exit()
    
if __name__ == "__main__":
    args = parse_args()
    main(args)
