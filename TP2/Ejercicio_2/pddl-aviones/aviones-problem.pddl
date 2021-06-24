(define (problem carga-aerea)
    (:domain aviones)
    (:objects 
        LA01
        LA02
        LA03
     	LA04
     	LA05
        AA01
        AA02
        AA03
        FB01
        FB02
        FB03
     	FB04
        MDZ
        AEP
        COR
        SFN
     	MDQ
     	PAR
     	TKY
     	NYC
     	WSG
        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES
     	ALFAJORES
     	FERNET
     	VINO
     	MADERA
     	DURAZNOS
     	REMERAS
    )
    (:init 
        (avion LA01)
        (avion LA02)
        (avion LA03)
     	(avion LA04)
     	(avion LA05)
        (avion AA01)
        (avion AA02)
        (avion AA03)
        (avion FB01)
        (avion FB02)
        (avion FB03)
     	(avion FB04)
        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)
     	(aeropuerto MDQ)
     	(aeropuerto PAR)
     	(aeropuerto TKY)
     	(aeropuerto NYC)
     	(aeropuerto WSG)
        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)
        (carga ALFAJORES)
     	(carga FERNET)
    	(carga VINO)
     	(carga MADERA)
     	(carga DURAZNOS)
     	(carga REMERAS)
        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 COR)
        (en LA04 PAR)
        (en LA05 TKY)
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 AEP)
        (en FB01 COR)
        (en FB02 AEP)
        (en FB03 SFN)
        (en FB04 NYC)
        (en FERTILIZANTE AEP)
        (en TELA-GRANIZO SFN)
        (en COSECHADORA MDZ)
        (en AUTOPARTES COR)
     	(en FERNET COR)
        (en ALFAJORES MDQ)
        (en VINO MDZ)
        (en MADERA COR)
        (en DURAZNOS PAR)
        (en REMERAS TKY)
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES AEP)
            (en FERNET TKY)
            (en ALFAJORES NYC)
            (en VINO PAR)
            (en MADERA MDZ)
            (en DURAZNOS AEP)
	    (en REMERAS MDZ)
        )
    )
)