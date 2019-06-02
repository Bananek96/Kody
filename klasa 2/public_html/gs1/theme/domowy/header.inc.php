<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title><?php get_page_clean_title(); ?> &lt; <?php get_site_name(); ?></title>

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
    
  <!-- Bootstrap -->
  <link rel="stylesheet" href="<?php get_theme_url(); ?>css/bootstrap.min.css">

  <!-- Font Awesome, zob. How to Use: https://fontawesome.bootstrapcheatsheets.com -->
  <link rel="stylesheet" href="<?php get_theme_url(); ?>https://use.fontawesome.com/releases/v5.0.8/css/solid.css" integrity="sha384-v2Tw72dyUXeU3y4aM2Y0tBJQkGfplr39mxZqlTBDUZAb9BGoC40+rdFCG0m10lXk" crossorigin="anonymous">
  <link rel="stylesheet" href="<?php get_theme_url(); ?>https://use.fontawesome.com/releases/v5.0.8/css/fontawesome.css" integrity="sha384-q3jl8XQu1OpdLgGFvNRnPdj5VIlCvgsDQTQB6owSOHWlAurxul7f+JpUOVdAiJ5P" crossorigin="anonymous">

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.js"></script>
  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
  <![endif]-->

  <!-- twoje style -->
  <link rel="stylesheet" href="<?php get_theme_url(); ?>css/style.css">
  <?php get_header(); ?>
</head>
