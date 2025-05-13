flowchart TD
    Start([Start])
    Main[test_met_autotje()]
    InitAuto[Initialiseer Autotje]
    RadioInit[Initialiseer RadioCom kanaal]
    DriverInit[Initialiseer Motordriver]
    LoopAuto[Loop: Simple_remote_control()]
    ReadRadio[Lees radio kanaal]
    IfSignal{Signaal ontvangen?}
    NoSignal[Zet alles op 0\nstop auto]
    ParseInput[Zet ontvangen signaal om in lijst]
    Forward[Indien Top-knop: vooruit]
    Backward[Indien A + B: achteruit]
    SpinLeft[Indien A: draai links]
    SpinRight[Indien B: draai rechts]
    StopAuto[Geen signaal: stop]
    End([Einde])

    Start --> Main --> InitAuto
    InitAuto --> RadioInit --> DriverInit --> LoopAuto
    LoopAuto --> ReadRadio --> IfSignal
    IfSignal -- Nee --> NoSignal --> StopAuto
    IfSignal -- Ja --> ParseInput
    ParseInput --> Forward --> LoopAuto
    ParseInput --> Backward --> LoopAuto
    ParseInput --> SpinLeft --> LoopAuto
    ParseInput --> SpinRight --> LoopAuto
    ParseInput --> StopAuto --> LoopAuto

    %% Remote controller component
    subgraph RemoteController
        RCStart([Start Remote])
        InitRemote[Initialiseer Remote object]
        LoopRemote[Loop: update()]
        ReadButtons[Lees knoppen (logo, A, B)]
        SendMessage[Verzend bitstring via radio]
        RCDisplay[Toon "S" op scherm]
        RCStart --> InitRemote --> LoopRemote
        LoopRemote --> ReadButtons --> SendMessage --> RCDisplay --> LoopRemote
    end
