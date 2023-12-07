#include <lmic.h>
#include <hal/hal.h>
#include <SPI.h>

static const u1_t PROGMEM APPEUI[8]={ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
void os_getArtEui (u1_t* buf) { memcpy_P(buf, APPEUI, 8);}

//static const u1_t PROGMEM DEVEUI[8]={ 0xc0, 0xb0, 0xe5, 0xe5, 0x14, 0x9d, 0x9b, 0xb6 };
static const u1_t PROGMEM DEVEUI[8]={ 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11 };
void os_getDevEui (u1_t* buf) { memcpy_P(buf, DEVEUI, 8);}

static const u1_t PROGMEM APPKEY[16] = { 0x81, 0xcc, 0xdc, 0xc5, 0xf9, 0x67, 0xe1, 0xc4, 0x91, 0x9d, 0x02, 0xba, 0x61, 0x8a, 0x8b, 0x33 };
void os_getDevKey (u1_t* buf) {  memcpy_P(buf, APPKEY, 16);}


char userMessage[242];
static osjob_t sendjob;
//const unsigned TX_INTERVAL = 60;
bool on = false;
const lmic_pinmap lmic_pins = {
    .nss = 10,
    .rxtx = LMIC_UNUSED_PIN,
    .rst = 5,
    .dio = {2, 3, LMIC_UNUSED_PIN},
};

void waitForSerialStart() {
    while (!Serial.available());
    Serial.read();
}

void readUserInput() {
    int index = 0;
    while (true) {
        if (Serial.available()) {
            char c = Serial.read();
            if (c == '\n' || index >= 241) {
            //if (c == '\n' || index >= 63) {
                break;
            }
            userMessage[index] = c;
            index++;
        }
    }
    userMessage[index] = '\0';
}

void onEvent (ev_t ev) {
    LMIC_setClockError(MAX_CLOCK_ERROR * 10 / 100); //Clock error due to inaccurate clock on the RFM9x
    if (ev >= 17) {
        return;
    }
    switch(ev) {
        case EV_SCAN_TIMEOUT:
            break;
        case EV_BEACON_FOUND:
            break;
        case EV_BEACON_MISSED:
            break;
        case EV_BEACON_TRACKED:
            break;
        case EV_JOINING:
            //LMIC_setClockError(MAX_CLOCK_ERROR * 10 / 100); //This line of code may be needed
            //delay(2000);
            break;
        case EV_JOINED:
            // Disable link check validation (automatically enabled
            // during join, but not supported by TTN at this time).
            //LMIC_setDrTxpow(DR_SF10,14);
            Serial.println(F("#JOINED"));
            LMIC_setAdrMode(1);
            //LMIC_setLinkCheckMode(0);
            //delay(2000);
            break;
        case EV_RFU1:
            break;
        case EV_JOIN_FAILED:
            break;
        case EV_REJOIN_FAILED:
            break;
            break;
        case EV_TXCOMPLETE:
            if (LMIC.txrxFlags & TXRX_ACK)
            if (LMIC.dataLen) {
              // Display the received message
              for (int i = 0; i < LMIC.dataLen; i++) {
              Serial.print((char)LMIC.frame[LMIC.dataBeg + i]);
                }
                Serial.println();
            }
            // Schedule next transmission
            //os_setTimedCallback(&sendjob, os_getTime()+sec2osticks(TX_INTERVAL), do_send);
            break;
        case EV_LOST_TSYNC:
            Serial.println(F("EV_LOST_TSYNC"));
            break;
        case EV_RESET:
            Serial.println(F("EV_RESET"));
            break;
        case EV_RXCOMPLETE:
            // data received in ping slot
            Serial.println(F("EV_RXCOMPLETE"));
            break;
        case EV_LINK_DEAD:
            Serial.println(F("EV_LINK_DEAD"));
            break;
        case EV_LINK_ALIVE:
            Serial.println(F("EV_LINK_ALIVE"));
            break;
        default:
            break;
    }

}

void do_send(){
    if (LMIC.opmode & OP_TXRXPEND) {
        Serial.println(F("OP_TXRXPEND, not sending"));
    } else {
        LMIC_setTxData2(1, (uint8_t*)userMessage, strlen(userMessage), 1);
    }
}


void setup() {
    Serial.begin(115200);
    #ifdef VCC_ENABLE
    pinMode(VCC_ENABLE, OUTPUT);
    digitalWrite(VCC_ENABLE, HIGH);
    #endif

    os_init();
    LMIC_reset();
    LMIC_setAdrMode(1);
    LMIC_setLinkCheckMode(0);
    //LMIC_setDrTxpow(DR_SF10,10);
    LMIC_selectSubBand(0);
}
//the main code
void loop() {
    os_runloop_once();
    //Serial.println("1");
    if (Serial.available()) {
      //inString = Serial.readString();
      //Serial.print(inString);
      readUserInput();
      if (strcmp(userMessage, "#BEGIN") == 0 && !on) {
        //do_send();
        LMIC_startJoining();
        //LMIC_clrTxData ();
        on = true;
      }
      else if (strcmp(userMessage, "#BEGIN") != 0 && on && strcmp(userMessage, "#QUIT") != 0) {
        //Serial.println(userMessage);
        //LMIC_clrTxData ();
        // Only send if there's a message
        do_send();
        //LMIC_clrTxData ();
      }
      else if (strcmp(userMessage, "#QUIT") == 0) { 
        LMIC_reset();
        LMIC_setAdrMode(1);
        LMIC_setLinkCheckMode(0);
        LMIC_setDrTxpow(DR_SF10,10);
        LMIC_selectSubBand(0);
        Serial.println("Quit");
        on = false;
         //os_runloop_once();
      }
        
    }
}
