{ pkgs }: {
  deps = [
    pkgs.python312
    pkgs.python312Packages.flask
    pkgs.python312Packages.flask_cors
  ];
}
