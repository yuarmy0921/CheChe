import BT
import maze
import score_new

# hint: You may design additional functions to execute the input command, which will be helpful when debugging :)
#幾個基本的function：讀取RFID、傳送指令、結束
class interface:
    def __init__(self):
        print("")
        print("Arduino Bluetooth Connect Program.")
        print("")
        port = input("PC bluetooth port name: ")
        self.ser = BT.bluetooth(port)      #創建出的bluetooth  #只是先有一個Serial
        while(not self.ser.do_connect(port)):
            if(port == "quit"):
                self.ser.disconnect()
                quit()
            port = input("PC bluetooth port name: ")
        input("Press enter to start.")
        
    def tell_you(self, string):
        print(string)

    def get_UID(self):
        return self.ser.SerialReadByte()

    def get_status(self):
        return self.ser.SerialReadString()

    def send_action(self,dirc):
        # TODO : send the action to car
        print("start send action.")
        self.ser.SerialWrite(dirc)
        print("action sent.\n")
<<<<<<< HEAD

=======
>>>>>>> 6a88a4b7f5079e58aede62d5cd502295f011db22
        #return self.ser.SerialReadString()   #確認有接收到指令

    def arrival(self):
        return self.ser.SerialReadString() == "k"

    def end_process(self):
        self.ser.SerialWrite('end')
        self.ser.disconnect()

if __name__ == "__main__":
    interface()