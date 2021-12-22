# thanks for the website https://www.tellert.de/files/media/temes/help/position-of-can-signals-(start.html
# it help me a lot!
import click
class signal():
    def __init__(self,name,represent,start, _len, frame_len,type="I"):
        self.name = name
        self.represent = represent
        self.start = start
        self._len =_len
        self.signal_bitmap = self.calc_bitmap(start,_len,frame_len,type)

    # I as intel format, M  as motorala format 
    def calc_bitmap(self, start, _len, frame_len, type="I"):
        _,bitpos= signal.gen_bit_maps(frame_len,type)
        signal_pos_map = {}
        for pos in range(start,start+_len):
            signal_pos_map[pos]=bitpos[pos]
        return signal_pos_map
            
            
    def gen_bit_maps(length, type = "I"):
        bitmaps = []
        bitpos = {}
        if type == "I": # intel format
            for idx in range(length):
                idx*=8
                bitmaps.append([idx,idx+1,idx+2,idx+3,idx+4,idx+5,idx+6,idx+7])
                for count, value in enumerate(bitmaps[-1]):
                    bitpos[value]=[len(bitmaps)-1,count]
                
        elif type == "M": # motorolar format
            for idx in range(length):
                idx=(7-idx)*8
                bitmaps.append([idx,idx+1,idx+2,idx+3,idx+4,idx+5,idx+6,idx+7])
                for count, value in enumerate(bitmaps[-1]):
                    bitpos[value]=[len(bitmaps)-1,count]
        else:
            raise Exception("the format were not supported")
        return bitmaps, bitpos

class frame():
    def __init__(self,frame_len=8,frame_type="I"):
        self.frame_reserves = [['.']*8 for i in range(frame_len)]
        self.frame_len = frame_len
        self.signal_maps = {}
        self.frame_type = frame_type

    def add_signal(self, name,represent,start,_len):
        self.signal_maps[name]=signal(name,represent,start,_len,self.frame_len,self.frame_type)
        pass
        
    def showit(self):
        for k in self.signal_maps:
            sig = self.signal_maps[k]
            for pos in sig.signal_bitmap.values():
                # here to debug all the print
                _byte = pos[0]
                _bit = pos[1]
                self.frame_reserves[_byte][_bit] = sig.represent
        print("| {} {} {} {} {} {} {} {} |".format(7,6,5,4,3,2,1,0))
        for line in self.frame_reserves:
            # line[::-1] make sure we can format as a embbeded view
            print("| {} {} {} {} {} {} {} {} |".format(*line[::-1]))
        print("")
        for k in self.signal_maps:
            sig = self.signal_maps[k]
            print("{} : {}".format(sig.name,sig.represent))
    # def dbg(self):
    #     for sig in self.signal_maps:
    #         print(self.signal_maps[sig].represent)
@click.command()
@click.option('--flen',default=8,help="This field help you set the CAN frame length")
@click.option('--name',default="signal",help="This field help you set the signal name")
@click.option('--repr',default="A",help="This field help you set the signal represent character for you view")
@click.option('--start',default=0,help="This field help you set the signal start bit position")
@click.option('--len',default=8,help="This field help you set the signal length ")
@click.option('--format',default="I",help="This field help you set the frame format were intel or mortorola ")
def cli(flen,name,repr,start,len,format):
    new_frame = frame(flen,format)
    new_frame.add_signal(name,repr,start,len)
    new_frame.showit()

if __name__ == '__main__':
    cli()
    # smap,spos = signal.gen_bit_maps(8,"M")
    # print(smap)

    # new_frame = frame(8,"M")
    # new_frame.add_signal("baby","A",7,9)
    # new_frame.showit()

    

