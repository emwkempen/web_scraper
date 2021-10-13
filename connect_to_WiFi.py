def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Ziggo4479854', 'kdrc4sdLvyn5')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())



# pin = machine.Pin(2, machine.Pin.OUT)
        #
        # for i in range(10):
        #     pin.value(1)
        #     time.sleep(0.5)
        #     pin.value(0)
        #     time.sleep(0.5)
        #
        # connect_to_WiFi.do_connect()