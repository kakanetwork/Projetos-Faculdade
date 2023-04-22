from tkinter import *
import scapy.all as scapy

def capture_packet():
    packet = scapy.sniff(filter='icmp', count=1)[0]
    ip_header = packet[scapy.IP]
    src_ip = ip_header.src
    dst_ip = ip_header.dst
    protocol = ip_header.proto
    ttl = ip_header.ttl
    
    src_label.config(text="Endereço de origem: " + src_ip)
    dst_label.config(text="Endereço de destino: " + dst_ip)
    protocol_label.config(text="Protocolo: " + str(protocol))
    ttl_label.config(text="TTL: " + str(ttl))

# cria a janela principal
root = Tk()

# cria widgets de rótulo para exibir informações do cabeçalho IP
src_label = Label(root, text="Endereço de origem: ")
src_label.pack()

dst_label = Label(root, text="Endereço de destino: ")
dst_label.pack()

protocol_label = Label(root, text="Protocolo: ")
protocol_label.pack()

ttl_label = Label(root, text="TTL: ")
ttl_label.pack()

# cria botão para capturar um pacote ICMP
button = Button(root, text="Capturar pacote ICMP", command=capture_packet)
button.pack()

# inicia o loop principal da interface gráfica
root.mainloop()
