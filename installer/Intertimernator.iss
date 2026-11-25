#define MyAppName "Intertimernator"
#define MyAppVersion "1.0.2"
#define MyAppExeName "Intertimernator.exe"

[Setup]
AppId={{A6D18B29-2D87-4E85-99B6-61D1F14A8B10}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer
OutputBaseFilename=Intertimernator-v{#MyAppVersion}-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
UninstallFilesDir={app}\uninstall

[Dirs]
Name: "{app}\_internal"; Attribs: hidden
Name: "{app}\uninstall"; Attribs: hidden


[Files]
Source: "dist\Intertimernator\Intertimernator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Intertimernator\msg.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Intertimernator\msg.txt"; DestDir: "{app}"; Flags: onlyifdoesntexist
Source: "dist\Intertimernator\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{app}\Uninstall Intertimernator"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Desktop-Verknüpfung erstellen"; GroupDescription: "Zusätzliche Symbole:"; Flags: unchecked

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{#MyAppName} starten"; Flags: postinstall nowait skipifsilent
