import re
from scapy.all import *
from datetime import datetime

def process_packet(packet, output_file):
    if packet.haslayer(Raw):
        try:
            raw_data = packet[Raw].load.decode('utf-8', errors='ignore')
           
            pattern = re.compile(r'<([^<>]+)>([^<>]*)</?>')
            matches = pattern.findall(raw_data)
            if matches:
                with open(output_file, 'a', encoding='utf-8') as f:
                    for tag, content in matches:
                        final_data = f'<{tag}>{content}</>'
                        letter_count = len(final_data)
                        possible_name_segment = re.split(r'[,\n]', raw_data)[-1].strip()
                        name_match = re.search(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', possible_name_segment)
                        if name_match:
                            potential_name = name_match.group(0)
                        else:
                            single_word_match = re.search(r'\b[A-Z][a-z]+\b', possible_name_segment)
                            potential_name = single_word_match.group(0) if single_word_match else "Unknown (Non-Latin letter)"
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        
                        # Write in Markdown format
                        f.write(f"## Packet Capture: {timestamp}\n\n")
                        f.write(f"- **Data**: `{final_data}`\n")
                        f.write(f"- **Letter Count**: {letter_count}\n")
                        f.write(f"- **Potential Name**: {potential_name}\n")
                        # f.write(f"- **Raw Data**: ```{raw_data}```\n\n")
                        f.write("\n")
        except UnicodeDecodeError:
            print("UnicodeDecodeError: Cannot decode packet data.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    output_file = "extracted_data.md"
    
    # Write the Markdown header
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Network Packet Capture Log\n\n")
   
    def packet_callback(packet):
        process_packet(packet, output_file)

    sniff(filter="host 43.159.31.173 and port 30031", prn=packet_callback)

if __name__ == "__main__":
    main()