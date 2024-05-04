import os
import subprocess
import stem.connection
import stem.control
import keyboard

class TorConnection:
    def __init__(self):
        self.controller = None

    def connect_to_tor(self):
        try:
            while True:
                print("Tentando conectar ao cliente Tor...")
                with open('/run/tor/control.authcookie', 'rb') as cookie_file:
                    cookie_data = cookie_file.read().strip().decode('latin1')
                    self.controller = stem.control.Controller.from_port(port=9051)
                    self.controller.authenticate()
                    print("Conexão ao cliente Tor estabelecida com sucesso!")
                    
                    # Aguardar até que o usuário pressione 'q' para sair
                    print("Pressione 'q' para sair.")
                    keyboard.wait('q')
                    break
                    
        except PermissionError:
            print("Permissão negada ao tentar acessar o arquivo de cookie do Tor. Solicitando senha do sudo...")
            subprocess.run(["sudo", "python", "TNWconn.py"]) # Pedir a senha do sudo e tentar novamente
        except stem.connection.AuthenticationFailure as exc:
            print(f"Erro de autenticação ao conectar ao cliente Tor: {exc}")
        except Exception as e:
            print(f"Erro ao conectar ao cliente Tor: {e}")

if __name__ == "__main__":
    tor_connection = TorConnection()
    tor_connection.connect_to_tor()


"""
Output:                                                                                                                                                                          
┌──(eduardo㉿eduardor)-[~/repos/A-Nony/src]
└─$ python TNWconn.py                        
Tentando conectar ao cliente Tor...
Permissão negada ao tentar acessar o arquivo de cookie do Tor. Solicitando senha do sudo...
Tentando conectar ao cliente Tor...
Conexão ao cliente Tor estabelecida com sucesso!
Pressione 'q' para sair.

"""
"""
Test:

Trecho da página whatsmyip.com:
	<div class="logo-container">
			<a href="https://whatismyipaddress.com">
				<img src="https://whatismyipaddress.com/wp-content/themes/wipa-bb-child/src/images/main-logo.png" alt="What Is My IP Address? Logo" width="433" height="144">
			</a>
		</div>
		<div class="ip-address-list">

			<p>My IP Address is:</p>
			


<p class="ip-address">IPv4: <span class="tooltip"><span>?</span> <span>The most common IP version assigned by ISPs.</span></span> <span class="address" id="ipv4"><a href="https://whatismyipaddress.com/ip/191.54.164.26" style="color:#fff;">191.54.164.26</a></span></p><p class="ip-address">IPv6: <span class="tooltip"><span>?</span> <span>A newer, longer IP format many networks use.</span></span> <span class="address" id="ipv6">Not detected</span><img src="https://ds6.whatismyipaddress.com/ds6.php?token=7d52e8f0deb19f8b24e615e5afeb9978" alt="" width="1" height="1"></p>
			
		</div>		
		<div class="call-to-action">
		
					
					<p>Your location may be exposed!</p>				
		
				
			<p><a href="https://whatismyipaddress.com/ip/191.54.164.26">Show Complete IP Details</a></p>
		</div>
		<div class="ip-information">
			<p class="label">My IP Information:</p>
			<div class="inner">
				        <p class="information"><span>ISP:</span> <span>Algar Telecom S/A</span></p>	 <p class="information"><span>City:</span> <span>Recife</span></p>				     <p class="information"><span>Region:</span> <span>Pernambuco</span></p>				    <p class="information"><span>Country:</span> <span>Brazil</span></p>			</div>
		</div>
	</div>
	
	<div class="right">
		<div class="map-wrapper desktop">
			<div id="map_desktop">
				<div><img src="https://whatismyipaddress.com/wp-content/uploads/blue-world-map.gif" width="270" height="270"><div class="leaflet-map-pane" style="transform: translate3d(-53px, 0px, 0px);"><div class="leaflet-tile-pane"><div class="leaflet-layer"><div class="leaflet-tile-container"></div><div class="leaflet-tile-container leaflet-zoom-animated"><img class="leaflet-tile leaflet-tile-loaded" style="height: 256px; width: 256px; transform: translate3d(-43px, -233px, 0px);" src="https://maps.whatismyipaddress.info/tiles/osm/6/25/32.png"><img class="leaflet-tile leaflet-tile-loaded" style="height: 256px; width: 256px; transform: translate3d(213px, -233px, 0px);" src="https://maps.whatismyipaddress.info/tiles/osm/6/26/32.png"><img class="leaflet-tile leaflet-tile-loaded" style="height: 256px; width: 256px; transform: translate3d(-43px, 23px, 0px);" src="https://maps.whatismyipaddress.info/tiles/osm/6/25/33.png"><img class="leaflet-tile leaflet-tile-loaded" style="height: 256px; width: 256px; transform: translate3d(213px, 23px, 0px);" src="https://maps.whatismyipaddress.info/tiles/osm/6/26/33.png"></div></div></div><div class="leaflet-objects-pane"><div class="leaflet-shadow-pane"></div><div class="leaflet-overlay-pane"></div><div class="leaflet-marker-pane"><img src="https://whatismyipaddress.com/wp-content/uploads/marker_sq.png" class="leaflet-marker-icon leaflet-zoom-animated leaflet-clickable" style="margin-left: -8px; margin-top: -12px; width: 16px; height: 16px; transform: translate3d(162px, 135px, 0px); z-index: 135;" tabindex="0"></div><div class="leaflet-popup-pane"><div class="leaflet-popup  leaflet-zoom-animated" style="opacity: 1; transform: translate3d(162px, 135px, 0px); bottom: 6px; left: -138px;"><a class="leaflet-popup-close-button" href="#close">×</a><div class="leaflet-popup-content-wrapper"><div class="leaflet-popup-content" style="width: 238px;"><a href="https://whatismyipaddress.com/ip/191.54.164.26" style="text-decoration:none;">Click for more details about <b>191.54.164.26</b></a></div></div><div class="leaflet-popup-tip-container"><div class="leaflet-popup-tip"></div></div></div></div></div></div><div class="leaflet-control-container"><div class="leaflet-top leaflet-left"><div class="leaflet-control-zoom leaflet-bar leaflet-control"><a class="leaflet-control-zoom-in leaflet-disabled" href="#" title="Zoom in">+</a><a class="leaflet-control-zoom-out" href="#" title="Zoom out">-</a></div></div><div class="leaflet-top leaflet-right"></div><div class="leaflet-bottom leaflet-left"></div><div class="leaflet-bottom leaflet-right"><div class="leaflet-control-attribution leaflet-control"><a href="http://leafletjs.com" title="A JS library for interactive maps">Leaflet</a> | © OpenStreetMap <a href="https://www.openstreetmap.org/copyright">Terms</a></div></div></div></div>
			</div>
			<div class="text">
				<p>Location not accurate?</p>
				<p><a href="https://whatismyipaddress.com/geolocation-update-notice">Update My IP Location</a></p>

"""
