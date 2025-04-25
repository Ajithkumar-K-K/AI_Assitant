[Setup]
AppName=WindowsAssist
AppVersion=1.0
DefaultDirName={pf}\WindowsAssist
DefaultGroupName=WindowsAssist
OutputDir=.
OutputBaseFilename=WindowsAssistSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\WindowsAssist.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Tesseract-OCR\*"; DestDir: "{app}\Tesseract-OCR"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\WindowsAssist"; Filename: "{app}\WindowsAssist.exe"
Name: "{commondesktop}\WindowsAssist"; Filename: "{app}\WindowsAssist.exe";

[Run]
Filename: "{app}\WindowsAssist.exe"; Description: "Launch application"; Flags: nowait postinstall skipifsilent

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "WindowsAssist"; ValueData: """{app}\WindowsAssist.exe"""; Flags: uninsdeletevalue