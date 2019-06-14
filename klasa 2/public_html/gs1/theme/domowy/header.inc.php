<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title><?php get_page_clean_title(); ?> &lt; <?php get_site_name(); ?></title>


  <!-- Bootstrap -->
  <link rel="stylesheet" href="<?php get_theme_url(); ?>css/bootstrap.min.css">


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
