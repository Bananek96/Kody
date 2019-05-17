<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Rock</title>

  <!-- Bootstrap -->
  <link rel="stylesheet" href="css/bootstrap.min.css">

  <!-- Font Awesome, zob. How to Use: https://fontawesome.bootstrapcheatsheets.com -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css" integrity="sha384-v2Tw72dyUXeU3y4aM2Y0tBJQkGfplr39mxZqlTBDUZAb9BGoC40+rdFCG0m10lXk" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/fontawesome.css" integrity="sha384-q3jl8XQu1OpdLgGFvNRnPdj5VIlCvgsDQTQB6owSOHWlAurxul7f+JpUOVdAiJ5P" crossorigin="anonymous">

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.js"></script>
  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
  <![endif]-->

  <!-- twoje style -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  <!-- brak java scriptu -->
  <noscript>
    Do pełnej funkcjonalności strony potrzebujesz włączonej obsługi skryptów.
    Tu znajdziesz <a href="https://www.enable-javascript.com/pl/" target="_blank">
    instrukcje, które pozwolą Ci włączyć skrypty w Twojej przeglądarce</a>.
  </noscript>

  <!-- nieaktualna przeglądarka, zob. dostosowanie: https://browser-update.org/customize.html -->
  <script>
    var $buoop = {notify:{e:-6,f:-4,o:-4,s:-2,c:-4},insecure:true,api:5};
    function $buo_f(){
      var e = document.createElement("script");
      e.src = "http://browser-update.org/update.min.js";
      document.body.appendChild(e);
    };
    try {document.addEventListener("DOMContentLoaded", $buo_f,false)}
    catch(e){window.attachEvent("onload", $buo_f)}
  </script>

  <!-- Nagłówek strony: menu, logo, breadcrumbs itp. -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="index.html"><img src="img/koles.png" class="rounded float-left col-md-2"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav float-center">
        <li class="nav-item active">
          <a class="nav-link" href="index.html">Geneza rocka<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="scenapl.html">Scena polska</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="scenasw.html">Scena światowa</a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- Treść główna -->
  <div class="container-wrapper">
    <div class="container text-center">
      <img class="rounded img-fluid" src="img/rock.svg" alt="Responsive image">
      <p class="align-center"><b>Rock</b> – gatunek muzyki rozrywkowej powstały w połowie XX wieku w Stanach Zjednoczonych. Dziś to najpopularniejszy typ muzyki rozrywkowej, który wytworzył wokół siebie krąg subkultury młodzieżowej.<br><br>
        Jest to muzyka gł. wokalno-instrumentalna. Utwory charakteryzują się dominacją silnie akcentowanego motorycznego rytmu. Pod względem tonalnym są oparte na harmonii systemu dur-moll, z rzadka sięgając do rozszerzonej tonalności lub atonalizmu, czy też do skal orientalnych lub skal muzyki dawnej i ludowej. Podstawową formą muzyki rockowej jest piosenka zwrotkowa. Wszystkie style rockowe charakteryzują się brzmieniem opartym na różnego rodzaju gitarach i perkusji, z wyraźnie zarysowanym rytmem i śpiewem, wywodzącym się z bluesa, oraz sposobem wolnej improwizacji w trakcie grania utworów, wywodzącym się z jazzu.<br><br>
W latach 50. i 60. rock stał się symbolem rewolucji obyczajowej, tworząc dotychczas nieznaną w takim wymiarze subkulturę młodzieżową. Koncentrował się na sposobie myślenia swojej generacji, a kolejne zespoły utożsamiały się ze swoim pokoleniem. Prosta, silnie rytmizowana muzyka i obrazoburcze teksty często też mają podtekst seksualny. Jednakże już poczynając od lat 70. rock (w większości swoich nowych odmian) przestawał być formą młodzieżowej subkultury, a stawał się jedynie muzyką taneczną młodych i nurtem pop music.</p>
<img class="rounded img-fluid" src="img/koncert.png" alt="Responsive image">
    </div>
  </div>

  <!-- Stopka strony: copyrights, dodatkowe linki itp. -->
  <div class="container">
    <p  class="navbar navbar-expand-lg navbar-dark bg-dark text-light">&copy; Bananek</p>
  </div>

  <!-- jQuery library -->
  <script src="js/jquery-3.3.1.min.js"></script>
  <!-- Bootstrap JavaScript and Popper JS (https://popper.js.org) -->
  <script src="js/bootstrap.bundle.min.js"></script>

</body>
</html>
